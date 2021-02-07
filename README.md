# Image Inpainting
The following repository presents an Image Inpainting project. The inpainting process employs the **Fast Marching Method** to produce distance maps of the points in a region from the boundary of that. To limit the scope of this project, it is only designed to eradicate _yellow_ lines from images. Due to this constraint, image masks can be generated automatically to detect yellow lines to be inpainted over.

## Technologies Used
- numpy
- Pillow

[Python version used == 3.7]

## Sample Results

| Initial image               | Inpainted image               |
| :-------------------------: | :---------------------------: |
| [![][im1_in_thumb]][im1_in] | [![][im1_out_thumb]][im1_out] |
| [![][im2_in_thumb]][im2_in] | [![][im2_out_thumb]][im2_out] |

[im1_in]: https://raw.github.com/Pushkar-Bhuse/ImageInpainting/master/blob/raw_image1.png
[im1_in_thumb]: https://raw.github.com/Pushkar-Bhuse/ImageInpainting/master/blob/raw_image1.png
[im1_out]: https://raw.github.com/Pushkar-Bhuse/ImageInpainting/master/blob/inpainted1.png
[im1_out_thumb]: https://raw.github.com/Pushkar-Bhuse/ImageInpainting/master/blob/inpainted1.png
[im2_in]: https://raw.github.com/Pushkar-Bhuse/ImageInpainting/master/blob/raw_image2.png
[im2_in_thumb]: https://raw.github.com/Pushkar-Bhuse/ImageInpainting/master/blob/raw_image2.png
[im2_out]: https://raw.github.com/Pushkar-Bhuse/ImageInpainting/master/blob/inpainted2.png
[im2_out_thumb]: https://raw.github.com/Pushkar-Bhuse/ImageInpainting/master/blob/inpainted2.png


## Instructions to Run
In order to access the API hosted as a serverless **AWS Lambda Function**, run the following command.
```
python api_access.py
```
**NOTE:** Before running this file, do not forget to add the source and desitation path of raw image and inpainted image respectively (Images have to be in PNG format).
