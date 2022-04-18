from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    pass

@app.route("/candidates/<x>")
def candidate():
    pass

@app.route("/skills/<x>")
def skills():
    pass
