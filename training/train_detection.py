# training/train_detection.py
from ultralytics import YOLO
import torch
import argparse

# Allow ultralytics models to be loaded with newer PyTorch versions
torch.serialization.add_safe_globals([YOLO])

parser = argparse.ArgumentParser()
parser.add_argument("--data", type=str, required=True, help="path to YAML data config for YOLO")
parser.add_argument("--epochs", type=int, default=50)
parser.add_argument("--imgsz", type=int, default=640)
parser.add_argument("--batch", type=int, default=16)
parser.add_argument("--name", type=str, default="visualforge_exp")
args = parser.parse_args()

# Use yolov8n or yolov8s as base; GPU will be used automatically if available
model = YOLO("yolov8n.pt")  # or path to custom cfg
model.train(data=args.data, epochs=args.epochs, imgsz=args.imgsz, batch=args.batch, name=args.name, device="cuda")