# training/download_voc_with_torchvision.py
import os
from pathlib import Path
from torchvision import datasets
import torchvision

def download_voc(root_dir, year):
    """
    Download the Pascal VOC dataset for a given year using torchvision.
    root_dir: path where VOCdevkit will be created
    year: '2007' or '2012'
    """
    root = Path(root_dir).resolve()
    target = root / "VOCdevkit"
    target.mkdir(parents=True, exist_ok=True)
    # torchvision will create VOCdevkit/VOCyear/... structure
    print(f"Downloading VOC{year} to {target} (may take some minutes)...")
    datasets.VOCDetection(root=str(target), year=year, image_set='trainval', download=True)
    if year == '2007':
        # also download test if desired
        datasets.VOCDetection(root=str(target), year=year, image_set='test', download=True)
    print(f"DONE: VOC{year} downloaded under {target}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-root", default="C:\\datasets", help="root folder to hold VOCdevkit")
    parser.add_argument("--years", default="2007,2012", help="comma separated years, e.g. 2007,2012")
    args = parser.parse_args()
    years = [y.strip() for y in args.years.split(",") if y.strip()]
    for y in years:
        download_voc(args.out_root, y)
