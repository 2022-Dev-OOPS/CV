from flask import Flask
import yaml
import os


config_path = os.path.dirname(os.path.abspath(__file__)) + "/config.yaml"


with open(config_path) as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

host = config["flask_config"]["host"]
port = config["flask_config"]["port"]

exec_commend = config["detect_config"]["commend"]
source = config["detect_config"]["source"]

app = Flask(__name__)

@app.route('/person_detect', methods=['POST'])
def person_detect() :
    os.system(exec_commend + source)
    return "No person detect"

if __name__ == "__main__" :
    app.run(host=host, debug=True, port=port) 