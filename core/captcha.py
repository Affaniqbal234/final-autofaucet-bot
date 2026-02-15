import asyncio
from contextlib import suppress
from utils.output import print_success, print_error, print_info


async def solve_turnstile(page, attempts=3, timeout=20000):
    iframe = page.locator("iframe[src*='challenges.cloudflare.com']")
    
    try:
        await iframe.wait_for(state="visible", timeout=30000)
        print_success("CAPTCHA BOX Found.")
    except Exception:
        print_error("CAPTCHA BOX not found.")
        return False
    
    for attempt in range(1, attempts + 1):
        try:
            await page.wait_for_function(
                """() => {
                    const token = document.querySelector('input[name="cf-turnstile-response"]');
                    return token && token.value && token.value.length > 20;
                }""",
                timeout=timeout
            )
            print_success("Captcha Success")
            return True
        except Exception:
            print_info(f"CAPTCHA retrying... Attempt: {attempt}")
            
            with suppress(Exception):
                close_btn = page.locator('//*[@id="fr-close"]')
                if await close_btn.is_visible(timeout=2000):
                    await close_btn.click()
                    print_info("Closed Captcha Feedback about Error.")
            
            box = await iframe.bounding_box()
            if box:
                await page.mouse.click(
                    box["x"] + box["width"] / 2,
                    box["y"] + box["height"] / 2
                )
                await asyncio.sleep(2)
                with suppress(Exception):
                    ctx = page.context
                    for pge in list(ctx.pages):
                        if pge != page:
                            await pge.close()
    
    try:
        await page.wait_for_function(
            """() => {
                const token = document.querySelector('input[name="cf-turnstile-response"]');
                return token && token.value && token.value.length > 20;
            }""",
            timeout=timeout
        )
        print_success("Captcha Success")
        return True
    except Exception:
        print_error(f"CAPTCHA failed after {attempts} attempts.")
        return False
