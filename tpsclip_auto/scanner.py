from bs4 import BeautifulSoup
import requests

def scan_website(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"ไม่สามารถเข้าถึง {url}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # ดึง input fields และ buttons
    inputs = [i.get('name') for i in soup.find_all('input')]
    buttons = [b.text.strip() for b in soup.find_all('button')]
    
    # แค่ตัวอย่าง, สามารถขยายไปจับ API calls หรือ forms
    return {
        "inputs": inputs,
        "buttons": buttons
  }
