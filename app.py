from stories import *
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/")
"""Take user to page for selecting template"""
def render_home():
    return render_template("home.html", stories=stories.values())


@app.route("/form")
"""Show user a form for picking words based off selected template"""
def render_form():
    story_title = request.args["story_title"]
    story = stories[story_title]
    prompts = story.prompts
    return render_template("form.html", prompts=prompts, story_title=story_title)


@app.route("/story")
"""Display story with user's words"""
def render_story():
    story_title = request.args["story_title"]
    story = stories[story_title]
    text = story.generate(request.args)
    return render_template("story.html", text=text, title=story_title)
