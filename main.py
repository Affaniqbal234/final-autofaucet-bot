import asyncio
from contextlib import suppress

from core.browser import BrowserManager
from config.settings import Config
from utils.state import StateManager
from utils.output import print_banner, print_success, print_section, print_error, print_info
from modules.login import login
from modules.dutchy_roll import dutchy_roll
from modules.coin_roll import coin_roll
from modules.ptc import process_ptc_list
from modules.ptc_wall import process_ptc_wall
from core.page_helpers import safe_click


async def main():
    print_banner()
    
    config = Config.load()
    state = StateManager(config.STATE_FILE)
    
    async with BrowserManager(config.USER_DATA_DIR, config.HEADLESS) as page:
        print_section("LOGIN")
        await login(page, config.EMAIL, config.PASSWORD, config.LOGIN_URL)
        
        # Handle one-time UI actions
        if not state.get("accept_btn_done", False):
            try:
                print_success("Waiting for Cookies Button to Accept")
                await safe_click(page, '//*[@id="accept-btn"]', timeout=60000, output="Agree Button Clicked")
                state.set("accept_btn_done", True)
            except Exception as e:
                print_error(f"AGREE Cookies button not found: {e}")
        
        if not state.get("minimize_chat", False):
            try:
                await safe_click(page, '.chatbro_minimize_button', timeout=20000, output="Minimized Chat")
                state.set("minimize_chat", True)
            except Exception as e:
                print_error(f"Minimized Chat button not found: {e}")

        locator = page.locator('xpath=//*[@id="dashboard-content"]/div[3]/div/div[4]/div[5]/div[1]/div/a[11]/div[2]/div[1]/span[2]')
        try:
            text = await locator.text_content(timeout=2000)
        except:
            text = ""
        if (text or "").strip() == "Ready!":
            print_section("DUTCHY ROLL")
            page = await dutchy_roll(page, config.ROLL_GAME_URL,config.UNLOCK_SELECTOR,
                                    config.CLAIM_SELECTOR, config.AD_VIDEO_BUTTON)
            print_section("COIN ROLL")
            page = await coin_roll(page, config.COIN_ROLL_URL, config.UNLOCK_SELECTOR, 
                                    config.CLAIM_SELECTOR, config.AD_VIDEO_BUTTON)
        else:
            print_error("Rolls Not Ready, Moving to PTC ADS...")
        print_section("PTC ADS")
        await process_ptc_list(page, config.PTC_URL)
        
        print_section("PTC WALL")
        await process_ptc_wall(page, config.PTC_WALL_URL)
        
        print_section("COMPLETE")
        print_success("BOT successfully executed.")


if __name__ == "__main__":
    asyncio.run(main())
