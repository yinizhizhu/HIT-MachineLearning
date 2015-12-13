# Assignment4
实现的是二维降为一维的pca。

利用了D,V= np.linalg.eig(sigma)来计算协方差矩阵的特征向量，且V的实数部分才是的列向量是我们所寻找的特征向量。