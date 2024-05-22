from flask import Flask, jsonify
from flask_restless import APIManager
from waitress import serve
from config.config_reader import config

# models
from model import db
from model.general import Gender, Publisher, User, SportType
from model.competion import Season, Competion, CompetionGroup, CompetionTeamMap, CompetionSeasonMap, CompetionType, \
    CompetionRound, PublisherCompetionMap
from model.match import Match, ResultCode
from model.team import Team, Player, TeamType

# blueprints
from blueprints import match_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['database_uri']

app.register_blueprint(match_blueprint, url_prefix='/api/v1')


@app.route('/')
def api_run():
    return jsonify({'message': 'The API is running!'})


def create_rest_api():
    with app.app_context():
        manager = APIManager(app, flask_sqlalchemy_db=db)
        # create api for each model
        models = [Gender, Publisher, User, SportType, Season, Competion, CompetionGroup, CompetionTeamMap,
                  CompetionSeasonMap, CompetionType, CompetionRound, PublisherCompetionMap, Match, ResultCode, Team,
                  Player, TeamType]

        for model in models:
            manager.create_api(model, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                               allow_delete_many=True)


def main():
    if "threads" in config:
        server_thread_count = config.get("threads")
    else:
        server_thread_count = 4
    serve(app, host=config["http_host"], port=config["http_port"], threads=server_thread_count)


if __name__ == '__main__':
    main()
