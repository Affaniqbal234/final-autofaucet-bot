from patchright.async_api import async_playwright


class BrowserManager:
    def __init__(self, user_data_dir, headless=False):
        self.user_data_dir = user_data_dir
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.page = None
    
    async def __aenter__(self):
        return await self.launch()
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()
    
    async def launch(self):
        self.playwright = await async_playwright().start()
        self.browser = await self.playwright.chromium.launch_persistent_context(
            user_data_dir=self.user_data_dir,
            channel="chrome",
            headless=self.headless,
            no_viewport=True,
        )
        self.page = await self.browser.new_page()
        return self.page
    
    async def close(self):
        if self.browser:
            await self.browser.close()
        if self.playwright:
            await self.playwright.stop()
