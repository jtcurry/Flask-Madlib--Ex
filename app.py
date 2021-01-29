from stories import story
from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/")
def render_home():
    prompts = story.prompts
    return render_template("home.html", prompts=prompts)


@app.route("/story")
def render_story():
    text = story.generate(request.args)
    return render_template("story.html", text=text)
