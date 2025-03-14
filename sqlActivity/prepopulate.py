from app import app, db, Driver

def preload_drivers():
    """Preload the database with the 2025 F1 driver roster if empty."""
    with app.app_context():  # ✅ Ensure the database operations run inside an app context
        if Driver.query.count() == 0:  # Check if the database is empty
            drivers = [
                Driver(name="Pierre Gasly", team="Alpine"),
                Driver(name="Jack Doohan", team="Alpine"),
                Driver(name="Fernando Alonso", team="Aston Martin"),
                Driver(name="Lance Stroll", team="Aston Martin"),
                Driver(name="Charles Leclerc", team="Ferrari"),
                Driver(name="Lewis Hamilton", team="Ferrari"),
                Driver(name="Oliver Bearman", team="Haas"),
                Driver(name="Esteban Ocon", team="Haas"),
                Driver(name="Oscar Piastri", team="McLaren"),
                Driver(name="Lando Norris", team="McLaren"),
                Driver(name="George Russell", team="Mercedes"),
                Driver(name="Andrea Kimi Antonelli", team="Mercedes"),
                Driver(name="Max Verstappen", team="Red Bull"),
                Driver(name="Liam Lawson", team="Red Bull"),
                Driver(name="Yuki Tsunoda", team="Racing Bulls"),
                Driver(name="Isack Hadjar", team="Racing Bulls"),
                Driver(name="Nico Hülkenberg", team="Sauber"),
                Driver(name="Gabriel Bortoleto", team="Sauber"),
                Driver(name="Alex Albon", team="Williams"),
                Driver(name="Carlos Sainz", team="Williams"),
            ]

            db.session.bulk_save_objects(drivers)
            db.session.commit()
            print("✅ Preloaded the database with F1 drivers.")
        else:
            print("⚠️ Database already contains data. No changes made.")

if __name__ == "__main__":
    with app.app_context(): 
        db.create_all()
        preload_drivers()