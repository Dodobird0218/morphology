import numpy as np
import cv2


class image:
    img0 = cv2.imread("1.bmp", cv2.IMREAD_GRAYSCALE)
    img1 = cv2.imread("2.png", cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread("3.png", cv2.IMREAD_GRAYSCALE)
    img3 = cv2.imread("4.bmp", cv2.IMREAD_GRAYSCALE)


def img0result():
    kernel = np.ones((7, 7), np.uint8)
    erosion = cv2.erode(image.img0, kernel, iterations=2)
    result = cv2.dilate(erosion, kernel, iterations=2)
    cv2.imshow("origin", image.img0)
    cv2.imshow("result", result)
    cv2.waitKey(0)


def img1result():
    kernel = np.ones((9, 1), np.uint8)
    kernel1 = np.ones((3, 3), np.uint8)
    k = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 3))
    k1 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    erosion = cv2.erode(image.img1, kernel, iterations=3)
    opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, k, iterations=3)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, k, iterations=3)
    erosion1 = cv2.erode(closing, kernel1, iterations=3)
    dilate = cv2.dilate(erosion1, kernel1, iterations=2)
    closing1 = cv2.morphologyEx(dilate, cv2.MORPH_CLOSE, k1, iterations=3)
    cv2.imshow("origin", image.img1)
    cv2.imshow("result", closing1)
    cv2.waitKey(0)


def img3result():
    median_blur = cv2.medianBlur(image.img2, 33)
    cv2.imshow("origin", image.img2)
    cv2.imshow("result", median_blur)
    cv2.waitKey(0)


def img4result():
    kernel = np.ones((7, 7), np.uint8)
    kernel1 = np.ones((7, 1), np.uint8)
    kernel2 = np.ones((1, 7), np.uint8)

    k = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))

    dilate = cv2.dilate(image.img3, kernel, iterations=10)
    erosion = cv2.erode(dilate, kernel, iterations=10)
    dilate1 = cv2.dilate(erosion, kernel1, iterations=20)
    erosion1 = cv2.erode(dilate1, kernel1, iterations=20)
    erosion2 = cv2.erode(erosion1, kernel2, iterations=20)
    dilate2 = cv2.dilate(erosion2, kernel2, iterations=20)

    cv2.imshow("origin", image.img3)
    cv2.imshow("result", dilate2)
    cv2.waitKey(0)


if __name__ == "__main__":
    # img0result()
    # img1result()
    # img2result()
    img4result()
