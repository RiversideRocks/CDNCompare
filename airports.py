import requests
from bs4 import BeautifulSoup

def airport(code):
    soup = BeautifulSoup(requests.get("https://www.travelmath.com/airport/" + code).text, 'html.parser')
    for x in soup.find_all('p'):
        if "Latitude/Longitude" in x.text:
            cords = x.text[20:]
            lat = cords.split(", ")[0]
            long = cords.split(", ")[1]
            return [float(lat), float(long)]
    return None

def yourCordinates():
    r = requests.get("https://ipapi.co/json")
    return [r.json()["latitude"], r.json()["longitude"]]