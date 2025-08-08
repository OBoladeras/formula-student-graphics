import csv
import json
import secrets
from backend import times
from flask import Flask, render_template, jsonify, request


raceTimes = times()
app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)
JSON_PATH = 'data.json'


def get_current_team() -> str:
    try:
        with open(JSON_PATH, "r", encoding="UTF-8") as f:
            current_team_number = json.load(f)["current_team_number"]
    except:
        current_team_number = ""

    return current_team_number


@app.route("/")
@app.route("/vmix")
def vmix():
    with open(JSON_PATH, "r") as f:
        data = json.load(f)
    graphics_status = data.get("graphics_status", {})
    current_speaker1 = data.get("current_speaker1")
    current_speaker2 = data.get("current_speaker2")

    last_run_times = [333, 333, 333, 'combustion', 7.216]

    return render_template("vmix.html", current_team_number=get_current_team(), graphics_status=graphics_status, current_speaker1=current_speaker1, current_speaker2=current_speaker2, last_run_times=last_run_times)


@app.route("/endurance")
@app.route("/autocross")
def endurance():
    with open(JSON_PATH, "r") as f:
        data = json.load(f)
        fileName = "classic.csv" if data['classic'] else "teams.csv"

        if data['race'] == "endurance":
            race = "endurance"
        elif data['race'] == "autocross":
            race = "autocross"
        else:
            race = "unknown"

    with open(fileName, "r", encoding="UTF-8") as f:
        all_teams = list(csv.reader(f))[1:]

    return render_template("endurance.html", teams=all_teams, race=race)


@app.route('/api/endurance_times')
def get_teams():
    try:
        with open(JSON_PATH, "r") as f:
            data = json.load(f)
            if data['race'] == "endurance":
                data = times().endurance()[:8]
            elif data['race'] == "autocross":
                data = times().autocross()[:8]

        return jsonify(data)
    except:
        return jsonify([])

# ------------------------------------------------------------------------------------
# -----------------------------
#   API
# -----------------------------


@app.route("/api/vmix", methods=["GET"])
def vmix_api():
    with open("data.json", "r") as f:
        data = json.load(f)

    return jsonify(data)


@app.route("/api/select_team", methods=["GET"])
def select_team():
    return jsonify({"current_team": get_current_team()})


@app.route("/api/best")
def best_api():
    with open("data.json", "r") as f:
        race = json.load(f)["race"]
    try:
        return jsonify(raceTimes.bestTime(race))
    except:
        return {}


@app.route('/manager', methods=['GET', 'POST'])
def index():
    with open(JSON_PATH, 'r') as f:
        data = json.load(f)

    if request.method == 'POST':
        data['race'] = request.form['race']
        data['classic'] = 'classic' in request.form
        data['current_team_number'] = request.form['current_team_number']
        data['location_text'] = request.form['location_text']
        data['current_speaker1']['name'] = request.form['speaker1_name']
        data['current_speaker1']['info'] = request.form['speaker1_info']
        data['current_speaker2']['name'] = request.form['speaker2_name']
        data['current_speaker2']['info'] = request.form['speaker2_info']

        data['last_run'] = []
        for i in range(3):
            number = request.form.get(f'last_run_{i}_number', '0')
            time = request.form.get(f'last_run_{i}_time', '0')
            try:
                time = float(time)
            except ValueError:
                time = 0.0
            data['last_run'].append({"number": number, "time": time})

        for key in data['graphics_status']:
            data['graphics_status'][key] = key in request.form

        with open(JSON_PATH, 'w') as f:
            json.dump(data, f, indent=4)
        return render_template('graphic_manager.html', data=data, success=True)

    return render_template('graphic_manager.html', data=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8081", debug=False)
