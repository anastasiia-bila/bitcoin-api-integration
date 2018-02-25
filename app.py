from flask import Flask, render_template
from BitcoinAPIIntegration import BitcoinAPIIntegration
import json

app = Flask(__name__)

@app.route('/')
def index():
    integration = BitcoinAPIIntegration()
    data = integration.get_bitcoin_forecast_in_usd()
    labels = integration.get_bitcoin_forecast_dates()
    return render_template('index.html', data=data, labels=json.dumps(labels))


if __name__ == '__main__':
    app.run()
