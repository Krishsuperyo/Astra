import os
import sys
import time
import logging
import platform
import subprocess

from typing import Union, List
from tronx.methods import Methods





if not os.path.exists("downloads"):
	""" all files are downloaded here """
	os.mkdir("downloads")



# versions /
userbot_version = "v.0.0.5"
assistant_version = "v.0.0.1"
python_version = str(platform.python_version())
pyrogram_version = str(pyrogram.__version__)

# database /
DB_URI = Config.DB_URI
db_status = "Available" if DB_URI else "Not Available"

# containers
CMD_HELP = {}
HELP = {}
	
# configurations shortcut /
LOG_CHAT = Config.LOG_CHAT
PREFIX = Config.PREFIX
SESSION = Config.SESSION
TOKEN = Config.TOKEN
API_ID = Config.API_ID
API_HASH = Config.API_HASH
WORKERS = Config.WORKERS
USER_BIO = Config.USER_BIO

# owner details /
OWNER_NAME = "࿇•ẞᗴᗩSԵ•࿇"
OWNER_ID = 1790546938
OWNER_USERNAME = "@BEASTZX"

# other /
REPO = "https://github.com/beastzx18/Tron"
StartTime = time.time()




def clear():
	""" clear terminal logs """
	subprocess.call("clear" if os.name == "posix" else "cls") 




def add_user(user_id: Union[int, List[int]], chat_id: str):
	""" Add users in groups / channels """
	try:
		done = app.add_chat_members(
			chat_id, 
			user_id
			)
		return True if done else False
	except Exception as e:
		print(e)




# check if the bot is in log chat 
def exists(user_id: int, chat_id: str):
	_data = []
	_data.clear()
	lime = app.get_chat_members(chat_id)

	for x in lime:
		_data.append(x.user.id)
	return True if user_id in _data else False




def check_bot_in_log_chat():
	try:
		if bot:
			print("Checking presence of bot in log chat . . .\n")
			try:
				if exists(BOT_ID, LOG_CHAT) is False:
					add_user(
						LOG_CHAT,
						BOT_ID
					)
					print(f"Added bot in log chat . . .\n")
				else:
					print(f"Bot is present in log chat . . .\n")
			except PeerIdInvalid:
				print("Peer id is invalid, Manually send a message in log chat . . .\n")
				pass
		else:
			log.warning("Bot is not available, please check (TOKEN, API_ID, API_HASH)")
	except Exception as e:
		print(e)




def get_readable_time(seconds: int) -> str:
	count = 0
	ping_time = ""
	time_list = []
	time_suffix_list = ["s", "m", "h", "days"]

	while count < 4:
		count += 1
		remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
		if seconds == 0 and remainder == 0:
			break
		time_list.append(int(result))
		seconds = int(remainder)

	for x in range(len(time_list)):
		time_list[x] = str(time_list[x]) + time_suffix_list[x]
	if len(time_list) == 4:
		ping_time += time_list.pop() + ", "

	time_list.reverse()
	ping_time += ":".join(time_list)

	return ping_time




def uptime():
	""" Bot active time """
	return get_readable_time(time.time() - StartTime)





class Collector(Methods, Config):
	# versions /

	userbot_version = "v.0.0.5"
	assistant_version = "v.0.0.1"
	python_version = str(platform.python_version())
	pyrogram_version = str(pyrogram.__version__)

	# database /

	db_status = "Available" if Config.DB_URI else "Not Available"

	# containers /

	CMD_HELP = {}
	HELP = {}

	# owner details /

	OWNER_NAME = "࿇•ẞᗴᗩSԵ•࿇"
	OWNER_ID = 1790546938
	OWNER_USERNAME = "@BEASTZX"

	# other /

	Repo = "https://github.com/beastzx18/Tron"
	StartTime = time.time()

	# debugging /

	logging.basicConfig(level=logging.WARNING)
	log = logging.getLogger(__name__)

	# telegraph /

	telegraph = Telegraph()
	telegraph.create_account(short_name=USER_NAME if USER_NAME else "Tron userbot")





class Tron(Client, Collector):
	""" Userbot """
	def __init__(self):
		super().__init__(
		session_name=self.SESSION,
		api_id=self.API_ID,
		api_hash=self.API_HASH,
		workers=self.WORKERS,
		)
       
	class bot(Client, Collector):
		""" Assistant """
		def __init__(self):
			super().__init__(
			session_name="Nora",
			api_id=self.API_ID,
			api_hash=self.API_HASH,
			bot_token=self.TOKEN,
			)





app = Tron() 
bot = Tron.Nora()







