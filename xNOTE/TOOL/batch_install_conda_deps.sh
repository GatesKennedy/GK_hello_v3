#!/bin/bash

# List of packages to check
packages=(
  "annotated-types" "anyio" "click" "dnspython" "email-validator" "fastapi"
  "fastapi-cli" "h11" "httpcore" "httptools" "httpx" "jinja2" "markdown-it-py"
  "markupsafe" "mdurl" "orjson" "pydantic" "pydantic-core" "pygments" "pyside6"
  "pyside6-addons" "pyside6-essentials" "python-dotenv" "python-multipart"
  "pyyaml" "rich" "shellingham" "shiboken6" "sniffio" "starlette" "typer"
  "ujson" "urllib3" "uvicorn" "uvloop" "watchfiles" "websockets"
)

# Array to store available packages
available_packages=()

# Check each package
echo -e "Searching conda-forge for packages...\n"
for package in "${packages[@]}"; do
  if conda search -c conda-forge "$package" > /dev/null 2>&1; then
    echo "Found - $package on conda-forge"
    available_packages+=("$package")
  else
    echo "!!! - $package is NOT available on conda-forge"
  fi
done

# Install all available packages at once
if [ ${#available_packages[@]} -gt 0 ]; then
  echo "Installing available packages from conda-forge..."
  conda install -c conda-forge "${available_packages[@]}" -y
  echo "Installation complete."
else
  echo "No packages were found to be available on conda-forge."
fi