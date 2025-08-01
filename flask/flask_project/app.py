from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    date = db.Column(db.String(20))
    time = db.Column(db.String(10))
    purpose = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create Table
with app.app_context():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def book_appointment():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        date = request.form["date"]
        time = request.form["time"]
        purpose = request.form["purpose"]

        new_appointment = Appointment(name=name, email=email, date=date, time=time, purpose=purpose)
        db.session.add(new_appointment)
        db.session.commit()

        return "Appointment booked successfully!"

    return render_template("appointment.html")


@app.route("/appointments")
def view_appointments():
    appointments = Appointment.query.all()
    return {
        a.id: {
            "name": a.name,
            "email": a.email,
            "date": a.date,
            "time": a.time,
            "purpose": a.purpose
        }
        for a in appointments
    }

if __name__ == "__main__":
    app.run(debug=True)
