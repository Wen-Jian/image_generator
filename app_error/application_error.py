import cv2
import numpy as np
import os
import sys
import glob
sys.path.append(os.path.join(os.getcwd(), 'lib'))
import create_mnist_jpg as im_creator
import basic_dnn as dnn
import tensorflow as tf

img_file_path = os.path.join(os.getcwd(),'MnistImage/Train')


dataset = im_creator.img_to_data_set(img_file_path)

dnn.train(np.array(dataset, np.float32), im_creator.labels().astype(np.float32))


