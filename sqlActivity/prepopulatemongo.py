from app import app, mongo

def preload_race_results():
    """Preload MongoDB with race results."""
    with app.app_context():
        # ✅ Fix: Explicitly check if mongo.db is not None
        if mongo.db is not None and mongo.db.race_results.count_documents({}) == 0:
            race_results = [
                {"race": "Bahrain Grand Prix", "year": 2025, "winner": "Max Verstappen", "team": "Red Bull"},
                {"race": "Saudi Arabian Grand Prix", "year": 2025, "winner": "Max Verstappen", "team": "Red Bull"},
                {"race": "Australian Grand Prix", "year": 2025, "winner": "Fernando Alonso", "team": "Aston Martin"},
                {"race": "Monaco Grand Prix", "year": 2025, "winner": "Charles Leclerc", "team": "Ferrari"},
                {"race": "British Grand Prix", "year": 2025, "winner": "Lando Norris", "team": "McLaren"},
                {"race": "Italian Grand Prix", "year": 2025, "winner": "Carlos Sainz", "team": "Williams"},
                {"race": "Singapore Grand Prix", "year": 2025, "winner": "Lando Norris", "team": "McLaren"},
            ]

            mongo.db.race_results.insert_many(race_results)
            print(f"✅ Inserted {len(race_results)} race results into MongoDB.")
        else:
            existing_count = mongo.db.race_results.count_documents({})
            print(f"⚠️ MongoDB already contains {existing_count} race results. No new data added.")

        # Log actual stored data for verification
        stored_data = list(mongo.db.race_results.find({}, {"_id": 0}))  # Get all records without _id
        print("📜 Current MongoDB race results:", stored_data)

if __name__ == "__main__":
    with app.app_context():
        preload_race_results()