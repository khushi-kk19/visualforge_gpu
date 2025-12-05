# VisualForge - AI Image Editor

An advanced AI-powered image editing platform that uses YOLOv8 for object detection and Stable Diffusion for generative AI tasks.

## Features

**Smart Object Detection** - Detects all objects in images using YOLOv8
**Remove Objects** - Remove unwanted objects with AI inpainting
**Replace Objects** - Replace objects with anything you want
**Add Objects** - Add new objects to your scenes
**Style Transfer** - Transform image styles (oil painting, watercolor, etc.)
**GPU Acceleration** - CUDA-optimized for fast processing

## Tech Stack

- **Backend**: Python Flask
- **Detection**: YOLOv8 (Large Model)
- **Image Generation**: Stable Diffusion 2 Inpainting
- **Frontend**: HTML5, CSS3, JavaScript
- **GPU**: CUDA 12.8 + PyTorch 2.9.1

## Installation

### Prerequisites
- Python 3.10+
- NVIDIA GPU with CUDA support
- 16GB+ RAM recommended

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/visualforge_gpu.git
cd visualforge_gpu
```

2. Create virtual environment:
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Linux/Mac
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app/main.py
```

5. Open browser and visit:
```
http://127.0.0.1:5000
```

## Usage

### Object Detection
1. Upload an image via drag & drop or file browser
2. AI automatically detects all objects
3. Choose an editing operation

### Remove Objects
- Select object from dropdown
- Click "Remove" button
- AI removes object and fills background

### Replace Objects
- Select object to replace
- Enter new object name
- Click "Replace" button

### Add Objects
- Enter object name to add
- Click "Add" button
- AI adds object to scene

### Style Transfer
- Select from predefined styles
- Click "Apply Style"
- Image transforms to selected style

## Project Structure

```
visualforge_gpu/
├── app/
│   ├── templates/
│   │   └── index.html           # Main web interface
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css        # Styling
│   │   └── js/
│   │       └── script.js        # Frontend logic
│   ├── detector.py              # YOLOv8 object detection
│   ├── image_editor.py          # Image generation & editing
│   └── main.py                  # Flask application
├── training/
│   ├── train_detection.py       # YOLO training script
│   └── download_voc_with_torchvision.py  # Dataset download
├── uploads/                     # Temporary image storage
├── requirements.txt             # Project dependencies
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

## API Endpoints

- `POST /detect` - Detect objects in image
- `POST /remove` - Remove object from image
- `POST /replace` - Replace object with another
- `POST /add` - Add new object to image
- `POST /style` - Apply style transfer

## Model Information

### YOLOv8 Large (yolov8l.pt)
- **Parameters**: 43.7M
- **Size**: ~76MB
- **Speed**: ~150ms per image (GPU)
- **Accuracy**: High (mAP 52.9)

## Performance

- **Detection Speed**: ~150-200ms per image (RTX 3090)
- **Inpainting Speed**: ~30-50 seconds per image
- **Supported Formats**: JPG, PNG, BMP, WebP

## Known Limitations

- Large images (>2048px) automatically resized to 512px for editing
- Style transfer takes longer than object detection
- GPU VRAM: 8GB+ recommended

## Future Enhancements

- [ ] Batch processing
- [ ] Multi-GPU support
- [ ] Custom model training
- [ ] Video editing support
- [ ] Real-time webcam processing
- [ ] Advanced masking tools


## Credits

- YOLOv8: [Ultralytics](https://github.com/ultralytics/ultralytics)
- Stable Diffusion: [Stability AI](https://stability.ai/)
- PyTorch: [Meta AI](https://pytorch.org/)


---

**Made for AI image editing**# visualforge_gpu
