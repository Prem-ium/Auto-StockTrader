# Sofi Invest Automation

Automating orders for Sofi Invest can be attempted through the `sofi_main.py` Python script. 

Sofi is very unpredictable and unstable, and has been archived. 
You can still attempt to use it, however the chances of every order going through are slim as Sofi Invest has weird order pages that are different depending on the stock.

### Sofi Environment Variables

To run this project, you will need to add the following environment variables to your .env file:

`ACCOUNT_NAMES` = A string of names of investment accounts, separated by commas.

`SOFI_LOGIN` = Login credentials of SOFI, separated by ':'

`EXCLUDE_ACCOUNTS` = Remove accounts in ACCOUNT_NAMES for testing, debugging, or excluding the purchase of the stock from the account. Separated by commas.

### Running Sofi {#Running_Sofi}

Specifiy commands in the following order within a terminal:

1. Whether to 'buy' or 'sell'
2. Stock Ticker's symbol
3. (Optional) 'slow' if you wish to pass in a sleep timer
4. sleep timer value

```bash
  cd src
  python sofi_main.py buy APPL
```
or, to wait 30 seconds in-between each account
```bash
  cd src
  python sofi_main.py buy APPL 100.54 slow 30
```
or, to place limit (on certain stocks)
```bash
  cd src
  python sofi_main.py buy GNUS 0.50 slow 30
```