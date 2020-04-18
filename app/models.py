from app import db

class Crimes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    severity = db.Column(db.Integer, unique=False, nullable=False)
    city = db.Column(db.Integer, unique=False, nullable=False)
    date = db.Column(db.String(120), unique=False, nullable=False)
    time = db.Column(db.String(120), unique=False, nullable=False)

    def __repr__(self):
        return 'Severity: {}; City: {}'.format(self.severity,self.city)

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    # Integer version of string names 
    postnr = db.Column(db.Integer, unique=False, nullable=False)
    kommune = db.Column(db.Integer, unique=False, nullable=False)

    # Coordinates
    latitude = db.Column(db.Float, unique=False, nullable=False)
    longitude = db.Column(db.Float, unique=False, nullable=False)
    
    

    def __repr__(self):
        return 'City:' + str(postnr)       

class MLresult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    def __repr__(self):
        return '<User %r>' % self.id