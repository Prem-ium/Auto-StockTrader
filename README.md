# Auto Stock Trader

A repository containing scripts and projects for automating stock orders across multiple brokerages.


For a majority of these projects, on your browser of choice, you will need to download the [Selenium IDE browser extension.](https://github.com/SeleniumHQ/selenium-ide)  <a href="https://www.selenium.dev/selenium-ide/" target="_blank"
rel="noreferrer"> <img
src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg"
alt="selenium" width="40" height="40" /></a>


## Quick-Start Enviornmental Variables {#Quick-ENV}

To use this project, you will need to set the following environment variables in your .env file:

`CHASE_AI` = A stringified JSON array containing your Chase Investment account numbers, separated by commas.

`FIDELITY_AI` = A stringified JSON array containing your Fidelity Investment account numbers, separated by commas.

`ALLY_AI` = A stringified JSON array containing your Ally Investment account numbers, separated by commas.

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
### Sofi Environment Variables

To run this project, you will need to add the following environment variables to your .env file:

`ACCOUNT_NAMES` = A string of names of investment accounts, separated by commas.

`SOFI_LOGIN` = Login credentials of SOFI, separated by ':'

`EXCLUDE_ACCOUNTS` = Remove accounts in ACCOUNT_NAMES for testing, debugging, or excluding the purchase of the stock from the account. Separated by commas.

### Installation

Clone the repository & install dependencies:

```bash
git clone https://github.com/Prem-ium/Auto-StockTrader
cd Auto-StockTrader
pip install -r requirements.txt
```
Check [Running_Sofi](#Running_Sofi) for sofi instructions, otherwise, continue for Quick-Start.

Configure [Quick Start Enviornmental Variables](#Quick-ENV) and run the script.
```
  python quickstart-ide.py
```

Passing an argument will quickly update the stock orders in all .side projects.
```
  python quickstart-ide.py APPL
```


# Chase Automation

Automating orders for Chase JPMorgan Brokerage can be done using the `Chase_Auto.side` file & Selenium IDE Extension.


1. Download the Selenium IDE Extension from your browser's extension store and open the `Chase_Auto.side` project file
2. Log in to your brokerage account on your browser.
3. Retrieve your AI within the URL of the Chase Trade Stock webpage for Each Account. Go through each account on the account dropdown and save the AI number in the URL. 
   (Retrieve the number at {YOUR_AI_HERE}): `https://secure07ea.chase.com/web/auth/dashboard#/dashboard/trade/equity/entry;ai={YOUR_AI_HERE};sym=`)
   
   ![image](https://user-images.githubusercontent.com/80719066/216079858-746af166-8387-41ad-9564-dd0c6285eb39.png)

4. Copy the AI for each account and replace the return statement on all test cases (Buy/Sell Test in Selenium IDE) returning the list:
   `return ['54658965', 'YOUR', 'AI', 'GOES', 'HERE']`
5. Input the Stock Ticker as a return statement and click the start button to start automating.
   `return "STOCK_TICKER"`

# Vanguard, Firstrade, Fidelity, & Ally Automation
Open the `Vanguard_Auto.side` , `Firstrade_Auto.side`, `Fidelity_Auto.side`, or `Ally_Auto.side` file within the Selenium IDE Extension in the broser of your choice. 

In [Ally Invest Settings Webpage](https://live.invest.ally.com/settings), you will need to change the default orders on the settings for all accounts to be a small penny stock for default stock ticker to miminize risk, Market, & Quantity: 1.

Automating orders for Firstrade Brokerage can be done using the `Ally.side` file & Selenium IDE Extension. You will need to change the default orders on the settings for all accounts to be a small penny stock for default stock ticker to miminize risk, Market, & Quantity: 1.

1. Download the Selenium IDE Extension from your browser's extension store and open the `Vanguard_Automation.side` project file
2. Log in to Vanguard, Firstrade, or Ally on your browser.
3. Retrieve the list of your account number(s) and place them in the return execute script on the buy and sell test(s). 
`return ["54566343", "34546546", "54566546"]`

4. Enter the Stock Ticker (Change Target/TICKERHERE)
![image](https://user-images.githubusercontent.com/80719066/216331460-00897c0e-1e21-4413-ac81-1931fe906de0.png)

5. Input the Limit Price (if applicable) in the LIMIT_PRICE variable.
5. Start the Test to begin the automation. 

# Schwab Automation

Automating orders for Schwab Brokerage can be done using the `Schwab.side` file & Selenium IDE Extension.

### Schwab Set-Up

1. Download the Selenium IDE Extension from your browser's extension store and open the `Schwab.side` project file
2. Log in to your brokerage account on your browser.
3. Adjust the array of numbers depending on how many accounts you have. (n-1)
4. Input the Stock Ticker in the desired test (Schwab_Buy or Schwab_Sell) and start the test.

# Sofi Invest Automation

Automating orders for Sofi Invest can be done through the `sofi_main.py` Python script.

### Running Sofi {#Running_Sofi}

Specifiy commands in the following order within a terminal:

1. Whether to 'buy' or 'sell'
2. Stock Ticker's symbol
3. (Optional) 'slow' if you wish to pass in a sleep timer
4. sleep timer value

```bash
  python sofi_main.py buy APPL
```
or, to wait 30 seconds in-between each account
```bash
  python sofi_main.py buy APPL 100.54 slow 30
```
or, to place limit (on certain stocks)
```bash
  python sofi_main.py buy GNUS 0.50 slow 30
```
## Donations
If you find my project helpful and would like to support its development, please consider making a donation. Every little bit helps and is greatly appreciated!

You can donate by clicking on the following button:

<a href="https://www.buymeacoffee.com/prem.ium" target="_blank"><img src="https://raw.githubusercontent.com/Prem-ium/youtube-analytics-bot/main/output-examples/media/coffee-logo.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

# Disclaimer

⚠️ **DISCLAIMER:** _You're using these automation scripts at your own risk, I am not responsible for any financial or account loss or damage that may occur._

## Important Information

- This script is provided for informational purposes only and does not constitute financial or investment advice. The user is solely responsible for any investment decisions made based on the information provided by the script.

- The script is provided "as is" and without warranty of any kind, either express or implied, including but not limited to the implied warranties of merchantability and fitness for a particular purpose.

- The user understands that the script's performance may be affected by factors beyond developer's control, such as market volatility, technical issues with the trading platform, internet connectivity issues, & more.

- The user agrees to indemnify and hold the developer(s) harmless from any and all claims, damages, or losses arising from their use of the script.

Thank you for your support!
