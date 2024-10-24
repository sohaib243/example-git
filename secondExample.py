from flask import Flask, request
from datetime import datetime 

app = Flask(__name__)

INDEX_HTML = """
<html>
<body>
    <h1>HELLO {0} WORLD {1}</h1>
</body>
</html>
"""

@app.route("/")
def index():
    name = request.args.get("name", "Guest")  
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return INDEX_HTML.format(name, current_time)

if __name__ == "__main__":
    app.run(debug=True)
