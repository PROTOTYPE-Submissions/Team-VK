from app import db

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    course = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Enrollment('{self.full_name}', '{self.email}', '{self.course}')"
