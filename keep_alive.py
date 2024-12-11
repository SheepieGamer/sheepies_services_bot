import flask


app = flask.Flask(__name__)


@app.route("/")
def home():
    return "I'm alive!"

def run():
    app.run(host="0.0.0.0", port=10000)