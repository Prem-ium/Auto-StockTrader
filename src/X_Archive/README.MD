
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

Automating orders for Sofi Invest can be attempted through the `sofi_main.py` Python script. 

Sofi is very unpredictable and unstable, and has been archived. 
You can still attempt to use it, however the chances of every order going through are slim as Sofi Invest has weird order pages that are different depending on the stock.

### Sofi Environment Variables

If you plan to use the Selenium IDE Helper file:
`SOFI_AI`= List of account numbers in an array, can be retrieved by using the JavaScript code in `\src\X_Archive\SoFi_Account_Array.js` of the repository. Sign into your account, head to Invest homepage, and paste the code into the browser console.

Otherwise:

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
  cd src/X_Archive
```
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