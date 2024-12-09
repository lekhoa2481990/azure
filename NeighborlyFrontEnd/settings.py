#--------- Flask settings
SERVER_HOST = '0.0.0.0' # Update this for the appropriate front-end website when up
FLASK_DEBUG = False # Do not use debug mode in prod
SERVER_PORT = 8000

# Flask-Restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_404_HELP = True
API_VERSION = 'v1'

#-------- Azure constants

# API_URL format: "https://[FUNCTION_APP_NAME_GOES_HERE].azurewebsites.net"
#API_URL = " https://neighborlyapi.azurewebsites.net/api/"

# for local host if Azure functions served locally
# API_URL = "http://localhost:7071/api"
API_URL = "https://getadvertisements.azurewebsites.net/api"