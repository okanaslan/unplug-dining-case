from src.endpoints.menu.get_menu import get_menu_handler


def test_answer():
    assert get_menu_handler(4) == 5
