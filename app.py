import csv
import json
import secrets
from flask import Flask, render_template, jsonify, send_file, request


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


@app.route("/favicon.ico")
def favicon():
    return send_file("static/favicon.ico", mimetype="image/x-icon")


@app.route("/")
def index():
    return render_template("index.html")


# -----------------------------
#  Teams
# -----------------------------
@app.route("/currentteamback")
def currentteamback():
    teams = []
    with open("teams.csv", "r") as f:
        reader = csv.reader(f)

        for row in reader:
            data = {}
            data["number"] = row[0]
            data["name"] = row[1]
            data["uni"] = row[2]
            data["flag"] = row[3]

            teams.append(data)

        with open("data.json", "r") as f:
            savedData = json.load(f)
            try:
                currentTeam = savedData["currentTeam"]
            except:
                currentTeam = {"number": "", "name": "",
                               "uni": "", "flag": ""}

        for i in range(1, len(teams)):
            if teams[i]["number"] == currentTeam["number"]:
                teams[i]['selected'] = 'true'
                break

    return render_template("currentteamback.html", teams=teams[1:])


@app.route("/currentteamfront")
def currentteamfront():
    with open("data.json", "r") as f:
        savedData = json.load(f)
        try:
            currentTeam = savedData["currentTeam"]
        except:
            currentTeam = {"number": "", "name": "",
                           "uni": "", "flag": ""}

    return render_template("currentteamfront.html", team=currentTeam)


# -----------------------------
#  Best Run
# -----------------------------
@app.route("/bestrun")
def bestrunback():
    return render_template("bestrun.html")


# -----------------------------
#  F1
# -----------------------------
@app.route("/sport/f1/<id>")
def f1(id):
    return render_template(f"f1/backend.html")


@app.route("/sport/f1/<id>/show")
def f1_frontend(id):
    return render_template(f"f1/frontend.html")


# ------------------------------------------------------------------------------------
# -----------------------------
#   API
# -----------------------------
@app.route("/api/currentteam", methods=["GET", "POST"])
def currentteam_api():
    if request.method == "GET":
        with open("data.json", "r") as f:
            savedData = json.load(f)

        return jsonify(savedData["currentTeam"])
    elif request.method == "POST":
        data = {}
        data["number"] = request.json["number"]
        data["name"] = request.json["name"]
        data["uni"] = request.json["uni"]
        data["flag"] = request.json["flag"]

        with open("data.json", "r") as f:
            savedData = json.load(f)
            savedData["currentTeam"] = data

        with open("data.json", "w") as f:
            json.dump(savedData, f)

        return jsonify({"message": "success"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True)
