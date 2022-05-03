from flask import Flask, render_template

import utils

app = Flask(__name__)


@app.route("/")
def list_candidates():
    candidates = utils.load_candidates_from_json("candidates.json")
    return render_template("list.html", candidates = candidates)

@app.route("/candidate/<int:candidate_id>")
def page_candidate(candidate_id):
    candidate = utils.get_candidate(candidate_id)
    if candidate:
        return render_template("card.html", candidate=candidate)
    else:
        abort(404)

@app.route("/skill/<string:skill_name>")
def page_candidates_skill(skill_name):
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates, candidates_count=len(candidates))

@app.route("/name/<string:candidate_name>")
def search_candidates_name(candidate_name):
    candidate = utils.get_candidates_by_name(candidate_name)
    return render_template("search.html", candidate=candidate, candidates_name_count=len(candidate))

app.run()