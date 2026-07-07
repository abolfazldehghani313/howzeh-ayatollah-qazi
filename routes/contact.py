from app import app
from models import db, Message
from flask import render_template, request, redirect, session


# صفحه تماس با ما
@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        new_message = Message(
            fullname=request.form["fullname"],
            phone=request.form["phone"],
            subject=request.form["subject"],
            text=request.form["text"]
        )

        db.session.add(new_message)
        db.session.commit()

        return render_template(
            "contact.html",
            success="پیام شما با موفقیت ارسال شد."
        )

    return render_template("contact.html")


# مدیریت پیام‌ها
@app.route("/admin/messages")
def admin_messages():

    if not session.get("admin"):
        return redirect("/login")

    messages = Message.query.order_by(Message.id.desc()).all()

    return render_template(
        "admin/messages.html",
        messages=messages
    )


# حذف پیام
@app.route("/admin/messages/delete/<int:id>")
def delete_message(id):

    if not session.get("admin"):
        return redirect("/login")

    message = Message.query.get_or_404(id)

    db.session.delete(message)
    db.session.commit()

    return redirect("/admin/messages")