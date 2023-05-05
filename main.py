import  os
import  json
import  sys
import  shutil

from    dotenv             import load_dotenv

load_dotenv()
if len(sys.argv) == 2:
    TICKER = sys.argv[1].upper()
    print(f"Argument Received\nTicker: {TICKER}\n\n")
else:
    TICKER = None

FILE_TASK_MAP = {
    "CHASE_AI": {"file": "src\Selenium_IDE\Chase_Auto.side", "task": ""},
    "FIRSTRADE_AI": {"file": "src\Selenium_IDE\Firstrade_Auto.side", "task": ""},
    "VANGUARD_AI": {"file": "src\Selenium_IDE\Vanguard_Auto.side", "task": ""},
    "FIDELITY_AI": {"file": "src\Selenium_IDE\Fidelity_Auto.side", "task": ""},
    "SCHWAB_AI": {"file": "src\Selenium_IDE\Schwab_Auto.side", "task": ""},
    "SOFI_AI": {"file": "src\X_Archive\Sofi Helper.side", "task": ""},
    "ALLY_AI": {"file": "src\Selenium_IDE\Ally_Auto.side", "task": ""},
    "MERRILL_AI": {"file": "src\Selenium_IDE\Merrill_Auto.side", "task": ""},
}

CUSTOM_DIR = os.environ.get("CUSTOM_DIR", "")
FILES = []

def main():
    for var_name, info in FILE_TASK_MAP.items():
        if os.environ.get(var_name):
            FILES.append(info["file"])
            print(f"{var_name} is enabled.")
            if var_name == "SCHWAB_AI":
                info["task"] = "Array.from({length: " + os.environ[var_name] + "}, (_, i) => i);"
            elif var_name == "MERRILL_AI":
                info["task"] = [i + 1 for i in range(int(os.environ[var_name].replace(" ", "").replace(",", ", ")))]
            else:
                info["task"] = os.environ[var_name].replace(" ", "")
        else:
            print(f"{var_name} is disabled. Skipping...")
    print('\n\n')
    for filePath in FILES:
        task = ""
        for var_name, info in FILE_TASK_MAP.items():
            if info["file"].lower() in filePath.lower():
                task = info["task"]
                break

        # Load the JSON data
        with open(filePath, 'r') as file:
            data = json.load(file)

        for test in data['tests']:
            for command in test['commands']:
                # Update Ticker, if provided
                if TICKER is not None and command['value'] == 'TICKER':
                    command['target'] = f"return '{TICKER}'" if command['command'] == 'executeScript' else TICKER
                # Update the account number(s) and break to next test
                if command['command'] == 'executeScript' and command['value'] == 'accounts':
                    command['target'] = f"return {task}"
                    break

        filePath = filePath.replace("src\\Selenium_IDE\\", "")
        filePath = filePath.replace("src\\X_Archive\\", "")

        filePath = f'{CUSTOM_DIR}/{filePath}' if CUSTOM_DIR else f'ENV-{filePath}'

        # Create a new file with the updated data
        with open(filePath, 'w') as file:
            json.dump(data, file, indent=2)

        print(f"Created/Updated:\t{filePath}!")

    if CUSTOM_DIR:
        os.startfile(CUSTOM_DIR)

    # Create a file shortcut of RSA-QuickStart.bat located in /src to the desktop
    if not os.path.exists(f"{os.environ['USERPROFILE']}\\Desktop\\RSA-QuickStart.bat"):
        shutil.copyfile("src\\RSA-QuickStart.bat", f"{os.environ['USERPROFILE']}\\Desktop\\RSA-QuickStart.bat")
        print(f"\n\nCreated/Updated:\t{os.environ['USERPROFILE']}\\Desktop\\RSA-QuickStart.bat")

    print(f"\n\nProgram successfully completed! Thanks for using Prem-ium\'s Automated Stock Trading project!\nPlease leave a star or drop a follow if you found this project cool!\nhttps://github.com/Prem-ium/Auto-StockTrader\n")

if __name__ == "__main__":
    main()