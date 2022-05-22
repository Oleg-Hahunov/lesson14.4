from flask import Flask, request


app = Flask(__name__)


@app.route("/", methods=['GET', "POST"])
def test_page():
    name = request.values.get('name')
    return f"Вы ввели имя {name}"


app.run()