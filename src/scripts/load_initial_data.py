import json
from models.menu import Menu
from models.menu_item import MenuItem


def loadInitialData():
    jsonData = json.load(open("src/scripts/sample_data.json"))
    menuList = jsonData["menu_group_map"]
    menuItemList = jsonData["menu_item_map"]
    menu_group_menu_item_lookup = jsonData["menu_group_menu_item_lookup"]

    for menuId in menuList:
        menu = menuList[menuId]
        isExisting = Menu.query.filter_by(restaurant_id=int(menu["id"])).first()
        if isExisting:
            continue
        menuObj = Menu(int(menu["id"]), menu["name"])
        menuObj.save()

    for menuItemId in menuItemList:
        menuItem = menuItemList[menuItemId]
        isExisting = MenuItem.query.filter_by(id=int(menuItem["id"])).first()
        if isExisting:
            continue
        menuItemObj = MenuItem(
            int(menuItem["id"]),
            menuItem["name"],
            menuItem["stock_status"],
            menuItem["image"],
            float(menuItem["price"]),
            menuItem["description"],
            int(menuItem["ranking"]) if menuItem["ranking"] else None,
            int(menuItem["calorie"]) if menuItem["calorie"] else None,
            int(menuItem["restaurant_id"]) if menuItem["restaurant_id"] else None,
        )
        menuItemObj.save()

    for menuId in menu_group_menu_item_lookup:
        menuItemIds = menu_group_menu_item_lookup[menuId]
        menu = Menu.query.filter_by(restaurant_id=int(menuId)).first()
        if not menu:
            continue
        for menuItemId in menuItemIds:
            menuItem = MenuItem.query.filter_by(id=int(menuItemId)).first()
            if not menuItem:
                continue
            menu.menu_items.append(menuItem)
            menu.save()

    print("Loaded sample data successfully")
