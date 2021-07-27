from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, SubmitField
from wtforms.validators import NumberRange

class ItemForm(FlaskForm):

    material = SelectField('Выберите материал', validate_choice=False)
    cut = IntegerField('Длинна реза в метрах', validators=[NumberRange(min=1, max = 100000)])
    submit = SubmitField('Добавить и рассчитать', render_kw={'class':'btn btn-primary'})
