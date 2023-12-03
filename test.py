import cv2
import cv2
import numpy as np

if __name__ == '__main__':

    img = cv2.imread("./resources/map_origin.jpg")
    (h, w, _) = img.shape
    mid_h = int((max(h, w) - h) / 2)
    mid_w = int((max(h, w) - w) / 2)
    img = cv2.copyMakeBorder(img, mid_h, mid_h, mid_w, mid_w, cv2.BORDER_CONSTANT, value=[0, 0, 0])
    print(img.shape)
    # 切割出六个方向的图片

    left = np.zeros((2048, 2048), dtype=np.uint8)
    right = np.zeros((2048, 2048), dtype=np.uint8)
    back = np.zeros((2048, 2048), dtype=np.uint8)
    up = np.zeros((2048, 2048), dtype=np.uint8)
    down = np.zeros((2048, 2048), dtype=np.uint8)


    cv2.imwrite("./BackGround/map/up.png", up)
    cv2.imwrite("./BackGround/map/down.png", down)
    cv2.imwrite("./BackGround/map/left.png", left)
    cv2.imwrite("./BackGround/map/right.png", right)
    cv2.imwrite("./BackGround/map/front.png", img)
    cv2.imwrite("./BackGround/map/back.png", back)