from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests


# Enlace a wikipedia
START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Controlador web
browser = webdriver.Chrome("D:\documentos\TravisV4.1\Snacks\Python\PRO_C128_EXTRACCIÓN_DE_DATOS_WEB_2\chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

new_planets_data = []

def scrape_more_data(hyperlink):
    print(hyperlink)
    
    ## AGREGA CÓDIGO AQUÍ ##
    try:
        page = requests.get(hyperlink)
        soup = BeautifulSoup(page.content, "html.parser")
        temp_list=[]
        for tr_tag in soup.find_all("tr", attrs={"class":"fact_row"}):
            td_tags = tr_tag.find_all("td")
            for td_tag in td_tags:
                try:
                    temp_list.append(td_tag.find_all("div", attrs={"class":"value"})[0].contents[0])
                except:
                    temp_list.append("")
        new_planets_data.append(temp_list)
    except:
        time.sleep(1)
        scrape_more_data(hyperlink)


planet_df_1 = pd.read_csv("updated_scraped_data.csv")

# Llamar al método
for index, row in planet_df_1.iterrows():

     ## ADGREGA CÓDIGO AQUÍ ##

     # Llama a scrape_more_data(<hyperlink>)

    print(f"La extracción de datos del hipervínculo {index+1} se ha completado")

print(new_planets_data)

# Remover el carácter '\n' de los datos extraídos
scraped_data = []

for row in new_planets_data:
    replaced = []
    ## AGREGAR EL CÓDIGO AQUÍ ##


    
    scraped_data.append(replaced)

print(scraped_data)

headers = ["planet_type","discovery_date", "mass", "planet_radius", "orbital_radius", "orbital_period", "eccentricity", "detection_method"]

new_planet_df_1 = pd.DataFrame(scrapped_data,columns = headers)

# Convertir a CSV
new_planet_df_1.to_csv('new_scraped_data.csv', index=True, index_label="id")