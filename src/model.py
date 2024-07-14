from cliqual.cliqual_api import CliqualAPI

#------------------#
# GLOBAL VARIABLES #
#------------------#
Cliqual_API = None

def Init():
    global Cliqual_API
    Cliqual_API = CliqualAPI()