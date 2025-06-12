from backend import times
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    endurance = times().readEndurance()
    print(endurance)

    return render_template('index.html', endurance=endurance)


if __name__ == '__main__':
    app.run(debug=True)
