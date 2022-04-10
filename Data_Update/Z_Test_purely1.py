# -*- coding: utf-8 -*-

import os
import yaml

# Replica_list=[]
# replicaCount_list=[]
#
# with open (r'C:\Users\lxi\OneDrive - Sigma Technology\Desktop\vpn_eric-pc-controller-1.45.13-6\eric-pc-controller-1.45.13-6\eric-pc-controller\charts\eric-pc-vpn-gw\values.yaml') as file:
#     data = yaml.safe_load(file)
#     temp_value = data
#
#     while temp_value is not None:
#         try:
#             for key in temp_value:
#                 if isinstance(temp_value, dict):
#                     if 'replicas' in temp_value:
#                         Replica_list.append(temp_value['replicas'])
#                     if 'replicaCount' in temp_value:
#                         replicaCount_list.append(temp_value['replicaCount'])
#                     temp_value = temp_value[key]
#                 else:
#                     pass
#         except:
#             temp_value = None
#
#         return temp_value
#


def break_loop():
    for i in range(1,5):
        if i == 2:
            return (2)
        print (i)
    return (5)

break_loop()

# def add (a,b):
#     i=10
#     while i>0:
#         try:
#             c = a + b
#             add (c,i)
#             i = i - 1
#         except:
#             i=5
# add(0,1)

