from flask import Flask, render_template, redirect, session, url_for
from webapp.forms import ItemForm

from webapp.scripts import serialize_price, cost_calc, sum_prices, MIN_COST

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('config.py')


    @app.route('/')
    def index():
        title = 'Калькулятор цен заказа'
        item_form = ItemForm()
        item_form.material.choices=serialize_price()
        if 'price' in session:
            price = [(item[0], item[1], cost_calc(item[1], item[0])) for item in session['price'].items()]
            count_price = sum_prices(price)
            order_cost_title = "Общая сумма заказа:"
        else:
            session['price'] = {}
            price = []
            order_cost_title = "Минимальная сумма заказа"
            count_price = MIN_COST

        return render_template("index.html", page_title=title, form=item_form, price=price, count_price=count_price , order_cost_title = order_cost_title)


    @app.route('/process_add_in_session', methods=['POST'])
    def process_add_in_session():
        price = ItemForm()
        if 'price' not in session:
            session['price'] = {}
        session['price'][price.material.data] = price.long.data
        session.modified = True
        
        return redirect(url_for('index'))

    
    @app.route('/clear_session')
    def clear_session():
        if 'price' in session:
            session.pop('price', None)
            session.modified = True
        return redirect(url_for('index'))
    

    return app