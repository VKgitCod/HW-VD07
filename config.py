class Config:
    SECRET_KEY = 'supersecretkey'  # Ключ для защиты сессий Flask
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'  # Путь к базе данных SQLite
    SQLALCHEMY_TRACK_MODIFICATIONS = False