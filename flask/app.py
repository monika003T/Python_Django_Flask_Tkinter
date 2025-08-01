from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    message = db.Column(db.Text)


with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])  # Root URL will open the contact page
def contact():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        new_contact = Contact(name=name, email=email, message=message)
        db.session.add(new_contact)
        db.session.commit()

        return "Thank you! Your message has been submitted."

    return render_template("contact.html")

@app.route("/contacts")
def contacts():
    all_contacts = Contact.query.all()
    return {c.id: {"name": c.name, "email": c.email, "message": c.message} for c in all_contacts}

if __name__ == "__main__":
    app.run(debug=True)
