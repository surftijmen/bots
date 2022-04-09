from bs4 import BeautifulSoup
import requests

page = "https://www.google.com/search?q=whats+my+ip&rlz=1C1ONGR_nlNL952NL952&oq=whats+my+ip"

def getPage(site):
    print(site)
    try:    
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')
        return(str(soup))
    except:
        return "invalid page"

if __name__ == "__main__":
    getPage(page)

getPage(page)