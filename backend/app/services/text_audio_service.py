import tempfile
import shutil
from pathlib import Path
from typing import Literal

# IMPORTANT: reuse your existing classes; we don't edit them
from algorithms.LSB import LSB
from algorithms.PhaseCoding import PhaseCoding

AlgorithmName = Literal["LSB", "PhaseCoding"]

async def _save_upload_to_temp(upload_file) -> Path:
    suffix = Path(upload_file.filename).suffix or ".wav"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        content = await upload_file.read()
        tmp.write(content)
        return Path(tmp.name)

def _select_algorithm(name: AlgorithmName):
    if name == "PhaseCoding":
        return PhaseCoding()
    return LSB()

async def encode_text_into_audio(upload_file, secret_text: str, algorithm: AlgorithmName) -> str:
    in_path = await _save_upload_to_temp(upload_file)
    algo = _select_algorithm(algorithm)
    # Your .encode returns the output file path
    out_path = algo.encode(str(in_path), secret_text)
    # Ensure file is accessible to FileResponse; keep it where algorithm saved it
    return out_path

async def decode_text_from_audio(upload_file, algorithm: AlgorithmName) -> str:
    in_path = await _save_upload_to_temp(upload_file)
    algo = _select_algorithm(algorithm)
    text = algo.decode(str(in_path))
    return text
