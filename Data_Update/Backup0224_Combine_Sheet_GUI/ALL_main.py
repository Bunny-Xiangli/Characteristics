import ADP_Extracted
# import ADP_settings
import PCG_Extracted
# import PCG_settings
import USER_Extracted
# import USER_settings
import ALL_settings
# import ALL_GUI

if __name__ == '__main__':
    ADP_Run = ADP_Extracted.Extract_Data(ALL_settings.ADP_PATH,ALL_settings.subfolders,ALL_settings.filename,ALL_settings.ADP_Excel_path)
    ADP_Run.action()

    PCG_Run = PCG_Extracted.Extract_Data_2nd_PCG(ALL_settings.PCG_PATH, ALL_settings.filename, ALL_settings.PCG_Excel_path)
    PCG_Run.action()

    USER_Run = USER_Extracted.Extract_Data_3rd_USER(ALL_settings.USER_PATH, ALL_settings.filename, ALL_settings.USER_Excel_path)
    USER_Run.action()


#先把Excel写入到三个sheet里