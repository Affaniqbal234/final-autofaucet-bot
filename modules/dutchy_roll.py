import asyncio
from contextlib import suppress
from core.captcha import solve_turnstile
from core.page_helpers import safe_click, close_secondary_pages, set_main_page
from utils.output import print_success, print_error, print_info


async def dutchy_roll(page, roll_game_url, unlock_selector, claim_selector, ad_video_button):
    try:
        await page.goto(roll_game_url, wait_until="domcontentloaded")
        await asyncio.sleep(2)
        await close_secondary_pages(page)
        print_success(f"Moved to DUTCHY ROLL: {roll_game_url}")
        
        await page.locator(unlock_selector).wait_for(state="visible", timeout=30000)
        await page.locator(unlock_selector).scroll_into_view_if_needed()
        await solve_turnstile(page)
        await page.locator(unlock_selector).click(force=True)
        print_success("[DUTCHY ROLL] Unlocked Boosted Roll.")
        await asyncio.sleep(3)
        
        if len(page.context.pages) > 1:
            page = await set_main_page(page, roll_game_url)
            await close_secondary_pages(page)
            await asyncio.sleep(3)
            await page.locator(unlock_selector).click(force=True)
            print_success("[DUTCHY ROLL] Unlocked Boosted Roll.")
            await asyncio.sleep(3)
        
        with suppress(Exception):
            await safe_click(page, ad_video_button, timeout=10000, output="[DUTCHY ROLL] Closed AD_Video.")
            await asyncio.sleep(2)
        
        page = await set_main_page(page, roll_game_url)
        await close_secondary_pages(page)
        await asyncio.sleep(10)
        
        await safe_click(page, claim_selector, timeout=30000, output="[DUTCHY ROLL] Successfully claimed.")
        await close_secondary_pages(page)
        await asyncio.sleep(2)
        with suppress(Exception):
            print_info(await page.locator('xpath=/html/body/div[4]/div[10]/div[2]/div[2]/div[2]').text_content(timeout=12000))
        return page
        
    except Exception as e:
        print_error(f"[DUTCHY ROLL] ERROR: {e}")
        return page
