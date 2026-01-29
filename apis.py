import os
import requests

url="https://api.nasa.gov/planetary/apod?api_key="

unique_key=os.getenv("NASA_API_KEY")

def apod_generator(base_url, unique_key):
    final_url = url + unique_key
    response = requests.get(final_url).json()
    return response
