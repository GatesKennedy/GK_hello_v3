# main.py
import uvicorn

from SERVER import routes
from SERVER.config import get_app

if __name__ == "__main__":
    app = get_app()

    # uvicorn server config
    uvicorn_config = {
        "app": "SERVER.config:app",
        "host": "0.0.0.0",
        "port": 8000,
        "reload": True,
        "workers": 1
    }

    # run uvicorn server
    uvicorn.run(**uvicorn_config)