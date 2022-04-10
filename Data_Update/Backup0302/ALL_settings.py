import os
import ALL_GUI

# # #PCG:

# Get_from_Entry_path = r'C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-gateway-1.47.0-44\eric-pc-gateway-1.47.0-44\eric-pc-gateway'
Get_from_Entry_path = ALL_GUI.theEntry_Charts.get() #想调用ALL_GUI里theEntry_Charts输入框里的内容

ADP_PATH = Get_from_Entry_path + '/' + 'charts'
PCG_PATH = Get_from_Entry_path
USER_PATH = Get_from_Entry_path + '\supporting-files\example-config'



# PATH  =r"C:/Users/lxi/OneDrive - Sigma Technology/Desktop/eric-pc-gateway-1.47.0-44/eric-pc-gateway-1.47.0-44/eric-pc-gateway\charts"

# subfolders = [
#     "eric-log-transformer"
#     ,"eric-log-shipper"
#     ,"eric-fh-alarm-handler"
#     ,"eric-cm-mediator"
#     ,"eric-data-coordinator-zk"
#     ,"eric-ctrl-bro"
# ]

subfolders = os.listdir(r'C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-gateway-1.47.0-44\eric-pc-gateway-1.47.0-44\eric-pc-gateway\charts')
subfolders.remove("eric-data-search-engine")

filename = "values.yaml"

ADP_Excel_path = r"C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-gateway-1.47.0-44\ADP_output.xlsx"
PCG_Excel_path = r"C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-gateway-1.47.0-44\PCG_output.xlsx"
USER_Excel_path = r"C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-gateway-1.47.0-44\USER_output.xlsx"

