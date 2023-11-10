from flask import Flask, jsonify
from flask_restless import APIManager
from waitress import serve
from config.config_reader import config

# models
from model import db
from model.general import Gender, Publisher, User, SportType
from model.competion import Season, Competion, CompetionGroup, CompetionTeamMap, CompetionSeasonMap, CompetionType, CompetionRound, PublisherCompetionMap
from model.match import Match, ResultCode
from model.team import Team, Player, TeamType

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = config['database_uri']

@app.route('/')
def api_run():
    return jsonify({'message': 'Hello World'})


def create_rest_api():
    with app.app_context():
        manager = APIManager(app, flask_sqlalchemy_db=db)
        # create api for each model
        manager.create_api(Gender, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                            allow_delete_many=True)
        manager.create_api(Publisher, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                            allow_delete_many=True)
        manager.create_api(User, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                            allow_delete_many=True)
        manager.create_api(SportType, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                            allow_delete_many=True)
        manager.create_api(Season, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                            allow_delete_many=True)
        manager.create_api(Competion, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                            allow_delete_many=True)
        manager.create_api(CompetionGroup, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                            allow_delete_many=True)
        manager.create_api(CompetionTeamMap, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                            allow_delete_many=True)
        manager.create_api(CompetionSeasonMap, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                            allow_delete_many=True)
        manager.create_api(CompetionType, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                            allow_delete_many=True)
        manager.create_api(CompetionRound, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                             allow_delete_many=True)
        manager.create_api(PublisherCompetionMap, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                                allow_delete_many=True)
        manager.create_api(Match, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                                allow_delete_many=True)
        manager.create_api(ResultCode, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                                allow_delete_many=True)
        manager.create_api(Team, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                                allow_delete_many=True)
        manager.create_api(Player, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                                allow_delete_many=True)
        manager.create_api(TeamType, url_prefix='/api/v2.0/model', methods=['GET', 'PUT', 'POST', 'DELETE'],
                                allow_delete_many=True)
        
def main():
    if "threads" in config:
        server_thread_count = config.get("threads")
    else:
        server_thread_count = 4 
    serve(app, host=config["http_host"], port=config["http_port"], threads=server_thread_count)

if __name__ == '__main__':
    main()