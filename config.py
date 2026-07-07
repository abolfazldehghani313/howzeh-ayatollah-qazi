import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:

    # تنظیمات دیتابیس
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "instance", "howze.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # پوشه ذخیره تصاویر اخبار
    UPLOAD_FOLDER = "static/uploads/news"

    # کلید امنیتی Flask (برای Session)
    SECRET_KEY = "howze_qazi_2026_secret_key"

    # اطلاعات مدیر
    ADMIN_USERNAME = "admin"
    ADMIN_PASSWORD = "123456"