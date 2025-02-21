import flask

app = flask.Flask(__name__)

@app.route('/Home')
def index():
    return "This is the N9INI API, Thanks for loving and supporting us!"
@app.route('/direc')
def index():
    return "This is the n9ini main_directory lets dive into the deepest world together!"
@app.route('/movies')
def index():
    return "Here is the beauty start of entertainment!"

if __name__ == '__main__':
    app.run()
