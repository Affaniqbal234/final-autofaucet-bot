import asyncio
import sys
from contextlib import suppress
from core.page_helpers import safe_click, close_secondary_pages
from utils.output import print_success, print_error, print_info


async def login(page, email, password, login_url):
    async def balance():
        with suppress(Exception):
            print_info("DUTCHY Balance: " + await page.locator('xpath=//*[@id="dashboard-content"]/div[3]/div/div[1]/div[3]/div[4]/div/div/div[2]/div/div[1]/div[1]/div[2]/h4').inner_text(timeout=10000))
            print_info("Current Level: " + await page.locator('xpath=//*[@id="dashboard-content"]/div[3]/div/div[1]/div[3]/div[4]/div/div/div[1]/div/div[1]/div[1]/div[2]/h4').inner_text(timeout=3000))
            print_info("Progess to next level: " + await page.locator('xpath=//*[@id="dashboard-content"]/div[3]/div/div[1]/div[3]/div[3]/div/b/center').inner_text(timeout=3000))
    print_info("Logging in...")
    try:
        await page.goto(login_url, wait_until="domcontentloaded")
        await close_secondary_pages(page)
        await asyncio.sleep(10)
        
        with suppress(Exception):
            await page.wait_for_url("**/dashboard.php", timeout=5000)
            print_success("Already Logged in!")
            await balance()
            return
        
        await page.wait_for_selector('input[name="username"]', timeout=15000)
        await page.fill('input[name="username"]', email)
        await asyncio.sleep(1)
        await page.fill('input[name="password"]', password)
        await safe_click(page, 'button[name="login-btn"]', timeout=40000, captcha=True, output="Login submitted.")
        await asyncio.sleep(2)
        
        await page.wait_for_url("**/dashboard.php", timeout=35000)
        print_success("Login successful!")
        await balance()
        return
        
    except Exception:
        try:
            print_info("Network is slow, waiting longer...")
            await page.wait_for_url("**/dashboard.php", timeout=5000)
            print_success("Already logged in.")
            await balance()
            return
        except Exception:
            print_error("Login failed, stopping bot... please restart the bot.")
            await page.context.browser.close()
            sys.exit(1)
