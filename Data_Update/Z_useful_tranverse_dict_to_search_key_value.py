# -*- coding: utf-8 -*-
import os
import yaml

#遍历字典去找寻某一个key的值，比如replic或replicaCount
# a = {'enabled': True, 'objectStorage': {'accessSecretName': 'eric-pc-gateway-obj-storage-secret'}, 'messageBus': {'msgSizeConfig': '6291456'},'productVersionConfigMap': {'name': 'eric-pc-gateway-version'}}

with open(r'C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-gateway-1.45.6-79\eric-pc-gateway-1.45.6-79\eric-pc-gateway\charts\eric-data-distributed-coordinator-ed\values.yaml') as file:
    data = yaml.safe_load(file)


def get_dict_allkeys(dict_a):
    key_list = []
    # 用instance检测a是否为字典
    if isinstance(dict_a,dict):
        for i in range(len(dict_a)):
            temp_key=list(dict_a.keys())[i]#将key转化为了一个list，再是list列表的第几个元素
            temp_value=dict_a[temp_key]
            key_list.append((temp_key))
            if temp_key == 'replicas' or temp_key == 'replicaCount':
                replica = temp_value
                print(temp_key)
                print(replica)
                # print(temp_value)
                # break
            get_dict_allkeys(temp_value)

    else:
        pass


get_dict_allkeys((data))

# for key in a:
#     # print (key)
#     print (a.items())
    # if key == 'objectStorage':
    #     print (dict.items())

# if __name__ == '__main__':
    # data="""{}"""
    # data1=json.loads(r'C:\XL\Sigma\Trainings\Python\Others\For_Liangrui_handle_json\bulk_report_1.json')
    # get_keys = get_dict_allkeys(data1)
    # print(get_keys)