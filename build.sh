#!/usr/bin/env bash
# exit on error
set -o errexit

# Install Python dependencies from requirements.txt
pip install -r requirements.txt

# Install the poppler system package using apt-get
apt-get update && apt-get install -y poppler-utils
