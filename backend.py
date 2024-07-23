import os
import csv
import json
from datetime import datetime, timedelta


class files():
    def __init__(self) -> None:
        if not os.path.exists("teams.csv"):
            print("teams.csv not found")
            exit(1)

    def teams(self) -> tuple:
        teams = []
        currentTeam = self.team()

        with open("teams.csv", "r", encoding="UTF-8") as f:
            reader = csv.reader(f)

            for row in reader:
                data = {}
                data["number"] = row[5]
                data["name"] = row[1]
                data["uni"] = row[2]
                data["flag"] = row[3]

                teams.append(data)

        for i in range(1, len(teams)):
            if teams[i]["number"] == currentTeam["number"]:
                teams[i]["selected"] = "true"
                break

        return teams[1:]

    def team(self) -> dict:
        try:
            with open("data.json", "r", encoding="UTF-8") as f:
                savedData = json.load(f)
                currentTeam = savedData["currentTeam"]
        except:
            currentTeam = {"number": "", "name": "", "uni": "", "flag": ""}

        return currentTeam

    def saveTeam(self, data: dict) -> str:
        try:
            with open("data.json", "r", encoding="UTF-8") as f:
                savedData = json.load(f)
                savedData["currentTeam"] = data
        except:
            savedData = {"currentTeam": data}

        with open("data.json", "w", encoding="UTF-8") as f:
            json.dump(savedData, f)

        return "success"

    def race(self, race: str = "") -> str:
        try:
            with open("data.json", "r", encoding="UTF-8") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        if race != "":
            with open("data.json", "w", encoding="UTF-8") as f:
                data["race"] = race
                json.dump(data, f)
        else:
            try:
                race = data["race"]
            except KeyError:
                race = "skidpad"

        return race


class api():
    def __init__(self, race: str) -> None:
        self.race = race.lower()

    def read(self) -> tuple:
        if not os.path.exists(f"{self.race}.json"):
            if os.path.exists(f"{self.race.upper()}.json"):
                self.race = self.race.upper()
            else:
                return []

        with open(f"{self.race}.json", "r") as f:
            return json.load(f)

    def best(self) -> dict:
        data = self.read()
        teams = files().teams()

        if self.race.lower() == "skidpad":
            dataByTeams = {}
            for i in data:
                if i["TempsVolta"] in ["", "DNF"]:
                    continue

                time = datetime.strptime(
                    i["TempsVolta"], "%H:%M:%S.%f").microsecond

                if dataByTeams.get(i["Dorsal"]) == None:
                    dataByTeams[i["Dorsal"]] = {}

                if dataByTeams[i["Dorsal"]].get(i["Cursa"]) == None:
                    dataByTeams[i["Dorsal"]][i["Cursa"]] = time

                dataByTeams[i["Dorsal"]][i["Cursa"]] += time

            best = {'Dorsal': '', 'TempsVolta': 9 ** 9 * 9}
            for key, i in dataByTeams.items():
                for key2, j in i.items():
                    if j < best["TempsVolta"]:
                        best["Dorsal"] = key
                        best["TempsVolta"] = j

            best["TempsVolta"] = best["TempsVolta"] / 1000000 * 60
            return best


print(
    api("skidpad").best()
)
