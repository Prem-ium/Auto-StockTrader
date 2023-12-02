# Additional Help: Automating Stock Trades with Selenium IDE

This README should help answer how to retrieve necessary sensitive account numbers and values for the project to work properly. Remember to use `env.example`'s format to ensure the automation is successful.

## Chase Automation

Automating orders for Chase's J.P. Morgan Self-Directed Investing Brokerage is facilitated through the `Chase_Auto.side` file and Selenium IDE Extension.

**Retrieve Account Identifiers:** For each account, visit the Chase Trade Stock webpage, select the account from the dropdown, and save the AI number from the URL (located at {YOUR_AI_HERE}).
    - Example URL: `https://secure07ea.chase.com/web/auth/dashboard#/dashboard/trade/equity/entry;ai={YOUR_AI_HERE};sym=`
    ![image](https://user-images.githubusercontent.com/80719066/216079858-746af166-8387-41ad-9564-dd0c6285eb39.png)

**Update Test Cases:** Copy the AI for each account and replace the return statement in all test cases (Buy/Sell Test in Selenium IDE).
```javascript
return [['54658965', 'YOUR', 'AI', 'GOES', 'HERE']]
```
**Provide Stock Ticker:** Input the Stock Ticker as a return statement and click the start button to begin automation.
```javascript
return "STOCK_TICKER"
```

## Fidelity Automation

1. Login & Open Fidelity Portfolio Webpage (https://digital.fidelity.com/ftgw/digital/portfolio)

2. Access the Browser's Developer Tools:
   - If you're using Google Chrome or Microsoft Edge: Right-click anywhere on the webpage, then click "Inspect."
   - If you're using Mozilla Firefox: Right-click anywhere on the webpage, then select "Inspect Element."

3. Copy and Paste the [Fidelity Account Array Script](https://github.com/Prem-ium/Auto-StockTrader/blob/main/src/Helper_JS_Scripts/Fidelity_Account_Array.js):

   - In the Developer Tools panel, find the "Console" tab or section.
   - Copy the entire script
   - Paste the script into the space in the Console.

4. Run the Script:
   - After pasting the script, press "Enter" on your keyboard. The script will execute, and you'll see numbers in the Console.

5. Copy the Numbers:
   - Select all the numbers in the Console by clicking and dragging your mouse cursor.
   - Right-click on the selected numbers and choose "Copy."

6. Paste the Numbers into .env file:
   - Open the ".env" file using a text editor like Visual Studio Code, Notepad, or TextEdit.
   - Paste copied array into the Fidelity_AI env variable
   - Save the ".env" file.

You can also use the Fidelity side project login test, with index of 1, to obtain the account numbers.


## Ally Invest Automation

On the [Ally Invest Settings Webpage](https://live.invest.ally.com/settings), update default orders for all accounts to be a small penny stock for the default stock ticker to minimize risk (Market, & Quantity: 1).

1. **Extension Installation:** Download the Selenium IDE Extension from your browser's extension store and open the corresponding project file.
2. **Login:** Log in to Vanguard, Firstrade, or Ally on your browser.
3. **Retrieve Account Numbers:** Retrieve the list of your account number(s) and place them in the return execute script on the buy and sell test(s).
    ```javascript
    return ["54566343", "34546546", "54566546"]
    ```
4. **Enter Stock Ticker:** Input the Stock Ticker and start the test.
    ![image](https://user-images.githubusercontent.com/80719066/216331460-00897c0e-1e21-4413-ac81-1931fe906de0.png)

5. **Set Limit Price (if applicable):** Input the Limit Price variable.
6. **Start Test:** Begin the automation.
