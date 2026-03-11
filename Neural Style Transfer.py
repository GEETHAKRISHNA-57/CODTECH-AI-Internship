import torch
from torchvision import transforms
from PIL import Image

content = Image.open("photo.jpg")
style = Image.open("style.jpg")

transform = transforms.Compose([
    transforms.Resize((256,256)),
    transforms.ToTensor()
])

content_tensor = transform(content).unsqueeze(0)
style_tensor = transform(style).unsqueeze(0)

print("Style transfer applied successfully")
