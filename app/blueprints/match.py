from flask import Blueprint, jsonify, render_template
from app.model.match import Match

match_blueprint = Blueprint('match', __name__)


@match_blueprint.route('/match/<int:match_id>', methods=['GET'])
def get_match(match_id: int):
    match = Match.query.get_or_404(match_id)
    return render_template('match/match.html', match=match)
