import json

from flask import Flask

app = Flask(__name__)


def load_file():
    with open('candidates.json', 'r') as file:
        candidates = json.load(file)
        return candidates


@app.route("/")
def main_profile():
    candidates = load_file()
    for candidat in candidates:
        print(f"{candidat['name']}\n{candidat['position']}\n{candidat['skills']}")

app.run()
