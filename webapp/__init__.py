from flask import Flask, render_template, redirect, url_for
from webapp.forms import ItemForm

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        title = 'Калькулятор цен заказа'
        item_form = ItemForm()
        return render_template("index.html", page_title=title, form=item_form)

    @app.route('/process_add', methods=['POST'])
    def process_add():
        None
        return redirect(url_for('index'))
    

    return app