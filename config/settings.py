import os
import sys
from dotenv import load_dotenv


class Config:
    EMAIL = None
    PASSWORD = None
    HEADLESS = False
    
    LOGIN_URL = "https://autofaucet.dutchycorp.space/login.php"
    ROLL_GAME_URL = "https://autofaucet.dutchycorp.space/roll_game.php"
    COIN_ROLL_URL = "https://autofaucet.dutchycorp.space/coin_roll.php"
    PTC_URL = "https://autofaucet.dutchycorp.space/ptc/"
    PTC_WALL_URL = "https://autofaucet.dutchycorp.space/ptc/wall.php"
    
    UNLOCK_SELECTOR = '//*[@id="unlockbutton"]'
    CLAIM_SELECTOR = '//*[@id="claim_boosted"]'
    AD_VIDEO_BUTTON = '//*[@id="ad_video"]/button'
    
    USER_DATA_DIR = "UserDataPersistantCookies"
    STATE_FILE = None
    
    @classmethod
    def load(cls):
        load_dotenv()
        
        config = cls()
        config.EMAIL = os.getenv("EMAIL", "").strip()
        config.PASSWORD = os.getenv("PASSWORD", "").strip()
        headless_str = os.getenv("HEADLESS", "false").strip().lower()
        config.HEADLESS = headless_str in ("true", "1", "yes")
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        config.STATE_FILE = os.path.join(project_root, config.USER_DATA_DIR, "run_once.json")
        
        if not config.EMAIL:
            print("ERROR: EMAIL is missing in .env")
            print("Fix: copy .env.example to .env and set EMAIL=your_email")
            sys.exit(1)
        
        if not config.PASSWORD:
            print("ERROR: PASSWORD is missing in .env")
            print("Fix: copy .env.example to .env and set PASSWORD=your_password")
            sys.exit(1)
        
        if config.HEADLESS:
            print("\n⚠️  WARNING: Headless mode is ENABLED!")
            print("⚠️  This may increase the risk of account ban.")
            print("⚠️  It's recommended to run with HEADLESS=false for safer operation.\n")
        
        return config
