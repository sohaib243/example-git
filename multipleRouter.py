from flask import Flask


app = Flask(__name__)

INDEX_HTML = """ 
<html>
<body>
 <h1>Hellow llearners</h1>
 CLick <a href="/time">here</a> for time
<body>
<html>
"""

TIME_HTML ="""
<html>
<body>
    The Time is {0}
<body>
<html>
""".format("10:33:25 AM")

@app.route('/')
@app.route('/index')
def index():
    return INDEX_HTML

@app.route('/time')

def time():
    return TIME_HTML

if __name__ == "__main__":
    app.run(debug=True)