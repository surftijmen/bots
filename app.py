import eel
import random
from requestBot.getpage import getPage

eel.init('web')

@eel.expose
def setPageContent(site):
    eel.copyPage(getPage(site))

@eel.expose
def get_random_number():
    eel.prompt_alerts(random.randint(1, 100))


eel.start('index.html')