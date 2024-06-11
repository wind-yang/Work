from __future__ import print_function
from __future__ import division

import os
import shutil
import argparse
from tqdm import tqdm

def image_move(src_path, dst_path):
    print('copy from %s to %s:'%(src_path,dst_path))
    if not os.path.exists(dst_path):
        os.makedirs(dst_path)
    sub_dirs = os.listdir(src_path)
    for sub_dir in sub_dirs:
        sub_path = os.path.join(src_path,sub_dir)
        if os.path.isdir(sub_path):
            for file_name in os.listdir(sub_path):
                src_file_path = os.path.join(sub_path,file_name)
                dst_file_path = os.path.join(dst_path,file_name)
                if os.path.exists(dst_file_path):
                    pass
                else:
                    shutil.copy(src_file_path,dst_file_path)
            print('%s finish'%sub_dir)

def get_args():
    parser = argparse.ArgumentParser(description='paramters')

    parser.add_argument('src_path', type=str,help='copy from path')
    parser.add_argument('dst_path', type=str,help='copy to path')

    args = parser.parse_args()
    return args
if __name__ == '__main__':
    args = get_args()
    image_move(args.src_path,args.dst_path)







