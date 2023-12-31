""" heroku configaration module """

HEROKUDV = [
    "HEROKU_API_KEY",
    "HEROKU_APP_NAME"
    ]




class HerokuConfig(object):
    @property
    def HerokuApiKey(self):
        """ Set your heroku auth key """
        return self.getdv("HEROKU_API_KEY") or self.HEROKU_API_KEY or None


    @property
    def HerokuAppName(self):
        """ Set your heroku app name """
        return self.getdv("HEROKU_APP_NAME") or self.HEROKU_APP_NAME or None
