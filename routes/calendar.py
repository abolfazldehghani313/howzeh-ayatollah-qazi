from app import app
from models import db, Calendar
from flask import render_template, request, redirect, session


# نمایش تقویم در سایت
@app.route("/calendar")
def calendar():

    events = Calendar.query.order_by(Calendar.id.desc()).all()

    return render_template("calendar.html", events=events)


# مدیریت تقویم
@app.route("/admin/calendar", methods=["GET", "POST"])
def admin_calendar():

    # بررسی ورود مدیر
    if not session.get("admin"):
        return redirect("/login")

    if request.method == "POST":

        event = Calendar(
            title=request.form["title"],
            date=request.form["date"],
            time=request.form["time"],
            place=request.form["place"],
            description=request.form["description"]
        )

        db.session.add(event)
        db.session.commit()

        return redirect("/admin/calendar")

    events = Calendar.query.order_by(Calendar.id.desc()).all()

    return render_template(
        "admin/calendar.html",
        events=events
    )


# حذف برنامه
@app.route("/admin/calendar/delete/<int:id>")
def delete_calendar(id):

    # بررسی ورود مدیر
    if not session.get("admin"):
        return redirect("/login")

    event = Calendar.query.get_or_404(id)

    db.session.delete(event)
    db.session.commit()

    return redirect("/admin/calendar")