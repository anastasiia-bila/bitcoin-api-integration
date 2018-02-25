from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Dima!'


if __name__ == '__main__':
    app.run()




url = "https://coinbin.org/btc/forecast"
r = requests.get()