-- add menu table
CREATE TABLE menu (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price INTEGER NOT NULL,
    description VARCHAR(255) NOT NULL,
    image VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL
);

-- add menu item table
CREATE TABLE menu_item (
    id SERIAL PRIMARY KEY,
    menu_id INTEGER REFERENCES menu(id),
    name VARCHAR(255) NOT NULL,
    price INTEGER NOT NULL,
    description VARCHAR(255) NOT NULL,
    image VARCHAR(255) NOT NULL,
    category VARCHAR(255) NOT NULL
);