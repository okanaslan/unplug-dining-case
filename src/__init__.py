from server import server
from database import db

if __name__ == "__main__":
    db.init_app(server)
    with server.app_context():
        print("Creating Database")
        db.create_all()
        db.session.commit()
        db.session.close()
        print("Database Created")
        # loadInitialData()
        
    server.run(debug=True)
