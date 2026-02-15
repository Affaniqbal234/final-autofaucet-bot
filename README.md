<p align="center">
    <img src="assets/logo.png"
    width="200" alt="FinalAutofaucetBotLogo">
    </p>

# Final Autofaucet BOT

Automated cryptocurrency faucet claiming bot for autofaucet.dutchycorp.space with Cloudflare Turnstile captcha solving.

**Version:** 1.0.0  
**GitHub:** [github.com/Affaniqbal234/final-autofaucet-bot](https://github.com/Affaniqbal234/final-autofaucet-bot)  
**Author:** Affan [@Affaniqbal234](https://github.com/Affaniqbal234)

## Features

- Automated login with email/password
- Cloudflare Turnstile captcha solver (built-in)
- Dutchy Roll faucet claiming
- Coin Roll faucet claiming
- PTC ads processing
- PTC Wall ads processing
- Persistent browser sessions (cookies saved)
- Clean terminal output with colors
- Optional headless mode (not recommended)

## Requirements

- Python 3.8 or higher
- Google Chrome browser installed
- Active account on [autofaucet.dutchycorp.space](https://autofaucet.dutchycorp.space)
- **Important:** Select Cloudflare Turnstile as the default captcha in your account settings first

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Affaniqbal234/final-autofaucet-bot.git
cd final-autofaucet-bot
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Install Chrome browser for Patchright (required for automation):
```bash
patchright install chrome
```

4. Create configuration file:
```bash
copy .env.example .env
```
(On Linux/Mac use: `cp .env.example .env`)

5. Edit the `.env` file with your credentials:
```env
EMAIL=your_email@example.com
PASSWORD=your_password
HEADLESS=false
```

## Configuration

Edit the `.env` file with the following settings:

- `EMAIL` - Your autofaucet.dutchycorp.space account email (required)
- `PASSWORD` - Your account password (required)
- `HEADLESS` - Run browser in headless mode (default: false)

### Headless Mode Warning

⚠️ **IMPORTANT:** Setting `HEADLESS=true` may significantly increase the risk of account ban. Websites can detect headless browsers and may flag them as bots. It's strongly recommended to keep `HEADLESS=false` for safer operation.

## Usage

Run the bot:
```bash
python main.py
```

The bot will automatically:
1. Display the banner with version info
2. Log in to your account
3. Handle cookie consent and UI elements
4. Claim Dutchy Roll faucet
5. Claim Coin Roll faucet
6. Process available PTC ads
7. Process PTC Wall ads
8. Display completion message

## Troubleshooting

### "ERROR: EMAIL is missing in .env"
- Ensure you created a `.env` file (not `.env.example`)
- Verify that `EMAIL` and `PASSWORD` are filled in correctly

### "patchright: command not found" or browser installation issues
- Make sure you installed patchright: `pip install patchright`
- Then install the browser: `patchright install chrome` or `patchright install chromium`
- If issues persist, try: `python -m patchright install chromium` or `python -m patchright install chrome`

### "Login failed"
- Verify your credentials are correct
- Ensure you selected Cloudflare Turnstile as default captcha in account settings
- Check your internet connection

### Browser doesn't close
- The bot should close automatically after completion
- If not, manually close Chrome - your session will be saved for next run

### Captcha not solving
- Make sure Cloudflare Turnstile is set as your default captcha type in account settings
- If issues persist, try running without headless mode

## Project Structure

```
final-autofaucet-bot/
├── main.py                 # Main entry point
├── config/
│   └── settings.py         # Configuration loader
├── core/
│   ├── browser.py          # Browser management
│   ├── captcha.py          # Captcha solving
│   └── page_helpers.py     # Page interaction utilities
├── modules/
│   ├── login.py            # Login functionality
│   ├── dutchy_roll.py      # Dutchy Roll claiming
│   ├── coin_roll.py        # Coin Roll claiming
│   ├── ptc.py              # PTC ads processing
│   └── ptc_wall.py         # PTC Wall processing
├── utils/
│   ├── output.py           # Terminal output formatting
│   └── state.py            # State management
├── .env                    # Your configuration (create from .env.example)
├── .env.example            # Example configuration
└── requirements.txt        # Python dependencies
```

## Disclaimer

This bot is provided for educational purposes. The author is not responsible for any misuse, violations of terms of service, or account bans. Use at your own risk and in accordance with the website's terms of service.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to:
- Report bugs by opening an issue
- Suggest new features
- Submit pull requests

## Support

If you found this project useful, please give it a ⭐ on GitHub!

For issues or questions, please open an issue on the [GitHub repository](https://github.com/Affaniqbal234/final-autofaucet-bot/issues).

