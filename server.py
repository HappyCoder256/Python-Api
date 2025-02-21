import flask

app = flask.Flask(__name__)

@app.route('/Home')
def home():
    return "This is the N9INI API, Thanks for loving and supporting us!"

@app.route('/direc')
def direc():
    return "This is the n9ini main_directory lets dive into the deepest world together!"

@app.route('/movies')
def movies():
    return "Here is the beauty start of entertainment!"

if __name__ == '__main__':
    app.run()
