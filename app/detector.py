import torch
import warnings
warnings.filterwarnings('ignore')

# Patch torch.load to disable weights_only
original_load = torch.load
def patched_load(f, *args, **kwargs):
    kwargs['weights_only'] = False
    return original_load(f, *args, **kwargs)
torch.load = patched_load

from ultralytics import YOLO
import cv2
from PIL import Image
import numpy as np

class ObjectDetector:
    def __init__(self, weights="yolov8n.pt"):
        """Initialize YOLO detector"""
        self.model = YOLO(weights)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
    
    def detect_objects(self, image_path):
        """
        Detect objects in an image
        Returns: list of detected objects with confidence scores
        """
        results = self.model(image_path, device=self.device)
        
        detections = []
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls[0])
                class_name = result.names[class_id]
                confidence = float(box.conf[0])
                detections.append({
                    "object": class_name,
                    "confidence": confidence,
                    "box": box.xyxy[0].tolist()
                })
        
        return detections
    
    def visualize_detections(self, image_path, output_path="output_detected.jpg"):
        """Draw bounding boxes on image"""
        results = self.model(image_path, device=self.device)
        annotated_frame = results[0].plot()
        cv2.imwrite(output_path, annotated_frame)
        return output_path

if __name__ == "__main__":
    detector = ObjectDetector("yolov8n.pt")
    print("Detector initialized OK")