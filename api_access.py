import requests
from PIL import Image
import io


def main():
    sample_image_path = "ADD PNG IMAGE PATH HERE"

    header = { "content-type": "image/png" }
    with open(sample_image_path, "rb") as f:
        image = f.read()

    resp = requests.post(
                        'https://qg33311cf5.execute-api.us-east-1.amazonaws.com/Testing', 
                        data = image, 
                        headers = header
                    )

    data = resp.content
    image_data = Image.open(io.BytesIO(data))
    image_data.save("FinalInpaintedImage.png")

if __name__ == "__main__":
    main()

