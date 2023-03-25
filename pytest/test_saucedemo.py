from playwright.sync_api import Page
import pytest

# pytest --headed --base-url https://www.saucedemo.com
# pytest --headed --base-url https://www.saucedemo.com --browser firefox

# ZAINSTALOWANE PRZEGLADARKI
# pytest --headed --base-url https://www.saucedemo.com --browser-channel chrome


# PS C:\GIT\playwrite_demo1> pytest --headed --base-url https://www.saucedemo.com --tracing on    
# PS C:\GIT\playwrite_demo1> pytest --headed --base-url https://www.saucedemo.com --tracing retain-on-failure
# playwright show-trace .\test-results\pytest-test-saucedemo-py-test-inventaty-site-chromium\trace.zip

# pytest może brać parametry z pytest.ini


# @pytest.mark.only_browser("firefox")
def test_title(page: Page):
    page.goto("/")
    assert page.title() == "Swag Labs"


# @pytest.mark.skip_browser("firefox")
def test_inventaty_site(page: Page):
    page.goto("/inventory.html")
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in."
