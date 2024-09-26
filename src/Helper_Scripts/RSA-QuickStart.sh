#!/bin/bash
# Set directory variable to the path of the project folder
DIRECTORY=

# Change to the project directory
if [ -d "$DIRECTORY" ]; then
    cd "$DIRECTORY" || { echo "Failed to change directory to $DIRECTORY"; exit 1; }
else
    echo "Directory $DIRECTORY does not exist."
    exit 1
fi

read -p "Enter the ticker symbol: " ticker

# REPLACE THE PATH BELOW WITH YOUR OWN PATH TO THE PROJECT FOLDER
cd /path/to/your/project

python3 main.py $ticker

# Examples of quickstarting with different browsers and profiles
# Uncomment the lines below to enable them.

# read -p "Do you want to open browsers? (y/n): " open_browsers
# if [ "$open_browsers" == "y" ]; then
#    /path/to/msedge --profile-directory="Default" &
#    /path/to/brave --profile-directory="Default" &
#    /path/to/brave --profile-directory="Profile 1" &
# fi

sleep 15