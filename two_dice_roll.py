import random

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/api/dice/JSON')
def two_dice_roll():
    """
    Route that returns a JSON output that simulates 2 dice roll

    The route is called /api/dice/JSON as it is an API for dice roll
    simulations and returns a JSON output
    
    :return: JSON output
    """

    # Since the output needs to simulate 2 dice rolls,
    # the program randomly generates two numbers between 1 and 6

    result = {
        'dice 1': random.randint(1, 6),
        'dice 2': random.randint(1, 6),
    }

    return jsonify(result)


if __name__ == '__main__':
    app.debug = True
    app.run()
