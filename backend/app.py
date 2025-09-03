from inference import censor_video_from_bytes
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
import io
from typing import Annotated
import nest_asyncio

nest_asyncio.apply()
app = FastAPI()

@app.get("/")
async def read_root():
    """
    Root endpoint that returns a simple greeting.
    """
    return {"message": "Health check: API is running!"}

@app.get("/test")
async def read_root():
    """
    Root endpoint that returns a simple greeting.
    """
    return {"message": "Test_message: API is running!"}


@app.post("/upload_video/")
async def process_video_endpoint(video_file: UploadFile = File(...)):
    video_bytes = await video_file.read()

    # Processa o vídeo
    processed_bytes = censor_video_from_bytes(video_bytes)

    return Response(content=processed_bytes, media_type="video/mp4")