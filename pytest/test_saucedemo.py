from playwright.sync_api import Page
import pytest

# pytest --headed --base-url https://www.saucedemo.com/

def test_title(page: Page):
    page.goto("")
    assert page.title() == "Swag Labs"


def test_inventaty_site(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."
