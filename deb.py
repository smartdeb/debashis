'''
Created on 03-Nov-2016

@author: Debashis Panda
'''
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()