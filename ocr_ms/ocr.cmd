@echo off
set ocr_path=E:\Users\Desktop\Atom\ocr\ocr_ms\ocr_main.py

python "%ocr_path%" %* >> "%~p1/ocr.log"
type "%~p1/ocr.log"
cmd