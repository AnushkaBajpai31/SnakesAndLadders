from datetime import datetime
from flask import Flask, jsonify, request
from constants.errors import Error
from constants.game import Game
from factory.bl_factory import BLFactory

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify('Hello World! The server is up and running.')

@app.route('/play', methods=['POST'])
def play_endpoint():
    try:
        config = getConfig()
        parameters = request.get_json()
        log = generateLogFile(config['LOG_FOLDER_PATH'])
        game = BLFactory().getGame(parameters, config, log)
        result = game.play()
        closeLogFile(log)
        return jsonify(result)
    except Exception as error:
        print('Error while calling Play Endpoint: ', error)
        raise Exception(Error.GAME_ERROR)

def getConfig():
    import json
    config_file = open(Game.CONFIG)
    config = json.load(config_file)
    return config

def generateLogFile(folder):
    folder = folder + '\\' if folder[-1] != '\\' else folder
    logFile = folder + str(int(round(datetime.now().timestamp() * 1000)))+'.txt'
    f = open(logFile, "a")
    return f

def closeLogFile(f):
    f.close()

if __name__ == '__main__':
    app.run(debug=True)