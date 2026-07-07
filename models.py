from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# اخبار
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200))


# تقویم آموزشی
class Calendar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(30), nullable=False)
    time = db.Column(db.String(20))
    place = db.Column(db.String(200))
    description = db.Column(db.Text)


# پیام‌های تماس
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    fullname = db.Column(db.String(100), nullable=False)

    phone = db.Column(db.String(30))

    subject = db.Column(db.String(200), nullable=False)

    text = db.Column(db.Text, nullable=False)