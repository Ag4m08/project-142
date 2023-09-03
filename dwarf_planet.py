from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

dwarf_planet_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(dwarf_planet_url)
print(page)

soup = bs(page.text,'html.parsel')
dwarf_table = soup.find('table')

temp_list = []
table_rows = dwarf_table.find_all('tr')

for tr in table_rows :
    td = tr.find_all('td')
    row = [i.text.r_strip() for i in td]
    temp_list.append(row)

dwarfs_name = []
constellation = []
right_ascention = []
declination = []
magnitude = []

for i in range(1,len(temp_list)):

    dwarfs_name.append(temp_list[i][1])
    constellation.append(temp_list[i][3])
    right_ascention.append(temp_list[i][5])
    declination.append(temp_list[i][6])
    magnitude.append(temp_list[i][7])

df2 = pd.DataFrame(list(zip(dwarfs_name,constellation,right_ascention,declination,magnitude)),columns=['dwarfs_name','constellation','right_ascention','declination','magnitude'])

print(df2)

df2.to_csv('dwarf_planet_csv')