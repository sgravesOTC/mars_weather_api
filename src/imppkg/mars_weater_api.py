import requests
from datetime import datetime

class MarsWeatherAPI():

    BASE_URL = "https://api.nasa.gov/insight_weather/"

    def __init__(self, api_key:str, feedtype:str='json',version = 1.0):
        self.api_key = api_key
        self.feedtype = feedtype
        self.version = version
    
    def get_all_weather(self):

        params ={
            "api_key": self.api_key,
            "feedtype": self.feedtype,
            "version": self.version
        }

        try:
            response = requests.get(self.BASE_URL , params=params)
            data = response.json()
        except Exception as e:
            raise e


# api = MarsWeatherAPI('j2DrCXQ7xeKYu6ab2wNfjogCgdVo4k4hPC5JZoxk')

# api.get_all_weather()