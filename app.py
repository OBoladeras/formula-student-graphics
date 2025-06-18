import csv
import json
import secrets
# from backend import files, times
from flask import Flask, render_template, jsonify, send_file, request


# backend = files()
# raceTimes = times()
app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


def get_current_team() -> str:
    try:
        with open("data.json", "r", encoding="UTF-8") as f:
            current_team_number = json.load(f)["current_team_number"]
    except:
        current_team_number = ""

    return current_team_number


def update_current_team(team_number: str) -> None:
    with open("data.json", "r", encoding="UTF-8") as f:
        savedData = json.load(f)
        savedData["current_team_number"] = team_number

    with open("data.json", "w", encoding="UTF-8") as f:
        json.dump(savedData, f, indent=4)


@app.route("/favicon.ico")
def favicon():
    return send_file("static/favicon.ico", mimetype="image/x-icon")


@app.route("/", methods=["GET", "POST"])
def index():
    #    if request.method == "POST":
    #         return jsonify({"message": backend.race(request.json["race"])})

    return render_template("index.html")  # , race=backend.race())


# -----------------------------
#   Teams
# -----------------------------
@app.route("/graphic_manager")
def teams():
    teams = []
    with open("teams.csv", "r", encoding="UTF-8") as f:
        reader = csv.reader(f)

        for row in reader:
            data = {}
            data["number"] = row[0]
            data["name"] = row[1]

            teams.append(data)

    for i in range(1, len(teams)):
        if teams[i]["number"] == get_current_team():
            teams[i]["selected"] = "true"
            break

    teams = sorted(teams[1:], key=lambda x: int(x["number"]))

    with open("data.json", "r") as f:
        data = json.load(f)
    graphics_status = data.get("graphics_status", {})

    return render_template("graphic_manager.html", teams=teams, graphics_status=graphics_status)


@app.route("/vmix")
def vmix():
    with open("data.json", "r") as f:
        data = json.load(f)
    graphics_status = data.get("graphics_status", {})

    return render_template("vmix.html", current_team_number=get_current_team(), graphics_status=graphics_status)


"""
# -----------------------------
#   Best Run
#       SKIDPAD
#       ACCELERATION
#       AUTOCROS
# -----------------------------
@app.route("/bestrun")
def bestrun():
    return render_template("bestrun.html")


# -----------------------------
#   ENDURANCE
# -----------------------------
@app.route("/endurance")
def endurance():
    return render_template("endurance.html")


# -----------------------------
#   STANDINGS
# -----------------------------
@app.route("/standings")
def standings():
    return render_template("standings.html")
"""


# ------------------------------------------------------------------------------------
# -----------------------------
#   API
# -----------------------------
@app.route("/api/vmix", methods=["GET"])
def vmix_api():
    with open("data.json", "r") as f:
        data = json.load(f)

    return jsonify(data)


@app.route("/api/select_team", methods=["GET", "POST"])
def select_team():
    if request.method == "GET":
        return jsonify({"current_team": get_current_team()})

    elif request.method == "POST":
        update_current_team(request.json["number"])

        return jsonify({"message": "Team selected successfully."})


@app.route("/graphics_status/<graphic_name>", methods=["POST"])
def graphics_status(graphic_name):
    if request.method == "POST":
        show = request.json.get("show", False)
        print(f"Updating graphic '{graphic_name}' to show: {show}")

        with open("data.json", "r") as f:
            data = json.load(f)

        with open("data.json", "w") as f:
            data["graphics_status"][graphic_name] = show
            print(data)
            json.dump(data, f)

        return jsonify({"message": "Graphic status updated successfully."})


@app.route("/api/update_location", methods=["POST"])
def update_location():
    if request.method == "POST":
        location = request.json.get("location", "")
        print(f"Updating location to: {location}")

        with open("data.json", "r") as f:
            data = json.load(f)

        with open("data.json", "w") as f:
            data["location"] = location
            json.dump(data, f)

        return jsonify({"message": "Location updated successfully.", "status": "success"})


"""
@app.route("/api/best")
def best_api():
    return jsonify(raceTimes.bestTime(backend.race()))


@app.route("/api/endurance")
def endurance_api():
    return jsonify(raceTimes.endurance())


@app.route("/api/standings")
def standings_api():
    return jsonify(raceTimes.standings(files().race()))
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
