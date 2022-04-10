# -*- coding: utf-8 -*-

#

import ADP_Extracted
import PCG_Extracted
import USER_Extracted
import FINAL_Extracted
import os
from tkinter import *
#
# data_list_ADP = None
# data_list_PCG = None
# data_list_USER = None
# print (data_list_ADP)


os.system('taskkill /f /im excel.exe')#先关掉电脑中已经打开的所有的excel

root = Tk()
root.title('Characteristics Generator (CPU, Memory, and Replicas)')

# group1 = LabelFrame(root, text='Please Give Your Inputs',padx=5,pady=5)
# group1.pack(padx=10,pady=10)

# group2 = LabelFrame(root, text='Note and Run',padx=5,pady=5)
# group2.pack(padx=10,pady=10)

frame1=Frame(root)
frame2=Frame(root)

#放Helm Chart路径
# theLabel_Charts=Label(frame1, text='Enter the Helm Charts path:').grid(sticky=W,row=0,column=0)
# theLabel_Charts_example=Label(frame1, text=r'For example, C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-gateway-1.47.0-44\eric-pc-gateway-1.47.0-44\eric-pc-gateway').grid(sticky=W, row=1,column=0)
# theEntry_Charts=Entry(frame1,width=130)
# theEntry_Charts.grid(padx=5, row=2,column=0)
# # theLabel_Charts.pack()

theLabel_Charts=Label(frame1, text='Enter the Helm Charts path:',font=('Arial',10,'bold')).grid(sticky=W,row=0,column=0)
example1 = StringVar()
example1.set(r'Example: C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-gateway-1.47.0-44\eric-pc-gateway-1.47.0-44')
theLabel_Charts_example = Entry(frame1,textvariable=example1,width=145, bd=0,state="readonly").grid(row = 1,column = 0,sticky = W)
helm_charts_path = StringVar()
#设置输入路径的默认选项
# helm_charts_path.set(r'C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-gateway-1.47.0-44\eric-pc-gateway-1.47.0-44')
theEntry_Charts=Entry(frame1,textvariable=helm_charts_path,width=140).grid(row=2,column=0,sticky = W)
print (helm_charts_path.get())



# #放输出的Excel路径
# theLabel_Output=Label(frame1, text='\nEnter the output Excel path:').grid(sticky=W,row=3,column=0)
# example2 = StringVar()
# example2.set(r'Example: C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-gateway-1.47.0-44\Output.xlsx')
# theLabel_Output_example = Entry(frame1,textvariable=example2,width=150, bd=0,state="readonly").grid(row = 4,column = 0,sticky = W)
# theEntry_Output=Entry(frame1,width=140).grid(row=5,column=0,sticky = W)

#放输出的services名字
# theLabel_Services=Label(frame1, text='\nEnter the services you need (empty means to run all services by default):', font=('Arial',10,'bold')).grid(sticky=W,row=6,column=0)
# example3 = StringVar()
# example3.set(r'Example: eric-cm-yang-provider, eric-log-transformer, eric-cm-mediator')
# theLabel_Services_example = Entry(frame1,textvariable=example3,width=150, bd=0,state="readonly").grid(row = 7,column = 0,sticky = W)
# theEntry_Services=Entry(frame1,width=140)
# theEntry_Services.grid(row=8,column=0,sticky = W)





# test = StringVar()
# test.set(example1.get())
# print (test)

# f = open (r'C:\XL\Sigma\Trainings\Python\test.txt','a')
# f.write (theEntry_Charts.get())
# #一定记得要close了，内容才会被写入文件
# f.close()


# PATH  =r"C:/Users/lxi/OneDrive - Sigma Technology/Desktop/eric-pc-gateway-1.47.0-44/eric-pc-gateway-1.47.0-44/eric-pc-gateway\charts"

# subfolders = [
#     "eric-log-transformer"
#     ,"eric-log-shipper"
#     ,"eric-fh-alarm-handler"
#     ,"eric-cm-mediator"
#     ,"eric-data-coordinator-zk"
#     ,"eric-ctrl-bro"
# ]



# ADP_Excel_path = r"C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-gateway-1.47.0-44\ADP_output.xlsx"
# PCG_Excel_path = r"C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-gateway-1.47.0-44\PCG_output.xlsx"
# USER_Excel_path = r"C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-gateway-1.47.0-44\USER_output.xlsx"


