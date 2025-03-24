from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import validators
from datetime import datetime
import time

def obter_print():
    url = input ('Colar url:')
    if not validators.url(url):
        print('Url inválida')
        return obter_print()
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--start-maximized')

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(2)
    width = 1280
    height = 720
    driver.set_window_size(width, height)
    time.sleep(2)
    info = datetime.now().strftime('%Y%m%d_%H%M%S')
    nome = f'imagem_{info}.png'
    driver.save_screenshot(nome)
    driver.quit()

   
obter_print()
