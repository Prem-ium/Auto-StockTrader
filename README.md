# Auto Stock Trader

A repository containing scripts and projects for automating stock orders across multiple brokerages.

# Chase Automation

Automating orders for Chase JPMorgan Brokerage can be done using the `ChaseAutoInvest.side` file & Selenium IDE Extension.

### Chase Set-Up

1. Download the Selenium IDE Extension from your browser's extension store and open the `ChaseAutoInvest.side` project file
2. Log in to your brokerage account on your browser.
3. Retrieve your AI within the URL of the trade stock webpage for each account. 
   (Example: `https://secure07ea.chase.com/web/auth/dashboard#/dashboard/trade/equity/entry;ai={YOUR_AI_HERE};sym=`)
4. Copy the AI for each account and replace the return statement on all test cases (Buy/Sell Test in Selenium IDE) returning the list:
   `return ['54658965', 'YOUR', 'AI', 'GOES', 'HERE']`
5. Input the Stock Ticker as a return statement and click the start button to start automating.
   `return "STOCK_TICKER"`

# Schwab Automation

Automating orders for Schwab Brokerage can be done using the `Schwab.side` file & Selenium IDE Extension.

### Schwab Set-Up

1. Download the Selenium IDE Extension from your browser's extension store and open the `Schwab.side` project file
2. Log in to your brokerage account on your browser.
3. Adjust the array of numbers depending on how many accounts you have. (n-1)
4. Input the Stock Ticker in the desired test (Schwab_Buy or Schwab_Sell) and start the test.

# Sofi Invest Automation

Automating orders for Sofi Invest can be done through the `sofi_main.py` Python script.

### Sofi Environment Variables

To run this project, you will need to add the following environment variables to your .env file:

`ACCOUNT_NAMES` = A string of names of investment accounts, separated by commas.

`SOFI_LOGIN` = Login credentials of SOFI, separated by ':'

`EXCLUDE_ACCOUNTS` = Remove accounts in ACCOUNT_NAMES for testing, debugging, or excluding the purchase of the stock from the account. Separated by commas.

### Sofi Installation

Clone the repository:

```bash
git clone https://github.com/Prem-ium/Auto-StockTrader
cd Auto-StockTrader
```

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
  python sofi_main.py buy APPL slow 30
```
