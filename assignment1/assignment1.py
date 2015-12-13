# -*- coding: utf-8 -*-
"""
@author: Jiahe Li
"""

import numpy as np
import matplotlib.pyplot as plt

class assignment1:
    def __init__(self, number_of_nodes):
        """
        To get the data ininial:
            input:
                number_of_nodes         the number inputted
                
            kernel:
                NumberOfNodes           the number of the data
                XLabel                  the horizontal ordinate
                YLabel                  the longitudinal coordinate
                np.sin                  the Function Sine()
                seita                   the parameter of the hypothesis Func
                step                    the length of each step
        """
        self.NumberOfNodes = number_of_nodes
        self.XLabel = np.arange(0, np.pi*2, np.pi*2/self.NumberOfNodes)
        self.YLabel = list()
        for i in xrange(self.NumberOfNodes):
            self.YLabel.append(np.sin( self.XLabel[i] ))
        self.seita = np.array([0.,0.,0.,0.,0.,0.,0.,0.,0.])
        self.step = 0.01
        self.FitFunction()

    def ComputeCost(self):
        """
            To compute the loss value or error value
        """
        cost = 0
        for i in xrange(self.NumberOfNodes):
            temp_h = self.Hypothesis(i)
            temp_y = self.YLabel[i]
            cost += (temp_h - temp_y)*(temp_h - temp_y)/2.0
        return cost

    def HandleStep(self):
        """
            Justise the value of the step with the condition of cost
        """
        temp_seita = self.NextSeita()
        while True:
            print self.seita
            temp = self.seita
            cost_first = self.ComputeCost()
            self.seita = self.seita - temp_seita*self.step/self.NumberOfNodes
            cost_second = self.ComputeCost()
            if cost_second - cost_first > 0:
                self.seita = temp
                self.step -= 0.000001
            else:
                break

    def NextSeita(self):
        """
            To get the next seita
        """
        temp_seita = np.array([0.,0.,0.,0.,0.,0.,0.,0.,0.])
        for j in xrange(self.NumberOfNodes):
            temp_h = self.Hypothesis(j)
            temp_y = self.YLabel[j]
            temp_x = self.XLabel[j]
            for i in xrange(len(temp_seita)):
                temp_seita[i] += (temp_h - temp_y)*np.power(temp_x, i)
        return temp_seita

    def Hypothesis(self, index):
        """
            To caculate the value of the function with index:
                index           the position of the data
        """
        temp_result = 0
        for i in xrange(len(self.seita)):
            temp_result += self.seita[i]*np.power(self.XLabel[index], i)
        return temp_result

    def DrawPlt(self, title, style):
        """
            To draw the figure:
                plt         the content need be plotted
                title       the title of the figure
        """
        plt.plot(self.XLabel, self.YLabel, style)
        plt.xlabel = 'x'
        plt.ylabel = 'y'
        plt.title = title
        plt.show()

    def Delta(self, temp_seita):
        """
            To caculate the difference between each seita with the source seita
                output:
                    np.sqrt(delta)          the difference between the two seitas
        """
        delta = 0
        for i in xrange(len(self.seita)):
            delta += (temp_seita[i]-self.seita[i])*(temp_seita[i]-self.seita[i])
        return np.sqrt(delta)

    def Push(self, store_seita):
        """
            To push the new seita into the tail of the store_seita
        """
        for i in xrange(1,20):
            store_seita[i-1] = store_seita[i]
        store_seita[19] = self.seita

    def FitFunction(self):
        """
            To fit the Sine() with multi-way
        """
        store_seita = list()
        store_seita.append(self.seita)
        i = 1
        while i < 20:
            self.HandleStep()
            store_seita.append(self.seita)
            i += 1

        while self.Delta(store_seita[0]) > 0.00000001:
            self.HandleStep()
            self.Push(store_seita)
#        self.NextSeita()
        h_label = list()
        for i in xrange(self.NumberOfNodes):
            h_label.append(self.Hypothesis(i))

        plt.figure(1)
        plt.subplot(211)
        plt.plot(self.XLabel, h_label, 'g^')
        plt.axis([0.,2*np.pi,-1.5,1.5])
        plt.subplot(212)
        plt.axis([0.,2*np.pi,-1.5,1.5])
        self.DrawPlt('Divided', 'ro')

        plt.figure(2)
        plt.plot(self.XLabel, self.YLabel, 'r', self.XLabel, h_label, 'g')
        plt.title = 'The joint condition!'
        plt.xlabel = 'x'
        plt.ylabel = 'y'
        plt.axis([0.,2*np.pi,-1.5,1.5])
        plt.show()
#        print h_label

test = assignment1(20)
