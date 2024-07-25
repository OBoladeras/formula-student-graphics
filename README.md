# Formula Student Spain - Graphics 🏎️

This repository contains the code for the graphics of the Formula Student Spain competition. This graphics are used on the streaming of the competition and on the official website.

## Description 📖

All graphics, except `Current Team` are updated in real time. The data is obtained from the official API of the competition.
`Best Run` and `Team Standings` can be used in any competition, category, Endurance, Acceleration, Autocross and Skidpad.  

To let the app know which competition is running, a user have to select the category from in the main page. The app will show the graphics of the selected category.

### Graphics 🎆
- **[Best Run]()** - Shows the best run of the competition with the time and the team.
- **[Current Team]()** - Shows the current team, number, flag and university of the driver.
- **[Team Standings]()** - Shows the top teams of the competition with basic information.
- **[Endurance]()** - Shows a list of the first 9 teams of the endurance race, with the time and the team.

## Usage 🚀
To use the graphics, navigate to the main page, select the category and chose the graphic you want to show.  
Then copy the URL and using the Browser Source paste the URL, the graphic will be shown and updated in the streaming. 

The data source is the official API of the competition, so the data is updated in real time.
In this version the head url is: `http://fss2023.ddns.net/`

## Installation 🛠️

To install the project, you need to clone the repository, install the dependencies and run the project.

### Clone the repository 🤖
```bash
git clone https://github.com/OBoladeras/FSS.git
cd FSS
```

### Install the dependencies 📚
Create a virtual environment and install the dependencies.
```bash
pythonr3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run the project 🌐
The web app will be running on the port 8080.  
To run the project, execute the following command:
```bash
python app.py
```

\
To run the project in `production`, you can use gunicorn with the systemd service.  
Copy the service file to the systemd folder, reload the services and start the service.
```bash
sudo cp fss.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable --now fss.service
```

