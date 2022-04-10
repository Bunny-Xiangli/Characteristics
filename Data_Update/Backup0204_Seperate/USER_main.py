import USER_Extracted
import USER_settings

if __name__ == '__main__':
    extracted = USER_Extracted.Extract_Data_3rd_USER(USER_settings.PATH,USER_settings.filename,USER_settings.excel_path)
    extracted.action()

