from utils import *

from flask import Flask

app = Flask(__name__)


@app.route("/")
def main():
    candidates_list = get_candidates('candidates.json')
    return formatted_candidates(candidates_list)


@app.route("/candidates/<int:candidate_id>")
def candidate(candidate_id):
    candidates_list = get_candidates('candidates.json')
    selected_candidate = candidate_selection_by_id(candidates_list, candidate_id)
    image = f'<img src="{selected_candidate["picture"]}">'
    return image + formatted_candidates([selected_candidate])


@app.route("/skills/<skill>")
def skills(skill):
    candidates_list = get_candidates('candidates.json')
    selected = candidate_selection_by_skill(candidates_list, skill.lower())
    return formatted_candidates(selected)


app.run(port=5005)
