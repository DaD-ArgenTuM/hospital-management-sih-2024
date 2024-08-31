from flask import Flask, render_template, request, redirect, url_for
from models import db, Patient, Bed, Medicine, Appointment
from database import init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hospital.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/opd_booking.html', methods=['GET', 'POST'])
def opd_booking():
    if request.method == 'POST':
        name = request.form['name']
        symptoms = request.form['symptoms']
        appointment = Appointment(name=name, symptoms=symptoms)
        db.session.add(appointment)
        db.session.commit()
        return redirect(url_for('opd_booking.html'))
    appointments = Appointment.query.all()
    return render_template('opd_booking.html', appointments=appointments)

@app.route('/bed_availability.html')
def bed_availability():
    #beds = Bed.query.all()
    beds = [
        {'id': 1, 'available': True},
        {'id': 2, 'available': False},
        {'id': 3, 'available': True},
    ]
    return render_template('bed_availability.html', beds=beds)

@app.route('/patient_admission.html', methods=['GET', 'POST'])
def patient_admission():
    if request.method == 'POST':
        name = request.form['name']
        bed_id = request.form['bed_id']
        patient = Patient(name=name, bed_id=bed_id)
        db.session.add(patient)
        db.session.commit()
        bed = Bed.query.get(bed_id)
        bed.available = False
        db.session.commit()
        return redirect(url_for('patient_admission.html'))
    beds = Bed.query.filter_by(available=True).all()
    return render_template('patient_admission.html', beds=beds)

@app.route('/inventory.html', methods=['GET', 'POST'])
def inventory():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form['quantity']
        medicine = Medicine(name=name, quantity=quantity)
        db.session.add(medicine)
        db.session.commit()
        return redirect(url_for('inventory.html'))
    medicines = Medicine.query.all()
    return render_template('inventory.html', medicines=medicines)

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)
