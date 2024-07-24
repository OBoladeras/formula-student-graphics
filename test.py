import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

url = 'http://fss2023.ddns.net/SkidPad.aspx'

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

table = soup.find('table', id='GridView_Resultats')

table_html = str(table)
df = pd.read_html(StringIO(table_html))[0]


print(df)
