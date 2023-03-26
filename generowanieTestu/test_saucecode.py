from playwright.sync_api import Page, expect

# GENEROWANIE KODU
# PS C:\GIT\playwrite_demo1\generowanieTestu> playwright codegen saucedemo.com
# URUCHOMIENIE TESTU
# pytest .\saucecode_demo.py

# consola w chromium, gdy jest włączony inspector
# playwright.$('input')
# playwright.$$('input')

# nawigacja do elementu 
# playwright.inspect('input')

def test_example(page: Page) -> None:
    page.goto("https://www.saucedemo.com/")


    # page.pause()

    page.locator("[data-test=\"username\"]").fill("standard_user")

    page.locator("[data-test=\"password\"]").fill("secret_sauce")

    page.locator("[data-test=\"login-button\"]").click()


    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
