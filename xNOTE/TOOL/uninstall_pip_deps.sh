#!/bin/bash

# Get a list of all installed packages
packages=$(pip list --format=freeze | grep -v '^\-e' | cut -d = -f 1)

# Uninstall each package
for package in $packages
do
    pip uninstall -y $package
done

echo "All pip packages have been uninstalled."