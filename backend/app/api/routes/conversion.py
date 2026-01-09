from fastapi import APIRouter, UploadFile, File
router = APIRouter(prefix="/convert")
@router.post("/pdf-to-text")
async def pdf_to_text(file: UploadFile = File(...)):
    return {"text": ""}
@router.post("/image-to-png")
async def image_to_png(file: UploadFile = File(...)):
    return {"url": ""}