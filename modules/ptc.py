import asyncio
from contextlib import suppress
from core.captcha import solve_turnstile
from core.page_helpers import wait_submit_up_to, close_secondary_pages
from utils.output import print_success, print_error, print_info


async def process_ptc_list(page, ptc_url):
    try:
        await page.goto(ptc_url, wait_until="domcontentloaded")
        print_success(f"Moved to PTC: {ptc_url}")
        
        count = 0
        
        while True:
            with suppress(Exception):
                locator1 = page.locator("xpath=/html/body/div[4]/div[1]/div[2]/div[1]/div[1]/center/h4")
                await locator1.wait_for(state="visible", timeout=5000)
                text1 = await locator1.inner_text()
                if "All Available Ads Watched" in text1:
                    print_success("[PTC] All Available Ads Watched.")
                    return
            
            print_info("[PTC] Waiting for Submit button to appear under 45 seconds")
            btn = await wait_submit_up_to(page, 45000)
            
            if not btn:
                print_success("[PTC] All DONE")
                return
            
            await asyncio.sleep(10)
            await btn.scroll_into_view_if_needed()
            await solve_turnstile(page)
            await btn.click()
            print_success("[PTC] Submit Clicked")
            await asyncio.sleep(2)
            await close_secondary_pages(page)
            
            await asyncio.sleep(2)
            if page.url.endswith("?invalid_captcha"):
                print_error("[PTC] Invalid captcha detected, reloading PTC page...")
                await page.goto(ptc_url, wait_until="domcontentloaded")
                await asyncio.sleep(15)
                continue
            
            count += 1
            print_success(f"[PTC] Ad {count} done")
            with suppress(Exception):
                print_info(await page.locator('xpath=/html/body/div[4]/nav/div/div/div/div[1]/p').inner_text(timeout=8000))
            await asyncio.sleep(2)
        
    except Exception as e:
        print_error(f"[PTC] ERROR: {e}")
