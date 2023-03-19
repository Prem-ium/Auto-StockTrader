import os, json, sys
from dotenv             import load_dotenv

load_dotenv()
if len(sys.argv) == 2:
    TICKER = sys.argv[1].lower()
    print(f"Ticker: {TICKER}")
else:
    TICKER = None

FILE_TASK_MAP = {
    "CHASE_AI": {"file": "Chase_Auto.side", "task": ""},
    "ALLY_AI": {"file": "Ally_Auto.side", "task": ""},
    "FIRSTRADE_AI": {"file": "Firstrade_Auto.side", "task": ""},
    "VANGUARD_AI": {"file": "Vanguard_Auto.side", "task": ""},
    "FIDELITY_AI": {"file": "Fidelity_Auto.side", "task": ""}
}

CUSTOM_DIR = os.environ.get("CUSTOM_DIR", "")
FILES = []

def main():
    for var_name, info in FILE_TASK_MAP.items():
        if os.environ.get(var_name):
            FILES.append(info["file"])
            print(f"{var_name} is enabled.")
            info["task"] = os.environ[var_name].replace(" ", "")
        else:
            print(f"{var_name} is disabled.")
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
                if command['command'] == 'executeScript' and command['value'] == 'accounts':
                    # Update the target with the new value
                    command['target'] = f"return {task}"
                elif TICKER is not None and command['command'] == 'executeScript' and command['value'] == 'TICKER':
                    command['target'] = f"return '{TICKER}'"

        if CUSTOM_DIR:
            filePath = f'{CUSTOM_DIR}/{filePath}'
        else:
            filePath = f'ENV-{filePath}'
        # Create a new file with the updated data
        with open(filePath, 'w') as file:
            json.dump(data, file, indent=2)

        print(f"Created/Updated {filePath}!")

    if CUSTOM_DIR:
        os.startfile(CUSTOM_DIR)


if __name__ == "__main__":
    main()