import asyncio
import time
from contextlib import suppress
from core.captcha import solve_turnstile
from core.page_helpers import wait_submit_up_to, close_secondary_pages
from utils.output import print_success, print_error, print_info


async def process_ptc_wall(page, ptc_wall_url):
    try:
        total = 0
        await page.goto(ptc_wall_url, wait_until="domcontentloaded")
        print_success(f"Moved to PTC_WALL: {ptc_wall_url}")
        
        visit_sel_css = '#ptc-container > div:nth-child(1) > div > div:nth-child(4) > a'
        visit_sel_xpath = '//*[@id="ptc-container"]/div[1]/div/div[3]/a'
        
        while True:
            end_time = time.time() + 60.0
            handle = None
            
            while time.time() < end_time and handle is None:
                with suppress(Exception):
                    h = await page.query_selector(visit_sel_css)
                    if h and await h.is_visible():
                        handle = h
                        break
                
                with suppress(Exception):
                    h = await page.query_selector(f'xpath={visit_sel_xpath}')
                    if h and await h.is_visible():
                        handle = h
                        break
                
                await asyncio.sleep(0.3)
            
            if handle is None:
                if not page.url.endswith('/ptc/wall.php'):
                    await page.goto(ptc_wall_url, wait_until="domcontentloaded")
                    print_info("[PTC_WALL] Reloading PTC_WALL page...")
                else:
                    print_success("[PTC_WALL] All DONE")
                    break
            
            with suppress(Exception):
                locator2 = page.locator("xpath=//*[@id='ptc-container']/p")
                await locator2.wait_for(state="visible", timeout=5000)
                text2 = await locator2.inner_text()
                if "All Internal PTC ads completed." in text2:
                    print_success("[PTC_WALL] All Internal PTC ads completed.")
                    return
            
            if handle:
                await handle.scroll_into_view_if_needed()
                await handle.click()
                await asyncio.sleep(2)
                await close_secondary_pages(page)
                
                print_info("[PTC_WALL] Waiting for Submit button.")
                submit_btn = await wait_submit_up_to(page, 60000)
                
                if submit_btn:
                    await asyncio.sleep(13)
                    await submit_btn.scroll_into_view_if_needed()
                    await solve_turnstile(page)
                    await submit_btn.click()
                    print_success("[PTC_WALL] Submit clicked")
                    await asyncio.sleep(2)
                    await close_secondary_pages(page)
                    
                    total += 1
                    print_success(f"[PTC_WALL] Ad {total} done")
                    with suppress(Exception):
                        print_info(await page.locator('xpath=/html/body/div[4]/div[9]/div[2]/center[3]/div[2]').inner_text(timeout=8000))
                else:
                    print_error("[PTC_WALL] No submit button found")
                
                with suppress(Exception):
                    if not page.url.endswith('/ptc/wall.php'):
                        await page.goto(ptc_wall_url, wait_until="domcontentloaded")
                        print_info("[PTC_WALL] Reloading PTC_WALL page...")
        
    except Exception as e:
        print_error(f"[PTC_WALL] ERROR: {e}")
