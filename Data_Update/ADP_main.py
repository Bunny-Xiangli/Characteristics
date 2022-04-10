import ADP_Extracted
import ADP_settings

if __name__ == '__main__':
    extracted = ADP_Extracted.Extract_Data(ADP_settings.PATH,ADP_settings.subfolders,ADP_settings.filename,ADP_settings.excel_path)
    extracted.action()

