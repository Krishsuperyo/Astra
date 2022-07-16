import os

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors.exceptions.bad_request_400 import BotInlineDisabled

from main import app, gen

from pyrogram.types import (
    Message,
    CallbackQuery,
)




app.CMD_HELP.update(
    {"help" : (
        "help",
        {
        "help [ module name ]" : "Get commands info of that plugin.",
        "help" : "Get your inline help dex.",
        "inline" : "Toggle inline mode to On or Off of your bot through @BotFather",
        "mods" : "Get list of available module names",
        "plugs" : "Get list of available plugin names",
        }
        )
    }
)


helpdex_ids = [x for x in app.getdv("DELETE_TAB_ID").strip("[]").split("," " ") if bool(app.getdv("DELETE_TAB_ID"))]


@app.bot.on_callback_query(filters.regex("delete-tab"))
@app.alert_user 
async def delete_helpdex(_, cb: CallbackQuery):
    if not bool(helpdex_ids):
        await cb.answer(
            "This message is expired, hence it can't be deleted !",
            show_alert=True,
        )
    else:
        try:
            for x in helpdex_ids[1:]: # list
                for y in x: # dicts
                    if y in ("None", "none", None):
                        continue
                    await app.delete_messages(int(y), x[y])
                    app.deldv("DELETE_TAB_ID") # empty var
        except Exception as e:
            app.log.error(e)





@app.on_message(gen("help", exclude =["sudo"]))
async def helpdex_handler(_, m: Message):
    args = m.command if app.long() > 1 else False

    try:
        if args is False:
            await app.send_edit(". . .", text_type=["mono"])
            result = await app.get_inline_bot_results(
                app.bot.username, 
                "#helpdex" 
            )
            if result:
                await m.delete()
                info = await app.send_inline_bot_result(
                    m.chat.id, 
                    query_id=result.query_id, 
                    result_id=result.results[0].id, 
                    disable_notification=True, 
                )
                
                if m.chat.type in [ChatType.BOT, ChatType.PRIVATE]:
                    app.setdv("DELETE_TAB_ID", helpdex_ids.append({m.chat.id : info.updates[1].message.id}))
                else:
                    app.setdv("DELETE_TAB_ID", helpdex_ids.append({m.chat.id : info.updates[2].message.id}))
            else:
                await app.send_edit("Please check your bots inline mode is on or not . . .", delme=3, text_type=["mono"])
        elif args:

            module_help = await app.PluginData(args[1])
            if not module_help:
                await app.send_edit(f"Invalid module name specified, use `{app.PREFIX}mods` to get list of modules", delme=3)
            else:
                await app.send_edit(f"**MODULE:** {args[1]}\n\n" + "".join(module_help))
        else:
            await app.send_edit("Try again later !", text_type=["mono"], delme=3)
    except BotInlineDisabled:
        await app.toggle_inline()
        await helpdex_handler(_, m)
    except Exception as e:
        await app.error(e)




# get all module name
@app.on_message(gen("mods", exclude =["sudo"]))
async def allmodules_handler(_, m: Message):
    store = []
    store.clear()
    for x in os.listdir("tronx/modules/"):
        if not x in ["__pycache__", "__init__.py"]:
            store.append(x + "\n")

    await app.send_edit("**MODULES OF USERBOT:**\n\n" + "".join(store))




# get all plugins name
@app.on_message(gen("plugs", exclude =["sudo"]))
async def allplugins_handler(_, m: Message):
    store = []
    store.clear()
    for x in os.listdir("tronx/plugins/"):
        if not x in ["__pycache__", "__init__.py"]:
            store.append(x + "\n")

    await app.send_edit("**PLUGINS OF BOT:**\n\n" + "".join(store))




@app.on_message(gen("inline", exclude =["sudo"]))
async def toggleinline_handler(_, m: Message):
    return await app.toggle_inline()


