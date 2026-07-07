from app import app
from models import db, News
from flask import render_template, request, redirect, session
from werkzeug.utils import secure_filename
import os


# صفحه اخبار
@app.route("/news")
def news():
    all_news = News.query.order_by(News.id.desc()).all()
    return render_template("news.html", news=all_news)


# مدیریت اخبار
@app.route("/admin/news", methods=["GET", "POST"])
def admin_news():

    # بررسی ورود مدیر
    if not session.get("admin"):
        return redirect("/login")

    if request.method == "POST":

        title = request.form["title"]
        text = request.form["text"]

        filename = ""

        image = request.files.get("image")

        if image and image.filename != "":
            filename = secure_filename(image.filename)
            image.save(
                os.path.join(app.config["UPLOAD_FOLDER"], filename)
            )

        new_news = News(
            title=title,
            text=text,
            image=filename
        )

        db.session.add(new_news)
        db.session.commit()

        return redirect("/admin/news")

    all_news = News.query.order_by(News.id.desc()).all()

    return render_template(
        "admin/news.html",
        news=all_news
    )


# ویرایش خبر
@app.route("/admin/news/edit/<int:id>", methods=["GET", "POST"])
def edit_news(id):

    # بررسی ورود مدیر
    if not session.get("admin"):
        return redirect("/login")

    news = News.query.get_or_404(id)

    if request.method == "POST":

        news.title = request.form["title"]
        news.text = request.form["text"]

        image = request.files.get("image")

        if image and image.filename != "":

            filename = secure_filename(image.filename)

            image.save(
                os.path.join(app.config["UPLOAD_FOLDER"], filename)
            )

            news.image = filename

        db.session.commit()

        return redirect("/admin/news")

    return render_template(
        "admin/edit_news.html",
        news=news
    )


# حذف خبر
@app.route("/admin/news/delete/<int:id>")
def delete_news(id):

    # بررسی ورود مدیر
    if not session.get("admin"):
        return redirect("/login")

    news = News.query.get_or_404(id)

    if news.image:

        image_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            news.image
        )

        if os.path.exists(image_path):
            os.remove(image_path)

    db.session.delete(news)
    db.session.commit()

    return redirect("/admin/news")