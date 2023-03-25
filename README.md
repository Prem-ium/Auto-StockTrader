# Auto Stock Trader

A repository containing scripts and projects for automating stock orders across multiple brokerages.


For a majority of these projects, on your browser of choice, you will need to download the [Selenium IDE browser extension.](https://github.com/SeleniumHQ/selenium-ide)  <a href="https://www.selenium.dev/selenium-ide/" target="_blank"
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
- Sofi Invest (Archived)

## Enviornmental Variables

To use this project, you will need to set the following environment variables in your .env file:

`CHASE_AI` = A stringified JSON array containing your Chase Investment AI numbers 
[found within the desktop stock order URL](https://user-images.githubusercontent.com/80719066/216079858-746af166-8387-41ad-9564-dd0c6285eb39.png), separated by commas.


`FIDELITY_AI` = A stringified JSON array containing your Fidelity Investment account numbers, separated by commas.

`ALLY_AI` = A stringified JSON array containing your Ally Investment account name + numbers, separated by commas.

   - In [Ally Invest Settings Webpage](https://live.invest.ally.com/settings), you will need to change the default orders on the settings for all accounts to be a small penny stock for default stock ticker to miminize risk, Market, & Quantity: 1.

`FIRSTRADE_AI` = A stringified JSON array containing your FirstTrade Investment account numbers, separated by commas.

`VANGUARD_AI` = A stringified JSON array containing your Vanguard Investment account numbers, separated by commas.

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
[Find more information here](https://github.com/Prem-ium/Auto-StockTrader/blob/main/src/X_Archive/README.MD)

## Donations
If you find my project helpful and would like to support its development, please consider making a donation. Every little bit helps and is greatly appreciated!

You can donate by clicking on the following button:

<a href="https://www.buymeacoffee.com/prem.ium" target="_blank"><img src="https://raw.githubusercontent.com/Prem-ium/youtube-analytics-bot/main/output-examples/media/coffee-logo.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

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
