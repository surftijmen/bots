from bs4 import BeautifulSoup
import requests

page = "https://www.google.com"

def getPage(site):
    print(site)
    try:    
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')
        print("page " + site + " printed!")
        return(str(soup))
    except:
        return "invalid page"

if __name__ == "__main__":
    getPage(page)
