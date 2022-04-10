import ADP_Extracted
import ADP_settings
import PCG_Extracted
import PCG_settings
import USER_Extracted
import USER_settings
import FINAL_Extracted
import FINAL_settings

if __name__ == '__main__':
    extracted = FINAL_Extracted.Final_Extract_Data(FINAL_settings.PATH,FINAL_settings.excel_path)
    extracted.action(FINAL_settings.excel_path)

