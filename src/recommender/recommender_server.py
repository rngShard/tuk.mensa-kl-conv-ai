import flask
from flask import request, jsonify

from src.recommender.recommender import Recommender

app = flask.Flask(__name__)

r = Recommender()


@app.route('/')
def index():
    pass


@app.route("/userexists", methods=['GET', 'POST'])
def user_exists():
    data = request.get_json()
    user_id = data["user_id"]
    if r.users.user_exists(user_id):
        exists = 1
    else:
        exists = 0
    return jsonify({"user_exists": exists})


@app.route("/prediction", methods=['GET', 'POST'])
def predict():
    data = request.get_json()
    user_id = data["user_id"]
    prediction = r.predict(user_id)
    answer = {}
    answer["prediction"] = prediction
    return jsonify(answer)


if __name__ == "__main__":
    # with open('config.json', 'r') as f:
    #    config = json.load(f)
    app.run()
