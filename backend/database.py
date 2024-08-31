from models import db, Bed

def init_db():
    db.create_all()
    if Bed.query.count() == 0:
        for i in range(1, 21):
            db.session.add(Bed(available=True))
        db.session.commit()
