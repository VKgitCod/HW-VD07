from flask import Flask, render_template, redirect, url_for, flash, request
from config import Config
from models import db, User
from forms import EditProfileForm

app = Flask(__name__)
app.config.from_object(Config)

# Инициализация базы данных
db.init_app(app)

# Создание базы данных при старте приложения
with app.app_context():
    db.create_all()


# Маршрут для редактирования профиля
@app.route('/edit_profile/<int:user_id>', methods=['GET', 'POST'])
def edit_profile(user_id):
    user = User.query.get_or_404(user_id)
    form = EditProfileForm()

    if form.validate_on_submit():
        user.name = form.name.data
        user.email = form.email.data
        if form.password.data:
            user.set_password(form.password.data)

        db.session.commit()
        flash('Профиль успешно обновлен!', 'success')
        return redirect(url_for('edit_profile', user_id=user.id))

    # Заполняем форму текущими данными пользователя
    if request.method == 'GET':
        form.name.data = user.name
        form.email.data = user.email

    return render_template('profile.html', form=form, user=user)


if __name__ == '__main__':
    with app.app_context():
        # Проверим, есть ли уже пользователь с таким email
        if not User.query.filter_by(email='test@example.com').first():
            user = User(name='Test User', email='test@example.com')
            user.set_password('password123')
            db.session.add(user)
            db.session.commit()
            print("Тестовый пользователь добавлен.")
        else:
            print("Тестовый пользователь уже существует.")

    app.run(debug=True)