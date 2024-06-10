from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image_path = 'C:\\Users\\user\\OneDrive\\Desktop\\test.png'
image = np.array(Image.open(image_path).convert('L'))

def convolve2d(image, kernel):
    kernel_height, kernel_width = kernel.shape
    image_height, image_width = image.shape
    output_height, output_width = image_height - kernel_height + 1, image_width - kernel_width + 1
    
    return np.array([
        [np.sum(image[i:i+kernel_height, j:j+kernel_width] * kernel) 
         for j in range(output_width)] 
        for i in range(output_height)
    ])

sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

edges_x = convolve2d(image, sobel_x)
edges_y = convolve2d(image, sobel_y)

edges = np.hypot(edges_x, edges_y)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.subplot(1, 2, 2)
plt.title('Edge Detection')
plt.imshow(edges, cmap='gray')
plt.show()


output_path = 'C:\\Users\\user\\OneDrive\\Desktop\\New folder\\edges.png'
Image.fromarray(edges.astype(np.uint8)).save(output_path)
print(f"{output_path}")
