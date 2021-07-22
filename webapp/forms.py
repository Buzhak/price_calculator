from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, SelectField, SubmitField

class ItemForm(FlaskForm):
    material = SelectField('Выберите материал', choices=[('1', 'фанера'), ('2', 'акрил'), ('3', 'полистирол')])
    thickness = RadioField('Толщина материала', choices=[('3', '3мм'), ('4', '4мм'), ('6', '6мм'), ('8', '8мм')])
    long = IntegerField('Длинна реза в метрах')
    submit = SubmitField('Добавить и рассчитать')