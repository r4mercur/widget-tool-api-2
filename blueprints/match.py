from flask import Blueprint, render_template
from model.match import Match

match_blueprint = Blueprint('match', __name__)


@match_blueprint.route('/match/<int:match_id>', methods=['GET'])
def get_match(match_id: int):
    match = Match.query.get_or_404(match_id)
    return render_template('match/../templates/match/match.html', match=match)
