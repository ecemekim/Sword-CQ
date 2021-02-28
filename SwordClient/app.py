from flask import Flask
from webapp.views import show

app = Flask(__name__)
app.debug = True

app.register_blueprint(show)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)
