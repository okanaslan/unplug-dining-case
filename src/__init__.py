from server import app

# Create a flask server hosting at port 5000

# Configurations
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Import models
# from src.models.menu import Menu
# from src.models.menu_item import MenuItem

# Import routes
from endpoints.menu.create_menu import create_menu
from endpoints.menu.get_menu import get_menu
from endpoints.menu_item import update_menu_item


# Register routes
# app.register_blueprint(create_menu)
# app.register_blueprint(get_menu)
# app.register_blueprint(update_menu_item)


# Run Server
if __name__ == "__main__":
    app.run(debug=True)
