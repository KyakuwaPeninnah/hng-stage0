from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pytz


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def get_api_info():
    """
     Returns essential information in JSON format.
    """

    return {
        "email": "pennykyakuwa@gmail.com",
        "current_datetime": datetime.now().isoformat() + "Z",
        "github_url": "https://github.com/KyakuwaPeninnah/hng-stage0",
    }