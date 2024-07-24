import os
import csv
import json
import requests
import pandas as pd
from io import StringIO
from bs4 import BeautifulSoup


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
                data["type"] = row[4]

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


class times():
    def __init__(self) -> None:
        pass

    def bestTime(self, race: str) -> dict:
        data = {"fuel": {}, "electric": {}, "race": race}
        print(race)

        if race == "skidpad":
            url = 'http://fss2023.ddns.net/Skidpad.aspx'
        elif race == "acceleration":
            url = 'http://fss2023.ddns.net/Acceleracio.aspx'
        elif race == "autocross":
            url = 'http://fss2023.ddns.net/Autocross.aspx'

        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        if race in ["skidpad", "acceleration", "autocross"]:
            table1 = soup.find('table', id='GridView_Resultats')
            table1_html = str(table1)
            df1 = pd.read_html(StringIO(table1_html))[0]

            table2 = soup.find('table')
            table2_html = str(table2)
            df2 = pd.read_html(StringIO(table2_html))[0]

            allRuns = df1.values.tolist()
            bestRuns = df2.values.tolist()

            # Get the best time for each category
            clean = []
            for i in bestRuns[0]:
                j = i.split("-")
                tmp = []
                for k in j:
                    if "combustion" in k.lower() or "electric" in k.lower():
                        if "combustion" in k.lower():
                            tmp.append("combustion")
                        else:
                            tmp.append("electric")
                        tmp.append(k.strip().split(" ")[-1])
                    else:
                        tmp.append(k.strip())

                clean.append(tmp)

            # Get the name of the team for each best time
            for i in clean:
                for j in allRuns:
                    if int(i[1]) == int(j[0]):
                        clean[clean.index(i)].insert(2, j[3])
                        break

            # Create the dictionary with the data
            data["fuel"]["time"] = clean[0][4]
            data["fuel"]["number"] = clean[0][1]
            data["fuel"]["uni"] = clean[0][3]
            data["fuel"]["name"] = clean[0][2]

            data["electric"]["time"] = clean[1][4]
            data["electric"]["number"] = clean[1][1]
            data["electric"]["uni"] = clean[1][3]
            data["electric"]["name"] = clean[1][2]

            return data

        return data