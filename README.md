# Formula Student Spain - Graphics 🏎️

This repository contains the code for the graphics of the Formula Student Spain competition. This graphics are used on the streaming of the competition and on the official website.

## Description 📖

All graphics, except `Current Team` are updated in real time. The data is obtained from the official API of the competition.
`Best Run` and `Team Standings` can be used in any competition, category, Endurance, Acceleration, Autocross and Skidpad.  

To let the app know which competition is running, a user have to select the category from in the main page. The app will show the graphics of the selected category.

### Graphics 🎆
- **Best Run** - Shows the best run of the competition with the time and the team.
![image](https://github.com/user-attachments/assets/a290d3ad-431c-469e-b222-2d2c6b8efcae)

- **Current Team** - Shows the current team, number, flag and university of the driver.
![image](https://github.com/user-attachments/assets/fc6292c9-6b0d-4eed-88f8-40a481086934)

- **Team Standings** - Shows the top teams of the competition with basic information.
![image](https://github.com/user-attachments/assets/18363a6b-b739-40cc-9a2c-ada647e9b25d)


- **Endurance** - Shows a list of the first 9 teams of the endurance race, with the time and the team.
![image](https://github.com/user-attachments/assets/4f636485-07c2-48e0-baa4-85d733a4fe49)

To seee more examples check the streams of youtube:
[@FormulaStudentSpain](https://www.youtube.com/@FormulaStudentSpain)


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

