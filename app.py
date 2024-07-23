import os
from backend import files
import json
import secrets
from flask import Flask, render_template, jsonify, send_file, request


app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
backend = files()
key = "losmnHjnsytTgsbaH6hs8K9o"


@app.route("/favicon.ico")
def favicon():
    return send_file("static/favicon.ico", mimetype="image/x-icon")


@app.route(f"/{key}", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return jsonify({"message": backend.race(request.json["race"])})

    return render_template("index.html", race=backend.race())


# -----------------------------
#  Teams
# -----------------------------
@app.route(f"/{key}/teams")
def teams():
    return render_template("teams.html", teams=backend.teams())


@app.route(f"/{key}/team")
def team():
    return render_template("team.html", team=backend.team())


# -----------------------------
#  Best Run
# SKIDPAD
# ACCELERATION
# AUTOCROS
# -----------------------------
@app.route(f"/{key}/bestrun")
def bestrun():
    return render_template("bestrun.html")


# -----------------------------
# ENDURANCE
# -----------------------------
@app.route(f"/{key}/endurance")
def fendurance():
    return render_template("endurance.html")


# ------------------------------------------------------------------------------------
# -----------------------------
#   API
# -----------------------------

# API endpoint to get or save the current team
@app.route(f"/{key}/api/team", methods=["GET", "POST"])
def team_api():
    if request.method == "GET":
        return jsonify(backend.team())

    elif request.method == "POST":
        data = {}
        data["number"] = request.json["number"]
        data["name"] = request.json["name"]
        data["uni"] = request.json["uni"]
        data["flag"] = request.json["flag"]

        return jsonify({"message": backend.saveTeam(data)})





# Test of where to send the data
@app.route(f"/{key}/api/<prova>", methods=["GET", "POST"])
def api(prova):
    if request.method == "GET":
        try:
            with open(f"{prova}.json", "r") as f:
                savedData = json.load(f)
        except:
            savedData = {}

        return jsonify(savedData)
    elif request.method == "POST":
        data = request.json

        with open(f"{prova}.json", "w") as f:
            json.dump(data, f)

        return jsonify({"message": "success"})

    return jsonify({"message": "error"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
