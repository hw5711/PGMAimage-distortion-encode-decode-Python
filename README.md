# PGMAimage-distortion-encode-decode-Python
multimedia image decode&amp;encode



Use the Baboon image from assignment 1 (available in the resources section of TRACS) and the instructions for reading/writing PGMA images from TRACS.
1. Read the image, convert it from 256 gray levels to 12-gray levels, and write the 12-gray level image as a pgma image. Note that this is equivalent to uniform quantization. You can use other images from TRACS for further testing.
2. Read the image, convert it from 256 gray levels to 2-gray levels, and write the 2-gray level image as a pgma image. Note that this is equivalent to uniform quantization. You can use other images from TRACS for further testing.

In specific:

a. Emulate the encoder and produce a pgma image where the value of pixel 𝑝̂ in the encoded 𝑖,𝑗
image is the quantized value of the pixel 𝑝𝑖,𝑗in the original image.

b. Generate the decoder output; that is the reconstructed image (in pgma format); where pixel
𝑝̃ of the reconstructed image assumes the reconstructed value that corresponds to the 𝑖,𝑗
original pixel vale.

c. Calculate the distortion introduced and find the rate.
i. The distortion is the mean square error. That is, the average of the pixel-wise square differences between the original image and the reconstructed image.

d. Produce the error image – the error image is obtained by the pixel-wise absolute difference
between the original image (i.e., the set of pixels 𝑝𝑖,𝑗) and the reconstructed image (i.e., the
set of pixels 𝑝̃ ). That is, pixel (𝑖, 𝑗) of the error image (say 𝑒 ) is the absolute difference 𝑖,𝑗 𝑖,𝑗
between pixel 𝑝 (from the original image) and pixel 𝑝̃ (from the reconstructed image). 𝑖,𝑗 𝑖,𝑗
Please note that the pgma error image must include the actual maximum gray level of image pixels in the header.
