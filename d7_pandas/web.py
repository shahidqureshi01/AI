import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

res = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YFx-AGQzZb8')

soup = BeautifulSoup(page.content, 'html.parser')

html = list(soup.children)[2]

body = list(html.children)[3]

tag = body.find('div', {'id' : 'seven-day-forecast-container'})

text = tag.get_text().replace('\n', ' ').strip().strip()

text = re.sub(' +', ' ', text)
l = text.split(' ')


i = 0
j = 1

l2 = []
'''
below code only extract the data from days and ignore the
night time data, strores it in the l2 list
'''
while(i < len(l)): 
    if(j == 4 and (i + 3) < len(l)):
        i += 5
        j = 1
    else:
        l2.append(l[i])
        i += 1
        j += 1

# remove °F from the list

l2 = [i for i in l2 if i != '°F']

# help function to convert list to a dictionary
def Convert(lst):
    res_dct = {lst[i]: [(f'{lst[i + 1]}, {lst[i + 2 ]}')] for i in range(0, len(lst), 3)}
    return res_dct
# convert list to a dictionary
dict = Convert(l2)

print(dict)
df = pd.DataFrame(data=dict, index=[1, 2, 3, 4, 5])

df