# app/utils.py
from PIL import Image, ImageDraw
from pathlib import Path
import os, io, json

def draw_boxes_pil(image_pil, boxes):
    draw = ImageDraw.Draw(image_pil)
    for b in boxes:
        x1,y1,x2,y2 = [int(v) for v in b["xyxy"]]
        draw.rectangle([x1,y1,x2,y2], outline="red", width=3)
        label = str(b.get("class_id", ""))
        draw.text((x1, max(y1-12,0)), label, fill="red")
    return image_pil

def pil_from_bytes(b: bytes):
    return Image.open(io.BytesIO(b)).convert("RGB")

def save_bytes(path: str, b: bytes):
    Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        f.write(b)

def save_json(path: str, obj):
    Path(os.path.dirname(path)).mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2)
