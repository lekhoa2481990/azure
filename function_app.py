import azure.functions as func
import logging
import pymongo
import os
import json
from bson.json_util import dumps

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="getNotesV10")
def getNotesV10(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        try:
            # url = "mongodb://khoalnn:mDPJzMcELxlra55KL2rxdmr7FHU2tNAJlIKyKBBKtzqA1mR80lhZQJl3hfpearSbwoIt28a4hFGIACDbUTIVIg==@khoalnn.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&maxIdleTimeMS=120000&appName=@khoalnn@" # Change the Variable name, as applicable to you
            url = os.environ["MyDbConnection"] 
            client = pymongo.MongoClient(url)
            database = client['lab2db'] # Change the MongoDB name
            collection = database['notes']    # Change the collection name


            result = collection.find({})
            result = dumps(result)

            return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
        except ConnectionError:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb",
                                     status_code=400)
        # return func.HttpResponse(
        #      "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
        #      status_code=200
        # )

@app.event_grid_trigger(arg_name="azeventgrid")
def myEventGridTrigger(azeventgrid: func.EventGridEvent):
    logging.info('Python EventGrid trigger processed an event')
