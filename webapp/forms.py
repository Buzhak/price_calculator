from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SelectField, SubmitField

class ItemForm(FlaskForm):
    material = SelectField('Выберите материал')
    long = IntegerField('Длинна реза в метрах')
    submit = SubmitField('Добавить и рассчитать', render_kw={'class':'btn btn-primary'})