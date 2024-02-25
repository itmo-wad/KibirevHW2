from flask import Flask
from flask import render_template, redirect

from depends import SECRET_KEY, TEMPLATE_FOLDER
from api import api_router
from utils import login_requiered


app = Flask(__name__)
app.secret_key = SECRET_KEY
app.template_folder = TEMPLATE_FOLDER

app.register_blueprint(api_router)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/profile')
@login_requiered
def profile():
    return render_template('profile.html')


@app.errorhandler(404)
def page_not_found(e):
    return redirect('/')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
