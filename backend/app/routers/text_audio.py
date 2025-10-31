from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from ..services.text_audio_service import encode_text_into_audio, decode_text_from_audio

router = APIRouter()

@router.post("/encode-text")
async def encode_text(
    file: UploadFile = File(..., description="Carrier audio (.wav or .mp3*)"),
    secret_text: str = Form(...),
    algorithm: str = Form("LSB"),  # "LSB" or "PhaseCoding"
):
    try:
        out_path = await encode_text_into_audio(file, secret_text, algorithm)
        return FileResponse(out_path, filename="encoded.wav", media_type="audio/wav")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Encoding failed")

@router.post("/decode-text")
async def decode_text(
    file: UploadFile = File(..., description="Stego audio (.wav)"),
    algorithm: str = Form("LSB"),
):
    try:
        text = await decode_text_from_audio(file, algorithm)
        return JSONResponse({"secret_text": text})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Decoding failed")
