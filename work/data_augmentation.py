from PIL import Image, ImageFilter, ImageDraw, ImageEnhance
import random
import os
import numpy as np
from tqdm import tqdm


# 读取路径下图片的名称
def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            img_name = os.path.split(file)[1]
            img_name = img_name.split('.')[0]
            L.append(img_name)

    return L

def rotate_90(img, label):
    # 图像和标签同时进行90旋转
    img = img.rotate(90)
    label = label.rotate(90)
    return img, label

def rotate_180(img, label):
    # 图像和标签同时进行180旋转
    img = img.rotate(180)
    label = label.rotate(180)
    return img,label

def rotate_270(img, label):
    # 图像和标签同时进行90，180，270旋转
    img = img.rotate(270)
    label = label.rotate(270)
    return img,label

def flip_horizontal(img, label):
    # 图像和标签同时进行水平翻转
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    label = label.transpose(Image.FLIP_LEFT_RIGHT)
    return img, label

def flip_vertical(img, label):
    # 图像和标签同时进行垂直翻转
    img = img.transpose(Image.FLIP_TOP_BOTTOM)
    label = label.transpose(Image.FLIP_TOP_BOTTOM)
    return img, label

# image_num：增广之后的图片数据
def creat_dataset(image_path,label_path):
    image_sets = file_name(img_path)  # 图片存储路径
    label_sets = file_name(label_path)  # 标签存储路径

    for i in range(len(image_sets)):
        img = Image.open(img_path + image_sets[i] +'.tif')  # 3 channels
        label = Image.open(label_path + label_sets[i] + '.png')  # 3 channels

        img_1,label_1 = rotate_90(img,label)
        img_2, label_2 = rotate_180(img, label)
        img_3, label_3 = rotate_270(img, label)
        img_4, label_4 = flip_horizontal(img, label)
        img_5, label_5 = flip_vertical(img, label)

        img.save('E:/DLRSD_augment/image/{}.tif'.format(image_sets[i] + '_origin'))
        label.save('E:/DLRSD_augment/gt/{}.png'.format(image_sets[i] + '_origin'))
        img_1.save('E:/DLRSD_augment/image/{}.tif'.format(image_sets[i] + '_r90'))
        label_1.save('E:/DLRSD_augment/gt/{}.png'.format(image_sets[i] + '_r90'))
        img_2.save('E:/DLRSD_augment/image/{}.tif'.format(image_sets[i] + '_r180'))
        label_2.save('E:/DLRSD_augment/gt/{}.png'.format(image_sets[i] + '_r180'))
        img_3.save('E:/DLRSD_augment/image/{}.tif'.format(image_sets[i] + '_r270'))
        label_3.save('E:/DLRSD_augment/gt/{}.png'.format(image_sets[i] + '_r270'))
        img_4.save('E:/DLRSD_augment/image/{}.tif'.format(image_sets[i] + '_fh'))
        label_4.save('E:/DLRSD_augment/gt/{}.png'.format(image_sets[i] + '_fh'))
        img_5.save('E:/DLRSD_augment/image/{}.tif'.format(image_sets[i] + '_fv'))
        label_5.save('E:/DLRSD_augment/gt/{}.png'.format(image_sets[i] + '_fv'))
        print("{} is saved successfully".format(image_sets[i]))



img_path = 'E:/pycharm_project/remote_image_DLRSD/PaddleSeg/dataset/dlrsd/image/'
label_path = 'E:/pycharm_project/remote_image_DLRSD/PaddleSeg/dataset/dlrsd/gt/'
creat_dataset(img_path,label_path)



