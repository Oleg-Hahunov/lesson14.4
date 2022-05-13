from flask import Flask, render_template
import utils

app = Flask(__name__)

@app.route('/')
def list_candidates():
    candidates = utils.load_candidates_from_json('candidates.json')
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:candidate_id>')
def candidate_card(candidate_id):
    candidate = utils.get_candidate(candidate_id)
    return render_template('card.html', candidate=candidate)


@app.route('/search/<string:candidate_name>')
def search_candidate(candidate_name):
    candidate = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidate=candidate, len_candidates=len(candidate))


@app.route('/skills/<string:skill_name>')
def search_skill(skill_name):
    candidate = utils.get_candidates_by_skill(skill_name)
    return render_template('skills.html', candidate=candidate, len_candidates=len(candidate))


app.run()
