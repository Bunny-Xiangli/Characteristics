import os

# # #PCG:

PATH  =r"C:\Users\lxi\OneDrive - Sigma Technology\Desktop\Test\eric-pc-gateway-1.45.6-79\eric-pc-gateway-1.45.6-79\eric-pc-gateway\charts"

# subfolders = [
#     "eric-log-transformer"
#     ,"eric-log-shipper"
#     ,"eric-fh-alarm-handler"
#     ,"eric-cm-mediator"
#     ,"eric-data-coordinator-zk"
#     ,"eric-ctrl-bro"
# ]

subfolders = os.listdir(r'C:\Users\lxi\OneDrive - Sigma Technology\Desktop\Test\eric-pc-gateway-1.45.6-79\eric-pc-gateway-1.45.6-79\eric-pc-gateway\charts')
subfolders.remove("eric-data-search-engine")
subfolders.remove('desktop.ini')

filename = "values.yaml"
excel_path = r"C:\Users\lxi\OneDrive - Sigma Technology\Desktop\Test\eric-pc-gateway-1.45.6-79\eric-pc-gateway-1.45.6-79\ADP_output.xlsx"





# PCC:
# PATH = r"C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-controller-1.41.12-1\eric-pc-controller-1.41.12-1\eric-pc-controller\charts"
# subfolders = os.listdir(r'C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-controller-1.41.12-1\eric-pc-controller-1.41.12-1\eric-pc-controller\charts')
# subfolders.remove("eric-data-search-engine")
# filename = "values.yaml"
# excel_path = r"C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-controller-1.41.12-1\output_ADP_for_PCC.xlsx"




