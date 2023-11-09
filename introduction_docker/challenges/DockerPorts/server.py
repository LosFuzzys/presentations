import flask


app = flask.Flask(__name__)

@app.route("/")
def index_route():
    return "LosCTF{Ports_exist!}"


if __name__ == "__main__":
    app.run("0.0.0.0", 8080)
