
# Auto Stock Trader

A short and sweet python script to help automate the purchase or sale of a stock across multiple accounts on Sofi, Chase, (and more) Invest.




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`ACCOUNT_NAMES` = A string of names of investment accounts, seperated by commas.

`SOFI_LOGIN` = Login credentials of SOFI, seperated by ':'

`EXCLUDE_ACCOUNTS` = Remove accounts in ACCOUNT_NAMES for testing, debugging, or excluding the purchase of the stock from the account. Seperated by commas.

## Features

- Automation of purchase of stock across multiple accounts
- Timer (Pass in how many seconds the program should wait between accounts)


## Installation

Clone the repository

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
  python main.py buy APPL
```
or, to wait 30 seconds in-between each account
```bash
  python main.py buy APPL slow 30
```
