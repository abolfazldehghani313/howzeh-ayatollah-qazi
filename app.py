from flask import Flask, session
import os

from config import Config
from models import db

app = Flask(__name__)

# بارگذاری تنظیمات
app.config.from_object(Config)

# کلید امنیتی Session
app.secret_key = app.config["SECRET_KEY"]

# اتصال دیتابیس
db.init_app(app)

# ساخت پوشه تصاویر
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# ساخت جداول
with app.app_context():
    db.create_all()

# بارگذاری Route ها
from routes.main import *
from routes.news import *
from routes.calendar import *
from routes.contact import *
# اجرای برنامه
if __name__ == "__main__":
    app.run(debug=True)