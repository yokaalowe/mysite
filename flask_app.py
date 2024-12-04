from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
# import dns.resolver
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'your_secret_key'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)

# def check_mx_record(email):
#     """Проверка существования MX-записи домена email."""
#     domain = email.split('@')[1]
#     try:
#         dns.resolver.resolve(domain, 'MX')
#         return True
#     except dns.resolver.NoAnswer:
#         return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_email():
    email = request.form.get('textInput', '').strip().lower()

    # # Валидация email
    # if not email or '@' not in email or not check_mx_record(email):
    #     flash('Некорректный email-адрес!', 'error')
    #     return redirect(url_for('index'))

    # # Проверка на наличие email в базе
    # if User.query.filter_by(email=email).first():
    #     flash('Email уже существует!', 'error')
    #     return redirect(url_for('index'))
    # if  email == StringField('Email', validators=[DataRequired(),Email())

    # Добавление email в базу
    if "." and "@" in email:
        new_user = User(email=email)
        db.session.add(new_user)
        db.session.commit()

    flash('Спасибо за подписку!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создание таблиц в базе данных
    app.run(debug=True)
