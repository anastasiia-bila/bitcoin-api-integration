import requests
import json
from datetime import datetime


class BitcoinAPIIntegration(object):

    url = "https://coinbin.org/btc/forecast"

    def __init__(self):
        self.data = self.get_request_bitcoin_forecast()
        self.forecast = self.data.get("forecast")

    def get_request_bitcoin_forecast(self):
        r = requests.get(self.url)

        return json.loads(r.text)

    def get_bitcoin_forecast_in_usd(self):
        usd_list = []
        for i in range(len(self.forecast)):
            if 'usd' in self.forecast[i].keys():
                usd_list.append(self.forecast[i].get('usd'))

        return usd_list

    def get_bitcoin_forecast_dates(self):
        timestamp_list = []
        for i in range(len(self.forecast)):
            if 'timestamp' in self.forecast[i].keys():
                temp = self.forecast[i].get('timestamp')
                # date = datetime.strptime(temp[:10], '%Y-%m-%d').date()
                timestamp_list.append(temp[:10])  # Timestamp was not parsable by Python datetime library, so I worked with date as with a string



        return timestamp_list
