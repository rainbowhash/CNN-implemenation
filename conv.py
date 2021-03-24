# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:12:08 2021

@author: k20104661
"""
import numpy as np

class conv3x3:
    def __init__(self,num_filters):
        self.num_filters=num_filters
        self.filter_size=3

        # filter is a 3x3 3d nump array 
        # we divide by 9 based on xavier initilization to make it 
        self.filters=np.random.rand(num_filters,self.filter_size,self.filter_size)/9
        
    def generate_regions(self,image):
        # generator function that genrates the regions for convling 
        # Input = Image
        # output = Regions
        h,w=image.shape()
        for i in range(h-2):
            for j in range(w-2):
                image_region=image[i:i+self.filter_size,j:j+self.filter_size]
                yield image_region , i, j
    
    def forward_pass(self,image):
        # method does the convolition of image and the filter and genreates 
        # the sequence of output
        # Input = Image
        # Output = Sequence of convoled output images
        
        h,w=image.shape()
        output=np.zeros((h-self.filter_size)+1,(w-self.filter_size)+1,self.num_filters)
        for region,i,j in self.generate_regions(image):
            output[i,j]=np.sum(region*self.filters,axis=(1,2))
            