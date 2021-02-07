import json
import numpy as np
from PIL import Image
import base64

from createMask import color_mask, write_to_file
from inpaint import inpaint

def lambda_handler(event, context):
    
    

    body = event["body"]
    
    if (not body):
        return {
            'statusCode': "400",
            'messages': "No data sent"
        }
        
        
    write_to_file("/tmp/image.png", body)

    image = np.array(Image.open("/tmp/image.png"))
    
    c = np.array([ 
                    [255, 255, 0],  # bright yellow
                    [255, 255, 50]  # dark yellow
                ])

    mask_img = color_mask(image, 
                    [c[0][0], c[1][0]],
                    [c[0][1], c[1][1]],
                    [c[0][2], c[1][2]])

    in_img = np.array(Image.open("/tmp/image.png"))
    mask = mask_img.astype(bool, copy=False)
    
    out_img = in_img.copy()
    inpaint(out_img, mask, 1)
    
    out_img = Image.fromarray(out_img)
    out_img.save("/tmp/final.png")
    
    # Converting final image into utf-8 encoded base64
    with open("/tmp/final.png", "rb") as imageFile:
        binary_file_data = imageFile.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        encoded_img = base64_encoded_data.decode('utf-8')
        
    
    return {
      "isBase64Encoded": True,
      "statusCode": 200,
      "headers": { "content-type": "image/png"},
      "body":  encoded_img
    }