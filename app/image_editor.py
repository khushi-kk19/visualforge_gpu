import torch
from PIL import Image
from diffusers import StableDiffusionInpaintPipeline
import numpy as np
from detector import ObjectDetector
import warnings
import os
import io
warnings.filterwarnings('ignore')

class ImageEditor:
    def __init__(self):
        """Initialize image generation pipelines"""
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        print("Loading inpainting model... (this may take a few minutes)")
        self.inpaint_pipe = StableDiffusionInpaintPipeline.from_pretrained(
            "runwayml/stable-diffusion-inpainting",
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            safety_checker=None
        ).to(self.device)
        print("Model loaded successfully!")
    
    def remove_object(self, image_path, object_name, output_path="output_removed.png"):
        """Remove an object from image"""
        try:
            image = Image.open(image_path).convert("RGB")
            original_size = image.size
            image = image.resize((512, 512))
            
            mask = self._create_mask_for_object(image_path, object_name)
            mask = mask.resize((512, 512))
            
            prompt = f"a clean background without {object_name}"
            result = self.inpaint_pipe(
                prompt=prompt,
                image=image,
                mask_image=mask,
                num_inference_steps=30,
                guidance_scale=7.5
            ).images[0]
            
            # Resize back to original and save
            result = result.resize(original_size)
            result.save(output_path, "PNG")
            print(f"Image saved to {output_path}")
            return output_path
        except Exception as e:
            print(f"Error in remove_object: {e}")
            raise
    
    def replace_object(self, image_path, old_object, new_object, output_path="output_replaced.png"):
        """Replace object with another"""
        try:
            image = Image.open(image_path).convert("RGB")
            original_size = image.size
            image = image.resize((512, 512))
            
            mask = self._create_mask_for_object(image_path, old_object)
            mask = mask.resize((512, 512))
            
            prompt = f"a {new_object}"
            result = self.inpaint_pipe(
                prompt=prompt,
                image=image,
                mask_image=mask,
                num_inference_steps=30,
                guidance_scale=7.5
            ).images[0]
            
            result = result.resize(original_size)
            result.save(output_path, "PNG")
            print(f"Image saved to {output_path}")
            return output_path
        except Exception as e:
            print(f"Error in replace_object: {e}")
            raise
    
    def add_object(self, image_path, new_object, output_path="output_added.png"):
        """Add new object to image"""
        try:
            image = Image.open(image_path).convert("RGB")
            original_size = image.size
            image = image.resize((512, 512))
            
            mask = Image.new("L", image.size, 0)
            mask_array = np.array(mask)
            mask_array[-150:, -150:] = 255
            mask = Image.fromarray(mask_array)
            
            prompt = f"add a {new_object} to the scene"
            result = self.inpaint_pipe(
                prompt=prompt,
                image=image,
                mask_image=mask,
                num_inference_steps=30,
                guidance_scale=7.5
            ).images[0]
            
            result = result.resize(original_size)
            result.save(output_path, "PNG")
            print(f"Image saved to {output_path}")
            return output_path
        except Exception as e:
            print(f"Error in add_object: {e}")
            raise
    
    def change_style(self, image_path, style, output_path="output_styled.png"):
        """Change image style"""
        try:
            image = Image.open(image_path).convert("RGB")
            original_size = image.size
            image = image.resize((512, 512))
            
            mask = Image.new("L", image.size, 0)
            
            prompt = f"rerender this image in {style} style"
            result = self.inpaint_pipe(
                prompt=prompt,
                image=image,
                mask_image=mask,
                num_inference_steps=30,
                guidance_scale=7.5
            ).images[0]
            
            result = result.resize(original_size)
            result.save(output_path, "PNG")
            print(f"Image saved to {output_path}")
            return output_path
        except Exception as e:
            print(f"Error in change_style: {e}")
            raise
    
    def _create_mask_for_object(self, image_path, object_name):
        """Create mask for detected object"""
        try:
            detector = ObjectDetector()
            detections = detector.detect_objects(image_path)
            
            image = Image.open(image_path).convert("RGB")
            mask = Image.new("L", image.size, 0)
            mask_array = np.array(mask)
            
            found = False
            for det in detections:
                if det["object"].lower() == object_name.lower():
                    x1, y1, x2, y2 = det["box"]
                    mask_array[int(y1):int(y2), int(x1):int(x2)] = 255
                    found = True
            
            if not found:
                print(f"Warning: Object '{object_name}' not found. Using default mask.")
                mask_array[-200:, -200:] = 255
            
            return Image.fromarray(mask_array)
        except Exception as e:
            print(f"Error in _create_mask_for_object: {e}")
            raise

if __name__ == "__main__":
    editor = ImageEditor()
    print("Editor initialized OK")