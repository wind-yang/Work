from __future__ import print_function
from __future__ import division
import os
import argparse
import numpy as np

# 把标签文件.tif换成.png
def name_img2gt(img_name):
    gt_name = img_name.replace('.tif', '.png')
    return gt_name

# 参数：训练集占比、验证集占比、预测集占比、图片路径、标签路径
def data_split(train_rate, val_rate, test_rate, img_dir, gt_dir):
    assert train_rate + val_rate + test_rate == 1, print('rate error!')

    files_list = os.listdir(img_dir)
    np.random.shuffle(files_list)
    total_num = len(files_list)
    train_num = int(total_num * train_rate)
    val_num = total_num - train_num if test_rate == 0 else int(total_num * val_rate)
    test_num = total_num - train_num - val_num

    data_dict = {}
    data_dict['train'] = files_list[:train_num]
    data_dict['val'] = files_list[train_num:train_num + val_num]
    data_dict['test'] = files_list[train_num + val_num:]

    # 生成train.txt、val.txt、test.txt
    save_dir = os.path.dirname(img_dir) # 去掉文件名，返回目录
    img_dir_name = os.path.basename(img_dir) # 获取文件名，不包含目录部分
    gt_dir_name = os.path.basename(gt_dir)
    for k, v in data_dict.items():
        split_txt_path = os.path.join(save_dir, k + '.txt')
        with open(split_txt_path, "w+") as f:
            for img_name in v:
                write_str = '%s %s\n' % (
                os.path.join(img_dir_name, img_name), os.path.join(gt_dir_name, name_img2gt(img_name)))
                f.write(write_str)

    print('total %d, split: train %d - %.2f rate, val %d - %.2f rate, test %d - %.2f rate' % (
    total_num, train_num, train_rate, val_num, val_rate, test_num, test_rate))


def get_args():
    parser = argparse.ArgumentParser(description='paramters')

    parser.add_argument('train_rate', type=float, help='train_rate')
    parser.add_argument('val_rate', type=float, help='val_rate')
    parser.add_argument('test_rate', type=float, help='test_rate')
    parser.add_argument('img_dir', type=str, help='img_dir')
    parser.add_argument('gt_dir', type=str, help='gt_dir')

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args()
    data_split(args.train_rate, args.val_rate, args.test_rate, args.img_dir, args.gt_dir)