# -*- coding: utf-8 -*-
"""
Author: Jiahe Li
"""

import numpy as np
import matplotlib.pyplot as plt
from string import atof

class assignment4:
    def __init__(self):
        """
            Let some varaible initial.
        """
        self.XLabel = list()
        self.YLabel = list()
        self.phi = [0., 0.]
        self.LoadDataSet()
        self.Pca()
        
    def LoadDataSet(self):
        """
            Load dataset from file:(From matlab)
mu1 = [-2 1];
SIGMA1 = [1 0;0 8];
SIGMA1 = [cos(pi/3) -sin(pi/3);sin(pi/3) cos(pi/3)]*SIGMA1*[cos(pi/3) sin(pi/3);-sin(pi/3) cos(pi/3)];
tr1 = mvnrnd(mu1,SIGMA1,100);
        """
        data_set = open('data.txt', 'r')
        for line in data_set.readlines():
            data_line = line.strip().split()
            temp_x = atof(data_line[0])
            temp_y = atof(data_line[1])
            self.phi[0] += temp_x
            self.phi[1] += temp_y
            self.XLabel.append(temp_x)
            self.YLabel.append(temp_y)
        self.phi[0] = self.phi[0]/100.0
        self.phi[1] = self.phi[1]/100.0
        data_set.close()
    
    def Transpose(self, matrix):
        """
            Get the transpose matrix
        """
        temp = list()
        for i in xrange(len(matrix[0])):
            temp.append(list())
            for j in xrange(len(matrix)):
                temp[i].append(matrix[j][i])
        return temp

    def Print(self, vector):
        """
            Print the vector to help me debug
        """
        for i in xrange(len(vector)):
            print vector[i]

    def Pca(self):
        """
            Just let two demensions downto one demension
        """
        temp_x = list()
        for i in xrange(100):
            temp_x.append([ self.XLabel[i]-self.phi[0], self.YLabel[i]-self.phi[1] ])
        temp_x_ = self.Transpose(temp_x)
        sigma = np.dot(temp_x_, temp_x)
        D,V= np.linalg.eig(sigma)
        
        for i in xrange(2):
            for j in xrange(2):
                V.real[i][j] *= -1
                
        temp_v_ = self.Transpose(V.real)
        
        tr1 = list()
        tr1.append(self.XLabel)
        tr1.append(self.YLabel)
        tr1 = self.Transpose(tr1)
        
        xr1 = np.dot(tr1, temp_v_[0])
        xr2 = np.dot(self.phi, temp_v_[1])
        
        xr = tr1
#        print xr
        for i in xrange(len(self.XLabel)):
            xr[i][0] = np.dot(xr1[i], V.real[0][0])+np.dot(xr2, V.real[0][1])
            xr[i][1] = np.dot(xr1[i], V.real[1][0])+np.dot(xr2, V.real[1][1])
#        print xr

        plt.plot(self.XLabel, self.YLabel, 'r+')
        temp_xr = self.Transpose(xr)
        plt.plot(temp_xr[0], temp_xr[1], 'b*')
        for i in xrange(len(self.XLabel)):
            plt.plot([self.XLabel[i],xr[i][0]], [self.YLabel[i],xr[i][1]])
        plt.axis([-8,6,-5,5])
        plt.xlabel = 'x'
        plt.ylabel = 'y'
        plt.show()

test = assignment4()
