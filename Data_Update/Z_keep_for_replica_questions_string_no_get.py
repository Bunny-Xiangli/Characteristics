# -*- coding: utf-8 -*-

import os
import yaml
import pickle
# from docx import Document


from yaml.loader import SafeLoader # 这样写是什么意思？
import openpyxl

# folder_name = os.listdir(r'C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-gateway-1.44.0-1269\eric-pc-gateway-1.44.0-1269\eric-pc-gateway\charts')
#print (folder_name)


#wb = openpyxl.Workbook() #打开工作簿

#files = os.listdir(folder_name)

# f=open(r'C:/Users/lxi/OneDrive - Sigma Technology/Desktop/eric-pc-gateway-1.44.0-1269/eric-pc-gateway-1.44.0-1269/eric-pc-gateway\charts\eric-log-transformer\values.yaml','r')
# print (f.read())

# with open(r"C:/Users/lxi/OneDrive - Sigma Technology/Desktop/eric-pc-gateway-1.44.0-1269/eric-pc-gateway-1.44.0-1269/eric-pc-gateway\charts\eric-log-transformer\values.yaml") as file:
#     data = yaml.safe_load(file)
#     print (data)

# resources = data["resources"]
# resource = resources["logtransformer"]["requests"]
# a= resource["requests"]["cpu"]
# resource2 = resources["logtransformer"]["requests"]["cpu"]
# print (resource)

#data=f.read()
#print(data)
#f.close()

# ydata=yaml.safe_load(data) #把yaml文件读成了字典格式
# print (ydata)

#sheet1= wb.active #使用工作簿对象创建一张表

#sheet1 ['A1']= data

#wb.save('test.xlsx') # 关闭工作簿

#folder_name = os.listdir(r'C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-gateway-1.44.0-131\eric-pc-gateway-1.44.0-131\eric-pc-gateway\charts')


# doc = docx.Document(r'C:\Users\lxi\OneDrive - Sigma Technology\Desktop\test.docx')
# print (doc.paragraphs)





class Test ():

    def __init__(self,path,filename): # 起始，传参数进来，self代表着新建的实例对象
        self.path = path
        self.filename = filename

    def extract(self, absolutepath):  # 打开并读取yaml file，并调用process函数。data里存的是yaml file全文，比如Log Transformer全文
        with open(absolutepath) as file:
            data = yaml.safe_load(file)  # 读取yaml file，读取出来是嵌套的字典
            self.maybepodname(data)

    def maybepodname(self,data):
        podnamelist_PCG = []
        for everypodname in data: #得到的就是data里面的key值
            podnamelist_PCG.append(everypodname) #podnamelist_PCG，就是最后带有所有的podname的list
        # podnamelist_PCG.remove("tags")
        # podnamelist_PCG.remove("global")
        # podnamelist_PCG.remove("m2m")
        # podnamelist_PCG.remove("productInfoStatus")
        # podnamelist_PCG.remove("labels")
        # print(podnamelist_PCG) #podnamelist_PCG是个列表
        self.process(podnamelist_PCG,data)


    def getfile(self): # 得到values.yaml的绝对路径
        absolutepath = self.path + "/" + self.filename
        self.extract(absolutepath)

    def return_value(self,dictionary,levels):
        thedict = dictionary
        thelevel = levels[::-1] # 先把各个level翻转，比如["requests","cpu"]变成["cpu","requests"]
        while thelevel:
            try:
                thedict = thedict[thelevel.pop()] #一层一层弹出时，先弹出requests,对应的值也就是{'cpu': '250m', 'memory': '2Gi', 'ephemeral-storage': None}
            except:
                thedict = None
        return thedict

    # def find_keywords(self,data_len,podnamelist_PCG,data): #尝试把带有resources的关键词搜索出来
    #     queue = [data]
    #     while len(data) > 0:
    #         left_data = queue.pop()
    #         for key,value in left_data.items():


    def process(self,podnamelist_PCG,data): #从yaml file里取出resource和replica的值
        for everypodname in podnamelist_PCG:
            everypodname_2ndhalf = data.get(everypodname) #get前半截的key，可以得到后半截数据, 比如得到eric-log-transformer: 后半截数据
            replica_value = everypodname_2ndhalf.get('replicaCount', None)
            replica_value_2nd = everypodname_2ndhalf.get('replicas',None)
            # print (replica_value)
            # print (replica_value_2nd)
            # print (everypodname)
            # print (everypodname_2ndhalf)
            # replicaCount: 2
            # resources:
            # logtransformer:
            # limits:
            # cpu: 1500m

            # everypodname_3rd = everypodname_2ndhalf.get(everypodname_2ndhalf)


            if "resources" in everypodname_2ndhalf: #这里查出来的结果不全呢？答案：是因为之前最后用了return，直接跳出了循环
                resources_details = everypodname_2ndhalf["resources"]
                # print(everypodname)
                # print(everypodname_2ndhalf)
                # print(resources_details)
            else:
                continue #中断这一次的for循环，进入下一次的for循环。我第一次用成了return，则是跳出了这个for循环


            if ("requests" or "limits") in resources_details:
                self.get_detailed_resources(resources_details,everypodname,replica_value,replica_value_2nd) # 传的是requests/limits这一层
            else:
                for container in resources_details:
                    # resources_details[container] # key对应value
                    self.get_detailed_resources(resources_details[container],everypodname,container,replica_value,replica_value_2nd) #传的是requests/limits这一层

    def get_detailed_resources(self, resources_level1, everypodname, container=None,replica_value=None,replica_value_2nd=None): # 万一没有传参数，container=None, 默认的container值是None
        data_list = []
        data_list.append(everypodname)  # 第一列是pod name，比如eric-log-transformer
        data_list.append(container)  # 第二列是resource，就是resources里的每个resource，比如logtransformer
        data_list.append(self.return_value(resources_level1, ["requests", "cpu"]))  # 调用return_value函数，输入为一个字典和不定的众多levels
        data_list.append(self.return_value(resources_level1, ["requests", "memory"]))
        data_list.append(self.return_value(resources_level1, ["requests", "ephemeral-storage"]))
        data_list.append(self.return_value(resources_level1, ["limits", "cpu"]))
        data_list.append(self.return_value(resources_level1, ["limits", "memory"]))
        data_list.append(self.return_value(resources_level1, ["limits", "ephemeral-storage"]))
        # return data_list
        data_list.append(replica_value)
        data_list.append(replica_value_2nd)
        print(data_list)
        # self.worksheet.append(data_list)




if __name__=='__main__':
    path = r'C:/Users/lxi/OneDrive - Sigma Technology/Desktop/eric-pc-gateway-1.44.0-1269/eric-pc-gateway-1.44.0-1269/eric-pc-gateway'
    filename = 'values.yaml'
    test = Test(path,filename)
    test.getfile()



