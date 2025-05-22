# 📈 Additional Help: Automating Stock Trades with Selenium IDE

This guide explains how to retrieve the sensitive account information required for automation and how to correctly configure your `.env` file using the format provided in `env.example`.

> 💎 For a seamless experience without manual configuration for Chase/Fidelity/Ally, [consider becoming a **Gold Sponsor**](https://github.com/sponsors/Prem-ium) to unlock premium features and ready-to-run scripts.

---

## 🏦 Chase Automation

Automate trades on **J.P. Morgan Self-Directed Investing** using the `Chase_Auto.side` file and the Selenium IDE extension.

### 🔍 Retrieve Account Identifiers

1. Navigate to the Chase [Trade Stocks page](https://secure07ea.chase.com/web/auth/dashboard#/dashboard/trade/equity/entry).
2. Select your account from the dropdown.
3. Copy the **AI number** from the URL. It will look like this:

   ```
   https://secure07ea.chase.com/web/auth/dashboard#/dashboard/trade/equity/entry;ai={YOUR_AI_HERE};sym=
   ```

   ![Chase AI Example](https://user-images.githubusercontent.com/80719066/216079858-746af166-8387-41ad-9564-dd0c6285eb39.png)

### 🧪 Update Test Cases in Selenium IDE

Replace the `return` statement in each Buy/Sell test case:

```javascript
return [['54658965', 'YOUR', 'AI', 'GOES', 'HERE'], ['YOUR', 'AI', 'for-another-login', 'GOES', 'HERE']]
```

### 💹 Provide Stock Ticker

Add your stock ticker as a `return` statement:

```javascript
return "STOCK_TICKER"
```

Start the test to execute the trade.

---

## 📊 Fidelity Automation

1. Log in to [Fidelity Portfolio](https://digital.fidelity.com/ftgw/digital/portfolio).
2. Open Developer Tools:

   * **Chrome/Edge**: Right-click → Inspect
   * **Firefox**: Right-click → Inspect Element
3. Copy and paste the [Fidelity Account Array Script](https://github.com/Prem-ium/Auto-StockTrader/blob/main/src/Helper_JS_Scripts/Fidelity_Account_Array.js) into the **Console** tab.
4. Press **Enter** to run the script. It will output account numbers.
5. Copy the resulting array.
6. Paste it into the `.env` file under:

```env
FIDELITY_AI=["12345678", "23456789"]
```

> 🧪 Tip: You can also run the Fidelity login test in the `.side` file (index `1`) to retrieve account IDs.

---

## 📈 Ally Invest Automation

1. On the [Ally Invest Settings Page](https://live.invest.ally.com/settings), change default orders to a low-risk penny stock (e.g., Quantity: 1, Order Type: Market).
2. Install and open the **Selenium IDE** browser extension.
3. Log in to **Ally**, **Vanguard**, or **Firstrade** in your browser.
4. Add account numbers to the test script:

```javascript
return ["54566343", "34546546", "54566546"]
```

5. Add the stock ticker and (optionally) a limit price:

```javascript
return "TICKER"
return "LIMIT_PRICE"
```

6. Start the test to run automation.

![Ally Example](https://user-images.githubusercontent.com/80719066/216331460-00897c0e-1e21-4413-ac81-1931fe906de0.png)