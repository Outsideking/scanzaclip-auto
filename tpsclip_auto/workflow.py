from scanner import scan_website
from generator import generate_commands

def auto_generate_workflow(url):
    dom_structure = scan_website(url)
    commands = generate_commands(dom_structure)
    print("Workflow Generated:")
    for cmd in commands:
        print(cmd)
    return commands

# ตัวอย่างการรัน
if __name__ == "__main__":
    url = "https://example.com"
    auto_generate_workflow(url)
