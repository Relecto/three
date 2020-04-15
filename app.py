from flask import Flask, render_template
import db

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('news.html', stories = db.stories)

@app.route('/category/<category>')
def by_category(category=''):
    stories = [story for story in db.stories if story['category'] == category]

    return render_template('news.html', stories = stories)



if __name__ == '__main__':
    app.run(port=3000)

