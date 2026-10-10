"""FRIS prototype API. Validates and hashes uploads only. It never executes or unpacks firmware,
and it does not store files. Syft / NVD / CISA KEV integration is planned (see README)."""
import hashlib, os
from fastapi import FastAPI, UploadFile, HTTPException

ALLOWED = {".bin", ".img", ".tar", ".zip", ".gz", ".tgz", ".trx", ".chk", ".squashfs"}
MAX_BYTES = 64 * 1024 * 1024
app = FastAPI(title="FRIS API (prototype)")

@app.get("/api/health")
def health():
    return {"status": "ok", "mode": "demo", "analysis_engine": "not configured"}

@app.post("/api/upload")
async def upload(file: UploadFile):
    ext = os.path.splitext(file.filename or "")[1].lower()
    if ext not in ALLOWED:
        raise HTTPException(415, f"Unsupported file type '{ext}'")
    h, size = hashlib.sha256(), 0
    while chunk := await file.read(1 << 20):  # streamed, never held fully in memory
        size += len(chunk)
        if size > MAX_BYTES:
            raise HTTPException(413, "File exceeds 64 MB limit")
        h.update(chunk)
    return {"filename": file.filename, "size": size, "sha256": h.hexdigest(), "analysed": False}
