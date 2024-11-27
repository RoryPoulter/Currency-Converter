#!/bin/bash
# Input API key
echo "Enter API key:"
read -r api_key
# Installs the dependencies
pip install -r requirements.txt
# Move to main directory
cd ../
# Create .env file
echo "ER_API_KEY=$api_key" >> .env
# Move to src
cd src || exit
# Loads server
python server.py