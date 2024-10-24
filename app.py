from flask import Flask
from datetime import datetime
# create object of flask
app = Flask(__name__)

print('Flask')

@app.route('/')

def home():
    return """
    <html>
    <body>
    <h1>Hello WORLD
    """ + str(datetime.now()) + """ 
    <body>
    <html>
"""    

if __name__ == "__main__":
    app.run(host='0.0.0.0' ,port=5001 , debug=True)