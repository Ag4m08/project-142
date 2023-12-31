from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

bright_star_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

page = requests.get(bright_star_url)
print(page)

soup = bs(page.text,'html.parsel')
star_table = soup.find('table')

temp_list = []
table_rows = star_table.find_all('tr')

for tr in table_rows :
    td = tr.find_all('td')
    row = [i.text.r_strip() for i in td]
    temp_list.append(row)

stars_name = []
distance = []
mass = []
radius = []
luminosity = []

for i in range(1,len(temp_list)):

    stars_name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    luminosity.append(temp_list[i][7])

df2 = pd.DataFrame(list(zip(stars_name,distance,mass,radius,luminosity)),columns=['stars_name','distance','mass','radius','luminosity'])

print(df2)

df2.to_csv('bright_stars_csv')