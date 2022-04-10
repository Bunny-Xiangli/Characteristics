import os

PATH  = r'C:\Users\lxi\OneDrive - Sigma Technology\Desktop\eric-pc-controller-1.45.13-6\eric-pc-controller-1.45.13-6'

filename = 'values.yaml'

subfolders = os.listdir(PATH)

# print (subfolders)

for subfolder in subfolders:
    if subfolder == 'eric-pc-sm':
        # subfolder_charts = os.listdir(PATH + "/charts/" + 'eric-pc-mm/charts')
        # print(subfolder_charts)
        for subsubfolder in subfolder_charts:
            absolutepath = PATH + "/" + subfolder + "/" + 'charts/' + subsubfolder + '/' + filename
    # #     # extract(subfolder, absolutepath)
    #     print(subsubfolder)
    # if subfolder == 'eric-pc-sm':
    #     subfolder_charts = os.listdir(PATH + "/" + 'eric-pc-sm/charts')
    #     # print(subfolder_charts)
    #     for subsubfolder in subfolder_charts:
    #         absolutepath = PATH + "/" + subfolder + "/" + 'charts' + subsubfolder + '/' + filename
    # #         # extract(subsubfolder, absolutepath)
    # #         print ('\n')
    #         print ('Yeah')
    #         print(subsubfolder)
    # else:
    #     pass
    # elif subfolder == 'eric-pc-mm':