#   BSD 3-Clause License
#   
#   Copyright (c) Present-2023, Prem Patel
#   
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions are met:
#   
#   1. Redistributions of source code must retain the above copyright notice, this
#      list of conditions and the following disclaimer.
#   
#   2. Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#   
#   3. Neither the name of the copyright holder nor the names of its
#      contributors may be used to endorse or promote products derived from
#      this software without specific prior written permission.
#   
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#   IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#   DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#   FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#   DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#   SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#   CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#   OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



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
LOGINS = []

def main():
    for var_name, info in FILE_TASK_MAP.items():
        if os.environ.get(var_name):
            FILES.append(info["file"])
            print(f"{var_name} is enabled.")

            if var_name == "SCHWAB_AI":
                info["task"] = "Array.from({length: " + os.environ[var_name] + "}, (_, i) => i);"
            elif var_name == "MERRILL_AI":
                info["task"] = "Array.from({length: " +os.environ[var_name] + "}, (_, i) => i + 1);"
            else:
                info["task"] = os.environ[var_name].replace(" ", "")

            try:
                LOGINS.append(os.environ[var_name.split("_")[0] + "_LOGIN"])
            except:
                LOGINS.append("LOGIN:HERE")
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
                # Store Login information, if provided
                if command['command'] == 'store' and 'LOGIN' in command['value']:
                    command['target'] = LOGINS.pop(0)

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

    if CUSTOM_DIR and len(sys.argv) != 2:
        os.startfile(CUSTOM_DIR)

    # Create a file shortcut of RSA-QuickStart.bat located in /src to the desktop
    if not os.path.exists(f"{os.environ['USERPROFILE']}\\Desktop\\RSA-QuickStart.bat"):
        shutil.copyfile("src\\RSA-QuickStart.bat", f"{os.environ['USERPROFILE']}\\Desktop\\RSA-QuickStart.bat")
        print(f"\n\nCreated/Updated:\t{os.environ['USERPROFILE']}\\Desktop\\RSA-QuickStart.bat")

    print(f"\n\nProgram successfully completed! Thanks for using Prem-ium\'s Automated Stock Trading project!\nPlease leave a star or drop a follow if you found this project cool!\nhttps://github.com/Prem-ium/Auto-StockTrader\n")

if __name__ == "__main__":
    main()