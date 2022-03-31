# -*- coding:gbk -*-

import os
import cv2
import numpy as np
#from sklearn.cross_validation import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

#----------------------------------------------------------------------------------
# ��һ�� �з�ѵ�����Ͳ��Լ�
#----------------------------------------------------------------------------------

X = [] #����ͼ������
Y = [] #����ͼ��������
Z = [] #����ͼ������

for i in range(0, 10):
    #�����ļ��У���ȡͼƬ
    for f in os.listdir("data/%s" % i):
        #��ȡͼ������
        X.append("data//" +str(i) + "//" + str(f))
        #��ȡͼ����꼴Ϊ�ļ�������
        Y.append(i)

X = np.array(X)
Y = np.array(Y)

#�����Ϊ100% ѡȡ���е�30%��Ϊ���Լ�
X_train, X_test, y_train, y_test = train_test_split(X, Y,                                                   
test_size=0.3, random_state=1)

print (len(X_train), len(X_test), len(y_train), len(y_test))

#----------------------------------------------------------------------------------
# �ڶ��� ͼ���ȡ��ת��Ϊ����ֱ��ͼ
#----------------------------------------------------------------------------------

#ѵ����
XX_train = []
for i in X_train:
    #��ȡͼ��
    #print i
    image = cv2.imread(i)
    #img = cv2.imread(i)
    
    #ͼ�����ش�Сһ��
    img = cv2.resize(image, (256,256),
                     interpolation=cv2.INTER_CUBIC)

    #����ͼ��ֱ��ͼ���洢��X����
    hist = cv2.calcHist([img], [0,1], None,
                            [256,256], [0.0,255.0,0.0,255.0])

    XX_train.append(((hist/255).flatten()))

#���Լ�
XX_test = []
for i in X_test:
    #��ȡͼ��
    #print i
    image = cv2.imread(i)
    
    #ͼ�����ش�Сһ��
    img = cv2.resize(image, (256,256),
                     interpolation=cv2.INTER_CUBIC)

    #����ͼ��ֱ��ͼ���洢��X����
    hist = cv2.calcHist([img], [0,1], None,
                            [256,256], [0.0,255.0,0.0,255.0])

    XX_test.append(((hist/255).flatten()))

#----------------------------------------------------------------------------------
# ������ �������ر�Ҷ˹��ͼ����ദ��
#----------------------------------------------------------------------------------

from sklearn.naive_bayes import BernoulliNB
clf = BernoulliNB().fit(XX_train, y_train)
predictions_labels = clf.predict(XX_test)

print ('Ԥ����:')
print (predictions_labels)

print ('�㷨����:')
print (classification_report(y_test, predictions_labels))

#���ǰ10��ͼƬ��Ԥ����
k = 0
while k<10:
    #��ȡͼ��
    print (X_test[k])
    image = cv2.imread(X_test[k])
    print (predictions_labels[k])
    #��ʾͼ��
    cv2.imshow("img", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    k = k + 1

