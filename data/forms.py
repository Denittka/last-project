from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, BooleanField, SubmitField, FileField, IntegerField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileRequired, FileAllowed


class LoginForm(FlaskForm):
    login = StringField("Логин (email)", validators=[DataRequired()])
    password = PasswordField("Пароль", validators=[DataRequired()])
    remember = BooleanField("Запомнить в системе", default=False)
    submit = SubmitField("Войти")


class RegistrationForm(FlaskForm):
    login = StringField("Логин (email)")
    password = PasswordField("Пароль")
    confirm_password = PasswordField("Повтор пароля")
    name = StringField("Имя")
    surname = StringField("Фамилия")
    photo = FileField(
        "Фотография (не обязательно)",
        validators=[FileAllowed(['jpg', 'png', 'jpeg'],
                                "Файл должен быть одного из этих форматов: 'jpg', 'png', 'jpeg'")])
    submit = SubmitField("Отправить")


class AddProductForm(FlaskForm):
    title = StringField("Название", validators=[DataRequired()])
    description = StringField("Описание", validators=[DataRequired()])
    photo = FileField(
        "Изображение",
        validators=[FileAllowed(['jpg', 'png', 'jpeg'],
                                "Файл должен быть одного из этих форматов: 'jpg', 'png', 'jpeg'")])
    submit = SubmitField("Подтвердить")


class AuctionForm(FlaskForm):
    product = StringField("Название предмета", validators=[DataRequired()])
    number = IntegerField("Введите порядковый номер объекта из выбранных")
    submit = SubmitField("Создать аукцион")
    search = SubmitField("Поиск")


class SearchForm(FlaskForm):
    product = StringField("Название предмета", validators=[DataRequired()])
    search = SubmitField("Поиск")
    number = IntegerField("Введите порядковый номер объекта из выбранных")
    submit = SubmitField("Перейти к предмету")


class BuyForm(FlaskForm):
    cost = IntegerField("Ваша ставка", validators=[DataRequired()])
    submit = SubmitField("Сделать ставку")


class DealForm(FlaskForm):
    cost = StringField("Предлагаемая цена (обязательное поле)")
    submit = SubmitField("Отправить запрос")


class CloseForm(FlaskForm):
    submit = SubmitField("Подтвердить сделку")


class AcceptForm(FlaskForm):
    yes = SubmitField("Согласиться")
    no = SubmitField("Отказаться")
