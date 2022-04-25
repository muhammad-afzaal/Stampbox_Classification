import cv2


# https://www.youtube.com/watch?v=ADV-AjAXHdc&list=PL2VXyKi-KpYuTAZz__9KVl1jQz74bDG7i&index=4&ab_channel=PythonTutorialsforDigitalHumanities
# https://www.youtube.com/watch?v=y1ZrOs9s2QA&ab_channel=Murtaza%27sWorkshop-RoboticsandAI

def resizing(image_param):
    img = cv2.imread(image_param, cv2.IMREAD_UNCHANGED)

    # print('Original Dimensions : ', img.shape)

    scale_percent = 500  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    # print('Resized Dimensions : ', resized.shape)

    make_gray(image_path=image_param)


def noise_removal(image):
    import numpy as np
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return image


def make_gray(**kwargs):
    image = cv2.imread(kwargs['image_path'])
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    cv2.imwrite(r"temp/gray_index.jpg", gray)
    blur = cv2.GaussianBlur(gray, (7, 7), 0)
    cv2.imwrite(r"temp/gray_blur.jpg", blur)
    thresh = cv2.threshold(blur, 0, 225, cv2.THRESH_BINARY + cv2.THRESH_BINARY_INV)[1]
    cv2.imwrite(r"temp/gray_blur_thresh.jpg", thresh)
    thresh = cv2.threshold(gray, 0, 225, cv2.THRESH_BINARY + cv2.THRESH_BINARY_INV)[1]
    cv2.imwrite(r"temp/gray_thresh.jpg", thresh)
    inverted_img = cv2.bitwise_not(image)
    cv2.imwrite(r"temp/inverted.jpg", inverted_img)
    gray_inverted_img = cv2.bitwise_not(gray)
    cv2.imwrite(r"temp/gray_inverted.jpg", gray_inverted_img)

    thresh_2, imbw = cv2.threshold(gray, 130, 300, cv2.THRESH_BINARY)
    cv2.imwrite(r"temp/gray_bw.jpg", imbw)

    no_noise_gray_inverted = noise_removal(gray_inverted_img)
    cv2.imwrite(r"temp/gray_inverted_no_noise.jpg", no_noise_gray_inverted)

    no_noise_inverted = noise_removal(inverted_img)
    cv2.imwrite(r"temp/no_noise_inverted.jpg", no_noise_inverted)

    # return gray


if __name__ == '__main__':
    image_path = r'C:\Users\pixarsart\PycharmProjects\StampBox Classifications\Images\Stamps_images\Untitled design (5).png'
    # make_gray(image_path=image_path)
    resizing(image_param=image_path)

