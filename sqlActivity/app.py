import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect
from flask_pymongo import PyMongo

app = Flask(__name__)

# Store the database inside the project directory (sqlExample/database.db)
db_folder = os.path.join(os.getcwd(), "database")
db_path = os.path.join(db_folder, "database.db")

# Ensure the database directory exists
os.makedirs(db_folder, exist_ok=True)

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["MONGO_URI"] = "mongodb+srv://catriona:web@Cluster0.mongodb.net/f1db?retryWrites=true&w=majority"
mongo = PyMongo(app)

db = SQLAlchemy(app)

class Driver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    team = db.Column(db.String(100), nullable=False)

def create_tables():
    with app.app_context():
        db.create_all()
        print(f"✅ Database created at {db_path}")

# Ensure the tables are created before starting Flask
create_tables()


@app.route('/add', methods=['POST'])
def add_driver():
    name = request.form['name']
    team = request.form['team']
    new_driver = Driver(name=name, team=team)
    db.session.add(new_driver)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>', methods=['POST'])
def delete_driver(id):
    driver = Driver.query.get(id)
    db.session.delete(driver)
    db.session.commit()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['POST'])
def edit_driver(id):
    driver = Driver.query.get(id)
    driver.name = request.form['name']
    driver.team = request.form['team']
    db.session.commit()
    return redirect('/')

@app.route('/')   
def index():
    drivers = Driver.query.all()  # Fetch all drivers from SQLite
    return render_template('index.html', drivers=drivers)

def home():
    return "Welcome to the F1 Team Management System!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
