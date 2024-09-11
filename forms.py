from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class EditProfileForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    email = StringField('Почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[
        DataRequired(),
        EqualTo('confirm_password', message='Пароли должны совпадать')
    ])
    confirm_password = PasswordField('Подтверждение пароля', validators=[DataRequired()])
    submit = SubmitField('Обновить профиль')