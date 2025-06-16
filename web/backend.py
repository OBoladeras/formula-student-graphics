import os
import csv
import json
import html
import requests
import pandas as pd
from io import StringIO
from bs4 import BeautifulSoup

class times():
    def __init__(self) -> None:
        self.categories = ["combustion&electric", "driverless", "classic-cup"]
        self.subcategories = ["endurance", "trackdrive", "skidpad", "acceleration", "autocross"]

    def get_data_from(self, cat: str, sub: str) -> list:
        if cat not in self.categories or sub not in self.subcategories:
            raise ValueError("Invalid category or subcategory")

        if sub in ("endurance", "trackdrive"):
            return self.readEndurance(cat)
        elif sub == "acceleration":
            return self.readAcceleration(cat)
        elif sub == "autocross":
            return self.readAutocross(cat)
        elif sub == "skidpad":
            return self.readSkidpad(cat)
            

    def readEndurance(self, category: str) -> list:
        if category not in self.categories:
            raise ValueError("Invalid category. Choose from: " +
                             ", ".join(self.categories))
        if category == "combustion&electric":
            url = "http://www.pde-racing.com/tol/temps1434.asp"
        elif category == "driverless":
            url = "http://www.pde-racing.com/tol/temps1433.asp"
        elif category == "classic-cup":
            url = "http://www.pde-racing.com/tol/temps1515.asp"

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

        data = df.values.tolist()[2:]
        clean_data = []
        for team in data:
            team.pop(0)
            team.pop(0)
            vehicle = team.pop(3).lower()
            team[3] = team[1]
            team.insert(5, f"static/cars/{team[1]}.png")
            team.pop(8)
            team.pop(8)
            team.pop(8)
            team.pop(8)
            team.pop(9)
            team.pop(-1)
            team.pop(-1)
            team.pop(-1)
            team.pop(-1)
            team.pop(-1)
            team.pop(-1)
            team.pop(-1)

            clean_data.append(team)

        return clean_data

    def readAcceleration(self, category: str) -> list:
        if category not in self.categories:
            raise ValueError("Invalid category. Choose from: " +
                             ", ".join(self.categories))
        if category == "combustion&electric":
            url = "http://fss2024.ddns.net/Acceleracio.aspx"
        elif category == "driverless":
            url = "http://fss2024.ddns.net/DL_Acceleracio.aspx"
        elif category == "classic-cup":
            url = "http://fss2024.ddns.net/CUP_Acceleracio.aspx"

        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        table = soup.find('table', id='GridView_Resultats')
        table_html = str(table)
        df = pd.read_html(StringIO(table_html), decimal=',', thousands='.')[0]

        data = df.values.tolist()
        position = 1
        for i in data:
            i.insert(0, position)
            position += 1

            i[-1] = f"{float(i[-1]):.3f}s"

        return data

    def readAutocross(self, category: str) -> list:
        if category not in self.categories:
            raise ValueError("Invalid category. Choose from: " +
                             ", ".join(self.categories))
        if category == "combustion&electric":
            url = "http://fss2024.ddns.net/Autocross.aspx"
        elif category == "classic-cup":
            url = "http://fss2024.ddns.net/CUP_Autocross.aspx"

        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        table = soup.find('table', id='GridView_Resultats')
        table_html = str(table)
        df = pd.read_html(StringIO(table_html), decimal=',', thousands='.')[0]

        data = df.values.tolist()
        position = 1
        for i in data:
            i.insert(0, position)
            position += 1

            i[-1] = f"{float(i[-1]):.3f}s"

        return data

    def readSkidpad(self, category: str) -> list:
        if category not in self.categories:
            raise ValueError("Invalid category. Choose from: " +
                             ", ".join(self.categories))
        if category == "combustion&electric":
            url = "http://fss2024.ddns.net/SkidPad.aspx"
        elif category == "driverless":
            url = "http://fss2024.ddns.net/DL_SkidPad.aspx"

        response = requests.get(url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        table = soup.find('table', id='GridView_Resultats')
        table_html = str(table)
        df = pd.read_html(StringIO(table_html), decimal=',', thousands='.')[0]

        data = df.values.tolist()
        position = 1
        for i in data:
            i.insert(0, position)
            position += 1

            i[-1] = f"{float(i[-1]):.3f}s"

        return data


if __name__ == "__main__":
    times().readSkidpad("combustion&electric")
