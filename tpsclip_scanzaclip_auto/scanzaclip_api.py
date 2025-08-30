# ตัวอย่างเชื่อม scanzaclip core
import requests

SCANZACLIP_API = "http://localhost:5000/api"  # backend ของคุณ

def run_scanzaclip(input_data):
    response = requests.post(f"{SCANZACLIP_API}/process", json=input_data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("scanzaclip processing failed")
