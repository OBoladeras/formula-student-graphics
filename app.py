import secrets
from backend import files, times
from flask import Flask, render_template, jsonify, send_file, request


backend = files()
raceTimes = times()
app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


@app.route("/favicon.ico")
def favicon():
    return send_file("static/favicon.ico", mimetype="image/x-icon")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return jsonify({"message": backend.race(request.json["race"])})

    return render_template("index.html", race=backend.race())


# -----------------------------
#   Teams
# -----------------------------
@app.route("/graphic_manager")
def teams():
    return render_template("graphic_manager.html", teams=backend.teams())



@app.route("/vmix")
def vmix():
    
    current_num = backend.team()["number"]
    
    return render_template("vmix.html", current_num=current_num)

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


# ------------------------------------------------------------------------------------
# -----------------------------
#   API
# -----------------------------
@app.route("/api/select_team", methods=["GET", "POST"])
def select_team():
    if request.method == "GET":
        return jsonify(backend.team())

    elif request.method == "POST":
        print(request.json)

        data = {}
        data["number"] = request.json["number"]

        return jsonify({"message": backend.saveTeam(data)})





@app.route("/api/best")
def best_api():
    return jsonify(raceTimes.bestTime(backend.race()))


@app.route("/api/endurance")
def endurance_api():
    return jsonify(raceTimes.endurance())


@app.route("/api/standings")
def standings_api():
    return jsonify(raceTimes.standings(files().race()))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True)
