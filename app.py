from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://afridrop:afridrop_pwd@localhost/afridrop_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Review(db.Model):
    """Representation of Review"""

    __tablename__ = 'reviews'
     
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(60), unique=True)
    product_id = db.Column(db.String(60), unique=True)
    rating = db.Column(db.Integer)
    comment = db.Column(db.String(1024))

with app.app_context():
    db.create_all()
    print("Database tables created successfully.")

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
