from flask import Blueprint, render_template, redirect, session, url_for
from webapp.calculator.forms import ItemForm


from webapp.scripts.scripts import cost_calc, sum_prices, serialize_price, MIN_COST

calculator_bp = Blueprint('calculator', __name__)

@calculator_bp.route('/')
def index():
    title = 'Калькулятор цен заказа'
    form = ItemForm()
    form.material.choices = serialize_price()


    if 'price' in session:
        price = [(item[0], item[1], cost_calc(item[1], item[0])) for item in session['price'].items()]
        count_price = sum_prices(price)
        order_cost_title = "Общая сумма заказа:"
    else:
        session['price'] = {}
        price = []
        order_cost_title = "Минимальная сумма заказа"
        count_price = MIN_COST

    return render_template("index.html", page_title=title, form=form, price=price, count_price=count_price , order_cost_title = order_cost_title)


@calculator_bp.route('/process_add_in_session', methods=['POST'])
def process_add_in_session():
    form = ItemForm()
    print(form.validate())
    print(form.errors)
    if form.validate_on_submit():
        print('!'*100)
        if 'price' not in session:
            session['price'] = {}
        session['price'][form.material.data] = form.cut.data
        session.modified = True
         
    return redirect(url_for('calculator.index'))


@calculator_bp.route('/del_item/<string:item_name>')
def del_item(item_name):
    if 'price' in session:
        del session['price'][item_name]
        session.modified = True
    return redirect(url_for('calculator.index'))


@calculator_bp.route('/clear_session')
def clear_session():
    if 'price' in session:
        session.pop('price', None)
        session.modified = True
    return redirect(url_for('calculator.index'))
