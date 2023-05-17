<h1 align="center">Auto Stock Trader </h1>

<p align="center">An <i>awesome</i> repository containing scripts and projects for automating stock orders across multiple brokerages.</p>

<p align="right"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/><img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white"/><img src="https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E"/></p>

For a majority of these projects, on your browser of choice, you will need to download the [Selenium IDE browser extension.](https://github.com/SeleniumHQ/selenium-ide) <a href="https://www.selenium.dev/selenium-ide/" target="_blank"
rel="noreferrer"> <img
src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg"
alt="selenium" width="40" height="40" /></a>

## Supported Brokerages
- Charles Schwab 
- Firstrade
- Vanguard
- Fidelity
- Chase / JP Morgan Invest
- Ally Invest
- Merrill Lynch
- Sofi Invest (Archived)

## Features
- Automate Pre-Market & Market Buy/Sell Orders 
- Multiple Tickers Automation in One Test (Split with ```,```)
- XPATH Error Checking Functions
- Quickstart using CLI

## Enviornmental Variables

To use this project, you will need to set the following environment variables in your .env file:

`SCHWAB_AI` = Total number of SCHWAB accounts.

`MERRILL_AI` = Total number of Merrill accounts.

`CHASE_AI` = A stringified JSON array containing your Chase Investment AI numbers 
[found within the desktop stock order URL](https://user-images.githubusercontent.com/80719066/216079858-746af166-8387-41ad-9564-dd0c6285eb39.png), separated by commas.

`FIDELITY_AI` = A stringified JSON array containing your Fidelity Investment account numbers, separated by commas.

`ALLY_AI` = A stringified JSON array containing your Ally Investment account name + numbers, separated by commas.

   - In [Ally Invest Settings Webpage](https://live.invest.ally.com/settings), you will need to change the default orders on the settings for all accounts to be a small penny stock for default stock ticker to miminize risk, Market, & Quantity: 1.

`FIRSTRADE_AI` = A stringified JSON array containing your FirstTrade Investment account numbers, separated by commas.

`VANGUARD_AI` = A stringified JSON array containing your Vanguard Investment account numbers, separated by commas. (Only for old Outdated Test Cases)

`CUSTOM_DIR` = Directory path updated .side files should be located. (Optional)

Example:

```bash
CHASE_AI="['1234567890','0987654321']";
ALLY_AI="['Individual-A123456789','Individual-B098765432']";
FIRSTRADE_AI="['111111','222222']";
VANGUARD_AI="['54554326','54678936']";
```
Refer to `.env.example` for more clarity. 

### Installation

Clone the repository & install dependencies:

```bash
git clone https://github.com/Prem-ium/Auto-StockTrader
cd Auto-StockTrader
pip install -r requirements.txt
```

Configure [Enviornmental Variables](https://github.com/Prem-ium/Auto-StockTrader#enviornmental-variables) and run the script.
```
  python main.py
```

Passing an argument will quickly update the stock orders in all .side projects.
```
  python main.py APPL
```
## Selenium IDE
Automating Chase, Fidelity, Firstrade, Schwab, Vanguard, & Ally Invest, run `main.py` after configurating your `.env`.

Once you've generated your .side projects, login to your brokerage accounts on your browser and utilize the [Selenium IDE browser extension](https://github.com/SeleniumHQ/selenium-ide) to open the `.side` projects generated & run your desired stock order automation(s).

For more assistance, refer to [archived README](https://github.com/Prem-ium/Auto-StockTrader/blob/main/src/X_Archive/README.MD)

# Archived Sofi Invest

Automating orders for Sofi Invest can be attempted through the now archived `sofi_main.py` Python script. 
Sofi is very unpredictable and unstable, and has been archived with no plans for further development.
You can still attempt to use it, however the chances of every order going through are slim as Sofi Invest has weird order landing pages that contain different requirements & order layout for different stock tickers.

You can also attempt to use 'Sofi Invest.side` to loop through your accounts and *manually* place orders. While not automated, it is a nice feature to have to help place orders on multiple accounts. Simpily replace the array with your account numbers, change 'Buy' or 'Sell' accordingly to get the correct order page.
[Find more information here](https://github.com/Prem-ium/Auto-StockTrader/blob/main/src/X_Archive/README.MD#sofi-invest-automation)

## Donations
I've been working on this project for a few months now, and I'm really happy with how it's turned out. It's also been a helpful tool for users to earn some extra money with Bing Rewards. I'm currently working on adding new features to the script and working on other similar programs to generate passive income. I'm also working on making the script more user-friendly and accessible to a wider audience.

I'm accepting donations through BuyMeCoffee or GitHub Sponsors. Any amount you can donate will be greatly appreciated.

<div style="display: grid; grid-template-columns: 1fr 1fr; justify-content: center; gap: 10px;">
    <div style="display: grid; justify-content: center;">
        <span>Buy Me a Coffee:</span>
        <a href="https://www.buymeacoffee.com/prem.ium" target="_blank">
            <img src="https://raw.githubusercontent.com/Prem-ium/youtube-analytics-bot/main/output-examples/media/coffee-logo.png" alt="Buy Me A Coffee" style="height: 41px !important; width: 174px !important; box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important; -webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;">
        </a>
    </div>
    <div style="display: grid; justify-content: center;">
        <span>GitHub Sponsors:</span>
        <a href="https://github.com/sponsors/Prem-ium" target="_blank">
            <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AAA" alt="GitHub Sponsor" style="height: 41px !important; width: 174px !important; box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important; -webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;">
        </a>
    </div>
</div>

Your donations will help me to cover the costs of hosting the project, developing new features, and marketing the project to a wider audience.
Thank you for your support!

# Disclaimer

⚠️ **DISCLAIMER:** _You're using these automation scripts at your own risk, I am not responsible for any financial or account loss or damage that may occur._

## Important Information

- This script is provided for informational purposes only and does not constitute financial or investment advice. The user is solely responsible for any investment decisions made based on the information provided by the script(s)/.side project/repository.

- The script is provided "as is" and without warranty of any kind, either express or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose.

- The user understands that the script's performance may be affected by factors beyond developer's control, such as market volatility, technical issues with the trading platform, internet connectivity issues, & more.

- The user agrees to indemnify and hold the developer(s) harmless from any and all claims, damages, or losses arising from their use of the script(s)/.side project/repository.

## Final Remarks

Thank you for your interest in this repository. 
Please consider leaving a :star2: if you found this project to be cool!
