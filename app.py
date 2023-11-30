from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://AfriDrop:afridrop@localhost/afridrop'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class SignIn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f"SignIn('{self.username}', '{self.email}')"

@app.route('/add_sign_in')
def add_sign_in():
    new_sign_in = SignIn(username='Mumbi', email='mumbi@example.com')
    db.session.add(new_sign_in)
    db.session.commit()
    return 'Sign-In added!'


if __name__ == '__main__':
    app.run(debug=True)
