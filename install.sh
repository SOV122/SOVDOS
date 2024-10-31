#!/bin/bash

# Banner
echo "=========================================="
echo "          SOVDOS Installation"
echo "=========================================="

# Check if running as root
if [ "$EUID" -ne 0 ]; then 
    echo "Please run as root"
    exit
fi

# Update package list and install Python3 if not installed
echo "Checking for Python3..."
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Installing Python3..."
    apt update && apt install -y python3
else
    echo "Python3 is already installed."
fi

# Check for Python3 pip and install if missing
echo "Checking for pip3..."
if ! command -v pip3 &> /dev/null
then
    echo "pip3 not found. Installing pip3..."
    apt install -y python3-pip
else
    echo "pip3 is already installed."
fi

# Make sovdos.py executable
echo "Setting up SOVDOS..."
chmod +x sovdos.py

# Create a symbolic link to run SOVDOS from anywhere
echo "Creating symbolic link..."
ln -sf "$(pwd)/sovdos.py" /usr/local/bin/sovdos

echo "=========================================="
echo "        SOVDOS Installation Complete!"
echo " You can now run SOVDOS using 'sovdos'"
echo "=========================================="
