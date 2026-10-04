from fastapi import FastAPI, UploadFile, File
import hashlib

app = FastAPI(title="Cyber File Scanner")


@app.get("/")
def home():
    return {
        "status": "online",
        "message": "Cyber File Scanner is running"
    }


@app.post("/scan")
async def scan_file(file: UploadFile = File(...)):
    file_data = await file.read()

    sha256_hash = hashlib.sha256(file_data).hexdigest()

    return {
        "filename": file.filename,
        "file_size": len(file_data),
        "sha256": sha256_hash
    }