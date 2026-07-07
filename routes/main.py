from app import app
from flask import render_template, request, redirect, session
from models import News


# صفحه اصلی
@app.route("/")
def home():
    all_news = News.query.order_by(News.id.desc()).all()
    return render_template("index.html", news=all_news)


# درباره حوزه
@app.route("/about")
def about():
    return render_template("about.html")


# ورود مدیر
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if (
            username == app.config["ADMIN_USERNAME"]
            and
            password == app.config["ADMIN_PASSWORD"]
        ):

            session["admin"] = True

            return redirect("/admin")

        return render_template(
            "login.html",
            error="نام کاربری یا رمز عبور اشتباه است."
        )

    return render_template("login.html")


# خروج مدیر
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


# داشبورد مدیریت
@app.route("/admin")
def admin():

    if not session.get("admin"):
        return redirect("/login")

    return render_template("admin/dashboard.html")