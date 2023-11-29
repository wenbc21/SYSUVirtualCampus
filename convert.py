import os
import py360convert as sbwbc
import cv2
import glob
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("--size", required=False, type = int, default=1024,
                help="转化结果中每一张方形图片的边长")


def convertImage(folder_path, image_name, w):
    # 图片读取
    img = cv2.imread(folder_path + '/' + image_name)
    img_path = "./BackGround/" + image_name.split('.')[0]

    # 立方体贴图转环
    res = sbwbc.e2c(img, face_w=w, mode='bilinear', cube_format='dice')

    print("converting: " + image_name)

    # 切割出六个方向的图片
    left = res[w:w*2, 0:w, :]
    front = res[w:w*2, w:w*2, :]
    right = res[w:w*2, w*2:w*3, :]
    back = res[w:w*2, w*3:w*4, :]
    up = res[0:w, w:w*2, :]
    down = res[w*2:w*3, w:w*2, :]

    if not os.path.exists(img_path):
        os.makedirs(img_path)

    cv2.imwrite(img_path + "/up.png", up)
    cv2.imwrite(img_path + "/down.png", down)
    cv2.imwrite(img_path + "/left.png", left)
    cv2.imwrite(img_path + "/right.png", right)
    cv2.imwrite(img_path + "/front.png", front)
    cv2.imwrite(img_path + "/back.png", back)

if __name__ == '__main__':
    # 读取边长
    args = vars(ap.parse_args())
    w = args['size']

    # 读取文件夹中图片
    input_path = ".\\resources\\CV60"
    Image_name_list = os.listdir(input_path)

    # 逐张转换
    for image in Image_name_list:
        convertImage(input_path, image, w)

    print("save result in ./BackGround/")


