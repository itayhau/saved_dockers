from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return f'<html><h1><b>Welcome flask user!</b></h1></body></html>';

app.run(host="0.0.0.0", port=8080);
