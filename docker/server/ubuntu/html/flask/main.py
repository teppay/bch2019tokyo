from flask import *

app = Flask(__name__)

@app.route("/")
def index():
    #title = "index"
    title = debug()
    return render_template("index.html", title = title)

def debug():
    #title = "index"
    title = type(render_template("index.html", title = "test"))
    return render_template("index.html", title = title)

@app.route("/", methods=["POST"])
def post():
    title = "POST"
    display_string = request.form["data"]
    return render_template("result.html", title = title, display_string = display_string)

if __name__ == "__main__":
    app.debug= True
    #app.run(host='0.0.0.0', port=5000)
    app.run(host='0.0.0.0', port=80)
