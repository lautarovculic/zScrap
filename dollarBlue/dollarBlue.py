#python3 -m pip install requests beautifulsoup4
#Lautaro Villarreal Culic'
import requests
from bs4 import BeautifulSoup
#Set URL
url = "https://www.valordolarblue.com.ar/"

if "__main__" == __name__:
    #GET method request
    page = requests.get(url)
    #Process the content
    soup = BeautifulSoup(page.content, "html.parser")

    #Function
    def has_data_search(tag):
        return tag.has_attr("class")

    results = soup.find_all(has_data_search)

    for values in results:
        #Compra/Buy
        compra = values.find("div", attrs={"class": "value", "title": "Precio de compra del Dólar Blue en la Argentina"}).get_text()
        #Venta/Sell
        venta = values.find("div", attrs={"class": "value", "title": "Precio de venta del Dólar Blue en la Argentina"}).get_text()
        #Brecha/Gap
        brecha = values.find("p", attrs={"class": "brecha"}).get_text()

        values = "${}\n${}\nBrecha: {}"
        #Format values
        values = values.format(venta, compra, brecha)
        #Show values
        print(values)
        #Break the for, we only want a value from each
        break
