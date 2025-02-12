from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch

class ImageCaptioningModel:
    def __init__(self):
        # Load the pretrained model and processor
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        self.model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    def generate_caption(self, image_file):
        # Open the image from the file object
        image = Image.open(image_file).convert("RGB")
        
        # Preprocess image
        inputs = self.processor(image, return_tensors="pt")
        
        # Generate caption
        with torch.no_grad():
            output = self.model.generate(**inputs)

        # Decode and return text
        caption = self.processor.batch_decode(output, skip_special_tokens=True)[0]
        return caption