import os
import csv
import json
import html
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
                data["number"] = row[0]
                data["name"] = row[1]

                teams.append(data)

        for i in range(1, len(teams)):
            if teams[i]["number"] == currentTeam["number"]:
                teams[i]["selected"] = "true"
                break

        return sorted(teams[1:], key=lambda x: int(x["number"]))





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

    def readEndurance(self) -> list:
        url = "http://www.pde-racing.com/tol/temps1434.asp"

        response = requests.get(url)
        decoded_data = html.unescape(response.text)

        rows = decoded_data.split('\n')

        structured_data = []
        for row in rows:
            fields = row.split('$')
            if len(fields) > 1:
                structured_data.append(fields)

        df = pd.DataFrame(structured_data)

        df.dropna(how='all', axis=1, inplace=True)
        df.dropna(how='all', axis=0, inplace=True)

        return df.values.tolist()[2:]

    def bestTime(self, race: str) -> dict:
        def split_first_last_hyphen(s):
            first_split = s.split('-', 1)

            if len(first_split) == 1:
                return first_split

            first_part = first_split[0]
            remaining_part = first_split[1]

            last_hyphen_index = remaining_part.rfind('-')

            if last_hyphen_index == -1:
                return [first_part, remaining_part]

            second_part = remaining_part[:last_hyphen_index]
            third_part = remaining_part[last_hyphen_index + 1:]

            return [first_part, second_part, third_part]

        data = {"fuel": {
            "time": "",
                    "number": "",
                    "uni": "",
                    "name": ""
        }, "electric": {
            "time": "",
                    "number": "",
                    "uni": "",
                    "name": ""
        }, "race": race}

        if race == "skidpad":
            url = 'http://fss2024.ddns.net/SkidPad.aspx'
        elif race == "acceleration":
            url = 'http://fss2024.ddns.net/Acceleracio.aspx'
        elif race == "autocross":
            url = 'http://fss2024.ddns.net/Autocross.aspx'

        if race in ["skidpad", "acceleration", "autocross"]:
            response = requests.get(url)
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

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
                j = split_first_last_hyphen(i)
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
                    try:
                        if int(i[1]) == int(j[0]):
                            clean[clean.index(i)].insert(2, j[3])
                            break
                    except:
                        pass

            # Create the dictionary with the data
            if len(clean[0]) == 5:
                data["fuel"]["time"] = clean[0][4]
                data["fuel"]["number"] = clean[0][1]
                data["fuel"]["uni"] = clean[0][3]
                data["fuel"]["name"] = clean[0][2]

            if len(clean[1]) == 5:
                data["electric"]["time"] = clean[1][4]
                data["electric"]["number"] = clean[1][1]
                data["electric"]["uni"] = clean[1][3]
                data["electric"]["name"] = clean[1][2]
        elif race == "endurance":
            list = self.readEndurance()

            for i in list:
                if i[5].lower() == 'ev' and data["electric"] == {}:
                    data["electric"]["time"] = i[14]
                    data["electric"]["number"] = i[3]
                    data["electric"]["name"] = i[4]

                    for j in files().teams():
                        if j["number"].strip() == i[3].strip():
                            data["electric"]["uni"] = j["uni"]
                            break

                elif i[5].lower() == 'cv' and data["fuel"] == {}:
                    data["fuel"]["time"] = i[14]
                    data["fuel"]["number"] = i[3]
                    data["fuel"]["name"] = i[4]
                    for j in files().teams():
                        if j["number"].strip() == i[3].strip():
                            data["fuel"]["uni"] = j["uni"]
                            break

                if data["fuel"] != {} and data["electric"] != {}:
                    break

        return data

    def endurance(self) -> list:
        data = []
        list = self.readEndurance()

        for i in list:
            tmp = {}

            tmp["name"] = i[4]
            tmp["class"] = i[5].lower()
            tmp['number'] = i[3]
            tmp['best'] = i[14]
            if i[8] == "Retirado":
                tmp['last'] = "DNF"
            else:
                tmp['last'] = i[8]

            data.append(tmp)

        return data[:9]

    def standings(self, race: str) -> list:
        data = [race, ]
        if race == "skidpad":
            url = 'http://fss2024.ddns.net/SkidPad.aspx'
        elif race == "acceleration":
            url = 'http://fss2024.ddns.net/Acceleracio.aspx'
        elif race == "autocross":
            url = 'http://fss2024.ddns.net/Autocross.aspx'

        if race == "endurance":
            list = self.readEndurance()
            teams = files().teams()

            for i in list:
                tmp = {"flag": ""}

                for j in teams:

                    number = i[3].strip()
                    if str(number[0]) == "0":
                        number = number[1:]

                    if j["number"].strip() == number:
                        tmp["flag"] = j["flag"]

                tmp["name"] = f"#{i[3]} {i[4]}"
                tmp["class"] = i[5]
                tmp["lap"] = i[7]
                if i[8] == "Retirado":
                    tmp['last'] = "DNF"
                else:
                    tmp['last'] = i[8]
                tmp['best'] = i[14]

                data.append(tmp)
        else:
            response = requests.get(url)
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            table = soup.find('table', id='GridView_Resultats')
            table_html = str(table)
            df = pd.read_html(StringIO(table_html))[0]

            allRuns = df.values.tolist()

            numbers = []
            for i in allRuns:
                if i[0] in numbers:
                    continue

                tmp = {}
                tmp["name"] = f"#{i[0]} {i[3]}"
                tmp["uni"] = i[4]
                if race in ["skidpad", "acceleration"]:
                    tmp["time"] = f"{str(i[-1])[0]},{str(i[-1])[1:]}"
                else:
                    tmp["time"] = f"{str(i[-1])[:2]},{str(i[-1])[2:]}"

                for j in files().teams():
                    if str(j["number"]).strip() == str(i[0]).strip():
                        tmp["flag"] = j["flag"]

                numbers.append(i[0])
                data.append(tmp)

        return data


if __name__ == "__main__":
    pass
