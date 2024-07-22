import cv2
import matplotlib.pyplot as plt

bg1_image = cv2.imread('./public/images/GreenBackground.png', 1)
bg1_image = cv2.resize(bg1_image, (678, 381))

ob_image = cv2.imread('./public/images/Object.png', 1)
ob_image = cv2.resize(ob_image, (678, 381))

bg2_image = cv2.imread('./public/images/NewBackground.jpg', 1)
bg2_image = cv2.resize(bg2_image, (678, 381))


def compute_difference(bg_img, input_img):
    difference_single_channel = np.abs(bg_img - input_img)
    return difference_single_channel


difference_single_channel = compute_difference(bg1_image, ob_image)


# Display the images using matplotlib
def show_image(img, title):
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')


plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
show_image(bg1_image, 'Background Image 1')
plt.subplot(1, 3, 2)
show_image(ob_image, 'Object Image')
plt.subplot(1, 3, 3)
show_image(difference_single_channel, 'Difference Image')
plt.show()


def compute_binary_mask(difference_single_channel):
    # Áp dụng ngưỡng để tạo mask nhị phân
    _, binary_mask = cv2.threshold(
        difference_single_channel, 30, 255, cv2.THRESH_BINARY)

    # Áp dụng morphology để loại bỏ nhiễu
    kernel = np.ones((5, 5), np.uint8)
    binary_mask = cv2.morphologyEx(binary_mask, cv2.MORPH_OPEN, kernel)
    binary_mask = cv2.morphologyEx(binary_mask, cv2.MORPH_CLOSE, kernel)

    return binary_mask


def replace_background(bg1_img, bg2_img, ob_img):
    difference_single_channel = compute_difference(bg1_img, ob_img)
    binary_mask = compute_binary_mask(difference_single_channel)
    output = np.where(binary_mask == 255, ob_img, bg2_img)
    return output


# Replace the background
output_image = replace_background(bg1_image, bg2_image, ob_image)

# Display the result using matplotlib
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.title('Background Image 1')
plt.axis('off')
