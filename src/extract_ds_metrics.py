#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 22:57:03 2019

@author: danielogenrwot
"""

from __future__ import print_function
import os
import pandas as pd
import re
import csv

def read_original_data(data_path, metrics, file_extension = '.xlsx'):
    # Import the data using the file path
    header = ['FullClassPath', 'Class', 'DIT', 'IR', 'LCOM5', 'McCabe', 'MultipleInterface', 'NAD', 
               'NMD', 'NOC', 'NOParam', 'NOTI', 'USELESS', 'WMC']
    filename = os.sep.join(data_path + [metrics[0] + '-rc.csv'])
    
    # write header
    f = open(filename, 'w')
    writer = csv.DictWriter(f, fieldnames=header)
    writer.writeheader()
    f.close()
    
    list_classpath = []
    
    for metric in metrics:
        filepath = os.sep.join(data_path + [metric + file_extension])
        data = pd.read_excel(filepath, header=None)
        
        #print(data.shape[0])
        print(header)
        
        # get class names
        for i in range(0, data.shape[0]-1):
            row = data.iloc[i, 0]
            str1 = re.split('\s', row) # index of interest 3, 5, 7
            list_classpath.append(str1[3])
            #print(str1[3], str1[5], str1[7])
            
        # get unique class names
        list_unique_classpath = []
        for classpath in list_classpath:
            if classpath not in list_unique_classpath:
                list_unique_classpath.append(classpath)
        # print(len(list_unique_classname))
        # print(list_unique_classname)
        
        # reconstruct data
        list_row = []
        for j in range(0, len(list_unique_classpath)):
            set_flag = 0 
            for i in range(0, data.shape[0]-1):
                row = data.iloc[i, 0]
                str1 = re.split('\s', row) # index of interest 3, 5, 7
                if list_unique_classpath[j] == str1[3]:
                    if set_flag == 0:
                        list_row.insert(0, str1[3])
                        list_row.insert(1, str1[5])
                        list_row.insert(2, str1[7])
                        set_flag = 1
                    else:
                        list_row.append(str1[7])
            # print(list_row)
            write_csv_data(list_row)
            list_row.clear()

def write_csv_data(data, file_extension = '.csv'):
    # header = ['FullClassPath', 'Class', 'DIT', 'IR', 'LCOM5', 'McCabe', 'MultipleInterface', 'NAD', 
               #'NMD', 'NOC', 'NOParam', 'NOTI', 'USELESS', 'WMC']
    
    filename = os.sep.join(data_path + [metrics[0] + '-rc' + file_extension])
    
    # write the data
    with open(filename, 'a', newline ='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(i for i in data)

if __name__ == '__main__':
    
    data_path = ['DesignSmells']
    
    """metrics = ['Bitcoin-wallet-6.31/Metrics-Bitcoint-wallet',
           'K9/Metrics-K9',
           'Mars-simulation/Metrics-Mars-simulation',
           'SweetHome3Dv5.6_new/Metrics-SweetHome3D_new',
           'SweetHome3Dv5.6_old/Metrics']"""
    metrics = ['SweetHome3Dv5.6_new/Metrics-SweetHome3D_new']
    
    """
    DIT: Depth of inheritance tree of an entity. Uses a recursive algorithm to calculate it.
    IR: Inheritance ratio.
    LCOM5: Lack of cohesion in methods of an entity.
    McCabe: McCabe Complexity: Number of points of decision + 1
    MultipleInterface: If a class implements more than one interface.
    NAD: Number of attributes declared by an entity.
    NMD: Number of methods declared by an entity.
    NOC: Number of children of an entity.
    NOParam: Maximum number of parameters of the methods of an entity.
    NOTI: Highest number of transitive invocation among methods of a class. See the Law of Demeter for a definition.
    USELESS: Same value for any entity: 1.
    WMC: Weight of an entity as the number of method invocations in each method. (Default constructors are considered even if not explicitly declared.).
    """
    
    # read_original_data(data_path, metrics)
    # write_csv_data(data_path)