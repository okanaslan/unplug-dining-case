from src.server import server
from src.database import db
from src.scripts.load_initial_data import loadInitialData

if __name__ == "__main__":
    db.init_app(server)
    with server.app_context():
        print("Creating Database")
        db.create_all()
        db.session.commit()
        db.session.close()
        print("Database Created")

        loadInitialData()

    server.run(debug=True)
