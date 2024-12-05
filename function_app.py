import logging
import azure.functions as func
import json


app = func.FunctionApp()

@app.event_grid_trigger(arg_name="azeventgrid")
def myEventGridTriggerV1(azeventgrid: func.EventGridEvent):
    result = json.dumps({
        'id': azeventgrid.id,
        'data': azeventgrid.get_json(),
        'topic': azeventgrid.topic,
        'subject': azeventgrid.subject,
        'event_type': azeventgrid.event_type,
    })

    logging.info('Python EventGrid trigger processed an event:', result)
