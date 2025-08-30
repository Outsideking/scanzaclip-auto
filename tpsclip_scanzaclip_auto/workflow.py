from scanner import scan_website
from generator import generate_commands
from scanzaclip_api import run_scanzaclip

def auto_generate_workflow(url):
    dom_structure = scan_website(url)
    commands = generate_commands(dom_structure)
    
    # ส่งคำสั่งให้ scanzaclip process
    sc_results = run_scanzaclip({"commands": commands})
    
    print("Workflow Generated & Scanzaclip processed:")
    for cmd, res in zip(commands, sc_results):
        print(f"{cmd} -> {res}")
    
    return commands, sc_results

if __name__ == "__main__":
    url = "https://example.com"
    auto_generate_workflow(url)
