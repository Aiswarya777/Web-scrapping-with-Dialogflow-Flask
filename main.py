from flask import  Flask, request, make_response, jsonify
import json
import os , sys
import time
from urllib.request import urlopen, Request


from happy import program


app = Flask(__name__)
log = app.logger

result = program()
print (result)

@app.route('/webhook', methods=['POST'])

def webhook():
    req = request.get_json(silent=True, force=True)
    action = req.get('queryResult').get('action')

    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'
    
    if action == 'jobinfo':
        return make_response(jsonify({'fulfillmentText': 'kindly tell us the location'}))
    elif action == 'location':
        return make_response(jsonify({'fulfillmentText': 'please tell us ur work experience'}))
    elif action =='experience':
        return make_response(jsonify({'fulfillmentText':result}))
    else:
        log.error('Unexpected action.')

   
        
if __name__ == '__main__':
   app.run()

