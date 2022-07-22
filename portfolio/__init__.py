from os import abort
from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "images/habit-tracker.jpg",
        "hero": "images/habit-tracker.jpg",
        "categories": ["python", "flask", "html", "css"],
        "slug": "habit-tracking",
        "prod": "https://custom-habit-tracker.herokuapp.com",
        "code": "https://github.com/arooshrana2/habit-tracker"
    },
    {
        "name": "Micro Blog with Flask and MongoDB",
        "thumb": "images/micro-blog.jpg",
        "hero": "images/micro-blog-hero.jpg",
        "categories": ["python", "flask", "html", "css"],
        "slug": "micro-blog",
        "prod": "http://microblog-python-flask.herokuapp.com",
        "code": "https://github.com/arooshrana2/microblog-python-flask"
    },
]

slug_for_projects = {project['slug']: project for project in projects}

@app.route('/')
def home():
    return render_template('home.html', projects=projects)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/project/<string:slug>')
def project_page(slug: str):
    if slug not in slug_for_projects:
        abort(404)

    return render_template(
        f'project_{slug}.html',
        project=slug_for_projects[slug]
    )
