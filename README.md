# Image Inpainting
The following repository presents an Image Inpainting project. The inpainting process employs the **Fast Marching Method** to produce distance maps of the points in a region from the boundary of that. To limit the scope of this project, it is only designed to eradicate *yellow* lines from images. Due to this constraint, image masks can be generated automatically to detect yellow lines to be inpainted over.

## Technologies Used
- numpy
- Pillow

## Results

| Initial image               | Inpainted Image               | 
| :-------------------------: | :---------------------------: | 
| ![alt text](https://github.com/Pushkar-Bhuse/ImageInpainting/master/blob/raw_image1.png?raw=true) | ![alt text] (https://github.com/Pushkar-Bhuse/ImageInpainting/master/blob/inpainted1.png?raw=true) | 
| ![alt text](https://github.com/Pushkar-Bhuse/ImageInpainting/master/blobraw_image2.png?raw=true) | ![alt text] (https://github.com/Pushkar-Bhuse/ImageInpainting/master/blobinpainted2.png?raw=true) | 

## Instructions to Run
In order to access the API hosted as a serverless AWS Lambda Funtion, run the following command.
```
python3 api_access.py
```
**NOTE:** Before running this file, do not forget to add the source and desitation path of raw image and inpainted image respectively (Images have to be in PNG format).
