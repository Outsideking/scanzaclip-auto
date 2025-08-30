from github import Github
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = "Thanva/scanzaclip-auto"

def push_workflow(commands):
    g = Github(GITHUB_TOKEN)
    repo = g.get_user().get_repo(REPO_NAME)
    content = "\n".join(commands)
    repo.create_file("workflow.txt", "Add new workflow", content)
    print("Workflow pushed to GitHub")

if __name__ == "__main__":
    example_commands = ["fill_field('username','abc')", "click_button('Login')"]
    push_workflow(example_commands)
