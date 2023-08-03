#!/bin/bash

# Update package lists
sudo apt update

# Install packages listed in the exported file
while read -r package; do
    sudo apt install -y "$package"
done < installed_packages.txt

echo "Installation of packages completed."
