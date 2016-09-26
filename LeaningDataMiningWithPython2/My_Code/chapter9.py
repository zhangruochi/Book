#-*-coding:utf8 -*-
from PIL import Image,ImageDraw,ImageFont #  创建验证码图片
from skimage import transform as tf  #错切变化
import numpy as np
from matplotlib import pyplot as plt

#创建验证码图片
def create_captcha(text,shear = 0, size = (100,24)):
    im = Image.new("L",size,color = "black")
    draw = ImageDraw.Draw(im)

    font = ImageFont.truetype(r"Coval.otf",15)
    draw.text((1,1),text,fill = 1,font = font)

    #将 PIL 图像转换为 numpy 数组 便于用 skimage 添加错且变化
    image_matrix = np.array(im)
    affine_tf = tf.AffineTransform(shear = shear)
    image_matrix = tf.warp(image_matrix,affine_tf)
    
    return image_matrix/ image_matrix.max() #对图像特征归一化

#显示图片
def show_image(image_matrix):
    plt.imshow(image_matrix,cmap="Greys")
    plt.show()


#将图像分割成单个单词
def segment_image(image_matrix):
    from skimage.measure import label,regionprops
    small_image_list = list()
    labeled_image = label(image_matrix)
    for region in regionprops(labeled_image):
        x_start,y_start,x_end,y_end = region.bbox
        small_image_list.append(image_matrix[x_start:x_end,y_start:y_end])

    if len(small_image_list) == 0:
        return [image_matrix,]    
    return small_image_list    

#先分割后的小图片显示出来
def show_segment_image(small_image_list):
    f,axes = plt.subplots(1,len(small_image_list),figsize = (10,3))
    for i in range(len(small_image_list)):
        axes[i].imshow(small_image_list[i],cmap='gray')
    plt.show()



def create_dataset():
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    shear_values = np.arange(0,0.5,0.05)
    #image,target = create_sample(letters,shear_values)
    dataset,labels = zip(*([create_sample(letters,shear_values) for i in range(3000)]))
    dataset = np.array(dataset)
    #show_image(dataset[111])    #检查随机数有没有问题
    #print(labels[111])
    labels = np.array(labels)
    # label 转换为onehot 编码
    from sklearn.preprocessing import OneHotEncoder
    enc = OneHotEncoder()
    labels = enc.fit_transform(labels.reshape(labels.shape[0],1)).todense()

    return dataset,labels

def create_sample(letters,shear_values,random_state_value = None):
    from sklearn.utils import check_random_state
    random_state = check_random_state(random_state_value)
    letter = random_state.choice(letters)
    shear_value = random_state.choice(shear_values)
    return create_captcha(letter,shear_value),letters.index(letter)

#将训练集中每个小图像化为20个像素 并且将训练集转化为2维度
def resize_dataset(dataset):
    from skimage.transform import resize
    dataset = np.array([resize(segment_image(image)[0],(20,20)) for image in dataset])
    # 此时 dataset 的数据是三维的[image1,image2......]  需要修改为二维
    X = dataset.reshape(dataset.shape[0],dataset.shape[1]*dataset.shape[2])
    return  X

#将数据集分为训练集和测试集
def split_dataset(X,labels):
    from sklearn.cross_validation import train_test_split
    X_train,X_test,y_train,y_test = train_test_split(X,labels,train_size = 0.9)
    return X_train,X_test,y_train,y_test


#PyBrain  使用自己的数据格式
def create_pybrain_dataset(X_train,X_test,y_train,y_test):
    from pybrain.datasets import  SupervisedDataSet
    training = SupervisedDataSet(X_train.shape[1],y_train.shape[1])
    for i in range(X_train.shape[0]):
        training.addSample(X_train[i],y_train[i])

    testing = SupervisedDataSet(X_test.shape[1],y_test.shape[1])
    for i in range(X_test.shape[0]):
        testing.addSample

    return training,testing

#创建神经网络  隐含层包含100个神经元
def create_brain_network(X,labels,training,testing):
    from pybrain.tools.shortcuts import buildNetwork
    net = buildNetwork(X.shape[1],100,labels.shape[1],bias = True)
    #利用反向传播算法修复错误输出
    from pybrain.supervised.trainers import BackpropTrainer
    trainer =BackpropTrainer(net,training,learningrate=0.01,weightdecay=0.01)
    #规定固定步数  不用等到完全收敛
    trainer.trainEpochs(epochs = 20)
    predictions = trainer.testOnClassData(dataset = testing)
    return predictions

def get_f1_score(predictions,y_test):
    from sklearn.metrics import f1_score
    print("F-score: {0}".format(f1_score(y_test,predictions)))






if __name__ == '__main__':
    dataset,labels = create_dataset()
    X = resize_dataset(dataset)
    X_train,X_test,y_train,y_test = split_dataset(X,labels)
    print(y_test.shape)
    training,testing = create_pybrain_dataset(X_train,X_test,y_train,y_test)
    predictions = create_brain_network(X,labels,training,testing)
    print(predictions)
    #predictions = get_f1_score(predictions,y_test)


    