def run_all_together():
    # print('Helm Charts:%s' % theEntry_Charts.get())
    # print('output Excel:%s' % theEntry_Output.get())
    # print('Services:%s' % theEntry_Services.get())
    # #尝试把ALL_settings里的内容全部搬到这里：
    Get_from_Entry_path = helm_charts_path.get()  # 如果把这句写在了def外面，执行出来是空，为什么呢？
    if 'eric-pc-gateway' in os.listdir(Get_from_Entry_path):
        ADP_PATH = Get_from_Entry_path + '\eric-pc-gateway' + '/' + 'charts'
        PCG_PATH = Get_from_Entry_path + '\eric-pc-gateway'
        USER_PATH = Get_from_Entry_path + '\eric-pc-gateway' + '\supporting-files\example-config'


        Output_path=Get_from_Entry_path + '\Output.xlsx'
        subfolders = os.listdir(ADP_PATH)
        subfolders.remove("eric-data-search-engine")
        if 'desktop.ini' in os.listdir(ADP_PATH):
            subfolders.remove("desktop.ini")
        else:
            pass
        # subfolders.remove('eric-pc-firewall-coordinator-at')

        filename = "values.yaml"
        ADP_Run = ADP_Extracted.Extract_Data(ADP_PATH, subfolders, filename, Output_path)  # def里不能跑class么？
        ADP_Run.action()
        # data_list_ADP  = ADP_Extracted.Extract_Data.get_resources(subfolder, data,replica_data)

        PCG_Run = PCG_Extracted.Extract_Data_2nd_PCG(PCG_PATH, filename, Output_path)
        PCG_Run.action(Output_path)

        USER_Run = USER_Extracted.Extract_Data_3rd_USER(USER_PATH, filename, Output_path)
        USER_Run.action(Output_path)

        FINAL_Run = FINAL_Extracted.Final_Extract_Data(Output_path)
        FINAL_Run.action(Output_path)

    if 'eric-pc-controller' in os.listdir(Get_from_Entry_path):
        ADP_PATH = Get_from_Entry_path + '\eric-pc-controller' + '/' + 'charts'
        PCG_PATH = Get_from_Entry_path + '\eric-pc-controller'
        USER_PATH = Get_from_Entry_path + '\eric-pc-controller' + '\supporting-files\example-config'


        ADP_Excel_path = Get_from_Entry_path + '\ADP_output.xlsx'
        PCG_Excel_path = Get_from_Entry_path + '\PCG_output.xlsx'
        USER_Excel_path = Get_from_Entry_path + '\output.xlsx'

        Output_path = Get_from_Entry_path + '\Output.xlsx'
        subfolders = os.listdir(ADP_PATH)
        subfolders.remove("eric-data-search-engine")
        # subfolders.remove('eric-pc-firewall-coordinator-at')
        filename = "values.yaml"
        ADP_Run = ADP_Extracted.Extract_Data(ADP_PATH, subfolders, filename, Output_path)  # def里不能跑class么？
        ADP_Run.action()

        PCG_Run = PCG_Extracted.Extract_Data_2nd_PCG(PCG_PATH, filename, Output_path)
        PCG_Run.action(Output_path)

        # USER_Run = USER_Extracted.Extract_Data_3rd_USER(USER_PATH, filename, Output_path)
        # USER_Run.action(Output_path)

        FINAL_Run = FINAL_Extracted.Final_Extract_Data(Output_path)
        FINAL_Run.action(Output_path)


    else:
        pass




# Note:
theNote=Label(frame2,text='Please manually check:\n',font=('Arial',10),justify=LEFT).grid(sticky=W,row=2,column=0)

theNote_details2=Label(frame2,text='1.eric-data-search-engine as it is excluded in the script. \n'
                                   ,font=('Arial',10),justify=LEFT).grid(sticky=W,row=3,column=0)

# theNote_details2=Label(frame2,text='3.Check the empty resources:                                                                                                                       \n'
#                                    '-eric-pc-firewall-coordinator-at                                                                                                                   \n'
#                                    ,font=('Arial',10)).grid(sticky=W,row=5,column=0)

theNote_details1=Label(frame2,text='2. The "MISMTACH" Excel sheet.\n',font=('Arial',10),justify=LEFT).grid(sticky=W,row=4,column=0)

theNote_details3=Label(frame2,text='3.For PCG, the following services containing multiple replicas in the ADP YAML file:\n'
                                   '-eric-odca-diagnostic-data-collector, like service.replicas:1, manualService.replicas:1 \n'
                                   '-eric-data-distributed-coordinator-ed, like Pods.dced.replicas:3, brAgent.replicas:1 \n'
                                   '-eric-lm-combined-server, like licenseConsumerHandler.replicaCount:2, licenseServerClient.replicaCount:1 \n'
                                   ,font=('Arial',10),justify=LEFT).grid(sticky=W,row=5,column=0)


theNote_details3 = Label(frame2,text='4.For PCG, though the following services have two groups of replica in "FINAL" sheet, but should be OK: \n'
                                   '-eric-sec-key-management, use PCX replicas=2?  \n'                                                                   
                                   '-eric-log-transformer, confirm to use PCX replicas=2. Done!\n'
                                   ,font=('Arial',10),justify=LEFT).grid(sticky=W,row=6,column=0)



# theNote_details3=Label(frame2,text='3.P:',font=('Arial',10)).grid(sticky=W,row=5,column=0)

theButton1 = Button(frame2, text='RUN', command=run_all_together,justify=RIGHT,default='active',font=('Arial', '10','bold'),anchor=E).grid(sticky=W, row=10,column=50)
# theSpace = Button(frame2, text='    ',).grid(sticky=E, row=30,column=3)
# theButton2 = Button(frame2, text='Quit', command =quit).grid(sticky=E, row=30,column=5)
# theButton1.pack(side=RIGHT)

frame1.pack(padx=20,pady=20)
frame2.pack(side=LEFT,padx=20,pady=20,fill=BOTH) #写不写fill=BOTH，貌似没啥区别

mainloop()
