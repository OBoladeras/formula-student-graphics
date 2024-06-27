import os
import csv
import json
import secrets
from flask import Flask, render_template, jsonify, send_file, request


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
key = "losmnHjnsytTgsbaH6hs8K9o"


@app.route("/favicon.ico")
def favicon():
    return send_file("static/favicon.ico", mimetype="image/x-icon")


@app.route(f"/{key}")
def index():
    return render_template("index.html")


# -----------------------------
#  Teams
# -----------------------------
@app.route(f"/{key}/currentteamback")
def currentteamback():
    teams = []
    with open("teams.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)

        for row in reader:
            data = {}
            data["number"] = row[6]
            data["name"] = row[1]
            data["uni"] = row[2]
            data["flag"] = row[3]

            teams.append(data)

    if not os.path.exists("data.json"):
        with open("data.json", "w") as f:
            json.dump(
                {"currentTeam": {"number": "", "name": "", "uni": "", "flag": ""}}, f
            )

    with open("data.json", "r") as f:
        savedData = json.load(f)
        try:
            currentTeam = savedData["currentTeam"]
        except:
            currentTeam = {"number": "", "name": "", "uni": "", "flag": ""}

    for i in range(1, len(teams)):
        if teams[i]["number"] == currentTeam["number"]:
            teams[i]["selected"] = "true"
            break

    return render_template("currentteamback.html", teams=teams[1:])


@app.route(f"/{key}/currentteamfront")
def currentteamfront():
    if not os.path.exists("data.json"):
        with open("data.json", "w") as f:
            json.dump(
                {"currentTeam": {"number": "", "name": "", "uni": "", "flag": ""}}, f
            )

    with open("data.json", "r") as f:
        savedData = json.load(f)
        try:
            currentTeam = savedData["currentTeam"]
        except:
            currentTeam = {"number": "", "name": "", "uni": "", "flag": ""}

    return render_template("currentteamfront.html", team=currentTeam)


# -----------------------------
#  Best Run
# -----------------------------
@app.route(f"/{key}/bestrun")
def bestrunback():
    return render_template("bestrun.html")


# -----------------------------
#  F1
# -----------------------------
@app.route(f"/{key}/sport/f1/<id>")
def f1(id):
    return render_template(f"f1/backend.html")


@app.route(f"/{key}/sport/f1/<id>/show")
def f1_frontend(id):
    return render_template(f"f1/frontend.html")


# ------------------------------------------------------------------------------------
# -----------------------------
#   API
# -----------------------------
@app.route(f"/{key}/api/currentteam", methods=["GET", "POST"])
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


@app.route(f"/{key}/api", methods=["GET", "POST"])
def api():
    if request.method == "GET":
        try:
            with open("data2.json", "r") as f:
                savedData = json.load(f)
        except:
            savedData = {}

        return jsonify(savedData)
    elif request.method == "POST":
        data = request.json

        with open("data2.json", "w") as f:
            json.dump(data, f)

        return jsonify({"message": "success"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
