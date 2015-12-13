# -*- coding: utf-8 -*-
"""
@author: Jiahe Li
"""

from numpy import *

class assignment2:
    def __init__(self):
        """
            To finish the fitting
        """
        self.data_mat, self.label_mat = self.LoadDataSet("trainingdata.txt")
#        print self.data_mat
#        print self.label_mat
        self.theta = self.NewtonMethod(10)
        self.PlotBestFit(array(self.theta))

    def LoadDataSet(self, data_file_name):
        """
            Read the data set from file
                input:
                    data_file_name          the filename of samplesets
                
                output:
                    data_mat                the cordinations of each sample
                    label_mat               the label of each sample
        """
        data_mat = []
        label_mat = []
        fr = open(data_file_name)
        for line in fr:
            line_arr = line.strip().split()
            data_mat.append([1.0, float(line_arr[0]), float(line_arr[1])])
            label_mat.append(float(line_arr[2]))
        fr.close()
        return data_mat, label_mat
    
    def Sigmoid(self, x):
        """
            The sigmod functoin
                input:
                    x               the variable
                    
                output:
                    the result of the sigmoid function
        """
        return 1.0 / (1+math.exp(-x))

    def NewtonMethod(self, iter_num=10):
        """
            The method of Newton
                input:
                    inter_num           the label to continue the iteration
                
                output:
                    m                   the number of training data set
                    n                   the number of the dimensions
        """
        m = len(self.data_mat)
        n = len(self.data_mat[0])
        theta = [0.0] * n

        while(iter_num):
            gradient_sum = [0.0] * n
            hessian_mat_sum = [[0.0] * n]*n
            for i in range(m):
                try:
                    hypothesis = self.Sigmoid(self.ComputeDotProduct(self.data_mat[i], theta))
                except:
                    continue
                error = self.label_mat[i] - hypothesis
                gradient = self.ComputeTimesVect(self.data_mat[i], error/m)
                gradient_sum = self.ComputeVectPlus(gradient_sum, gradient)
                hessian = self.ComputeHessianMatrix(self.data_mat[i], hypothesis/m)
                for j in range(n):
                    hessian_mat_sum[j] = self.ComputeVectPlus(hessian_mat_sum[j], hessian[j])
    
        #compute the matrix Hessian to check, if not right to ignore this iteration
            try:
                hessian_mat_inv = mat(hessian_mat_sum).I.tolist()
            except:
                print 'Something is wrong!'
                continue
            for k in range(n):
                theta[k] -= self.ComputeDotProduct(hessian_mat_inv[k], gradient_sum)

            iter_num -= 1
        return theta

    def ComputeHessianMatrix(self, data, hypothesis):
        """
            Caculate the value the matrix Hessian
                input:
                    data            the particular one sample
                    hypothesis      the result of Hypothesis function

                output:
                    hessian_matrix  the matrix hessian
        """
        hessian_matrix = []
        n = len(data)
        for i in range(n):
            row = []
            for j in range(n):
                row.append(-data[i]*data[j]*(1-hypothesis)*hypothesis)
            hessian_matrix.append(row)
        return hessian_matrix

    def ComputeDotProduct(self, a, b):
        """
            Compute the '.' of the vectors
                input:
                    a               the first vector
                    b               the second vector
                
                output:
                    dot_product     the result of method .
        """
        if len(a) != len(b):
            return False
        n = len(a)
        dot_product = 0
        for i in range(n):
            dot_product += a[i] * b[i]
        return dot_product
    
    def ComputeVectPlus(self, a, b):
        """
            Compute the sum of two vectors
                input:
                    a               the first vector
                    b               the second vector
                
                output:
                    sum             the result of method +
        """
        if len(a) != len(b):
            return False
        n = len(a)
        sum = []
        for i in range(n):
            sum.append(a[i]+b[i])
        return sum
    
    def ComputeTimesVect(self, vect, n):
        """
            Compute the n times of the vector
                input:
                    vect                the vector
                    n                   the times
                
                output:
                    n_times_vect        the result of method *
        """
        n_times_vect = []
        for i in range(len(vect)):
            n_times_vect.append(n * vect[i])
        return n_times_vect

    def PlotBestFit(self, weights):
        """
            Fit the best one
                input:
                    weights       the weights of theta      
        """
        import matplotlib.pyplot as plt
        data_arr = array(self.data_mat)
        n = shape(data_arr)[0]
        xcord1 = []
        ycord1 = []
        xcord2 = []
        ycord2 = []
        for i in range(n):
            if int(self.label_mat[i])== 1:
                xcord1.append(data_arr[i,1])
                ycord1.append(data_arr[i,2])
            else:
                xcord2.append(data_arr[i,1])
                ycord2.append(data_arr[i,2])
        x = arange(10.0, 65.0, 0.1)
        y = (-weights[0]-weights[1]*x)/weights[2]
        plt.plot(xcord1, ycord1, 'ro', xcord2, ycord2, 'g^', x, y)
        plt.xlabel('X1')
        plt.ylabel('X2')
        plt.show()

test = assignment2()