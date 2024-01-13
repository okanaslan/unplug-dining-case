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
        print(menu)
        menuObj = Menu(int(menu["id"]), menu["name"])
        menuObj.save()
