from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
import shutil
import os

from app.services.text_extractor import extract_text
from app.services.ai_processor import process_text
from app.services.rag_service import store_document, answer_question

router = APIRouter()


class QuestionRequest(BaseModel):
    question: str


@router.get("/")
async def root():
    return {
        "status": "running"
    }


@router.post("/upload-document")
async def upload_document(file: UploadFile = File(...)):

    file_path = f"temp_{file.filename}"

    try:
        # Save uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Extract text
        extracted = extract_text(file_path)

        # Error handling
        if isinstance(extracted, dict) and "error" in extracted:
            return {
                "status": "error",
                "data": extracted
            }

        # Store document for RAG
        store_document(extracted["text"])

        # Generate summary / keywords / insights
        result = process_text(extracted)

        return {
            "status": "success",
            "data": result,
            "meta": {
                "length": len(extracted["text"]),
                "file_type": file.filename.split(".")[-1].lower()
            }
        }

    finally:
        # Cleanup temp file
        if os.path.exists(file_path):
            os.remove(file_path)


@router.post("/ask")
async def ask_document(payload: QuestionRequest):

    result = answer_question(payload.question)

    return {
        "status": "success",
        "data": result
    }