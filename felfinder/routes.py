import sys

from flask import request, session, jsonify
from flask_cors import cross_origin

from felfinder import app
from felfinder.connector import ElFinderConnector

#from config import DISPATCH_DICT

def arg_translate(req):

    cmd = req.form.get('cmd')
    init = req.form.get('init')
    
    # Take the parameters from the dictionary and use them here

    d = {'init': init}

    return d

# NOTE: THIS IS INSECURE ATM BECAUSE IT ALLOWS ALL CROSS_ORIGIN. DISABLE
# WHEN DEVELOPING
    
@app.route("/", methods=['GET', 'POST'])
@cross_origin(origins= '*', supports_credentials=True)
def index():

    print(request.form)
    
    # is_init = request.form.get('init')
    # if is_init:
    #    session['connect'] = ElFinderConnector()

    elf = ElFinderConnector()
    
    arg_d = arg_translate(request)
    resp = elf.open(**arg_d)
    
    return jsonify(resp)
    

        
    
    
