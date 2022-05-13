from flask import Flask, template_rendered
import utils
import json

app = Flask(__name__)


@app.route('/')


def list_candidates():
    with open('candidates.json', 'r', encoding='UTF-8') as file:
        candidates = json.load(file)
    return template_rendered('list.html', candidates=candidates)


app.run()
