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

   # Check each package
   for package in "${packages[@]}"; do
     if conda search -c conda-forge "$package" > /dev/null 2>&1; then
       echo "YES - $package"
	   conda install -c conda-forge "$package" -y
     else
       echo "!!! - $package is NOT available on conda-forge"
     fi
   done