import asyncio
import time
from contextlib import suppress
from core.captcha import solve_turnstile
from utils.output import print_success


async def safe_click(page, selector, timeout=20000, captcha=False, output="Button Clicked"):
    await page.locator(selector).wait_for(state="visible", timeout=timeout)
    await page.locator(selector).scroll_into_view_if_needed()
    
    if captcha:
        await solve_turnstile(page)
    
    await page.locator(selector).click()
    await asyncio.sleep(3)
    
    if await page.locator(selector).is_visible():
        await page.locator(selector).click(force=True)
        print_success(f"{output} (Forced)")
    else:
        print_success(output)


async def close_secondary_pages(page):
    try:
        ctx = page.context
        for pge in list(ctx.pages):
            if pge != page:
                with suppress(Exception):
                    await pge.close()
    except Exception:
        pass


async def set_main_page(page, expected_url):
    ctx = page.context
    await asyncio.sleep(2)
    
    for p in ctx.pages:
        try:
            if expected_url in p.url:
                return p
        except Exception:
            continue
    
    return page


async def first_visible_submit(page):
    selectors = [
        'button:has-text("Submit")',
        'button[data-action="submit"]',
        'xpath=//button[contains(text(), "Submit")]',
    ]
    
    for sel in selectors:
        with suppress(Exception):
            h = await page.query_selector(sel)
            if h and await h.is_visible():
                return h
    
    return None


async def wait_submit_up_to(page, timeout_ms=45000):
    end_time = time.time() + (timeout_ms / 1000.0)
    
    while time.time() < end_time:
        btn = await first_visible_submit(page)
        if btn:
            return btn
        await asyncio.sleep(0.3)
    
    return None
