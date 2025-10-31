@echo off
REM Run from repo root so "algorithms" is importable
cd /d %~dp0\..
SET PYTHONPATH=%CD%
uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
