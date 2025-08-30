from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

def scan_website(url):
    # Static scraping
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"ไม่สามารถเข้าถึง {url}")
    soup = BeautifulSoup(response.text, 'html.parser')
    inputs = [i.get('name') for i in soup.find_all('input')]
    buttons = [b.text.strip() for b in soup.find_all('button')]
    
    # Dynamic content scraping using Selenium
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    dynamic_buttons = [b.text for b in driver.find_elements("tag name","button")]
    driver.quit()
    
    # รวมข้อมูล
    return {
        "inputs": inputs,
        "buttons": list(set(buttons + dynamic_buttons))
    }
