from flask import Flask, request
import json
from urllib.parse import urlparse

app = Flask(__name__)

def bash(user: str): 
    # is the string length zero? 
    if len(user)==0 or user.startswith('/') is False:
        return False 
    return True

def msg(par: str): 
    if bash(par) is False: 
        sep = {"data": {"command": None, "message": par}}
        return sep #json.dumps(sep)
    else: 
        sep = par[1:].split(' ', 1)
        val = {"data": {"command": sep[0], "message": sep[1]}}
        return val #json.dumps(val)


@app.route('/<message>', methods = ['POST'])
def last(message):
    m = msg(message)
    return str(m), 200
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 53960, debug=True)
     