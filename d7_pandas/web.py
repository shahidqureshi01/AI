import requests
from bs4 import BeautifulSoup
d={}
page = requests.get("https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YFtWia9KhPZ")
page.status_code
soup= BeautifulSoup(page.content, 'html.parser')

p= body.find(id= "seven-day-forecast-container").get_text().replace("\n"," ").replace("\n\n", " ").replace("\n\n\n", " ")
print(p)
list= p.strip().split(" ")
print(list)