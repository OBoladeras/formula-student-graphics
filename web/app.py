from backend import times
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    time_loader = times()
    data = {
        "combustion&electric": {
            "name": "Combustion & Electric",
            "times": {
                "endurance": time_loader.readEndurance("combustion&electric"),
                "acceleration": time_loader.readAcceleration("combustion&electric"),
                "autocross": time_loader.readAutocross("combustion&electric"),
                "skidpad": time_loader.readSkidpad("combustion&electric"),
            }

        },
        "driverless": {
            "name": "Driverless",
            "times": {
                "trackdrive": time_loader.readEndurance("driverless"),
                "acceleration": time_loader.readAcceleration("driverless"),
                # "autocross": time_loader.readAutocross("driverless"), Check this!!!!!!!!!!!!!!!!!
                "skidpad": time_loader.readSkidpad("driverless"),
            }
        },
        "classic-cup": {
            "name": "Classic Cup",
            "times": {
                "endurance": time_loader.readEndurance("classic-cup"),
                "acceleration": time_loader.readAcceleration("classic-cup"),
                "autocross": time_loader.readAutocross("classic-cup"),
            }
        },
    }


    import json
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
        

    return render_template('index.html', data=data, endurance=None)


if __name__ == '__main__':
    app.run(debug=True)
