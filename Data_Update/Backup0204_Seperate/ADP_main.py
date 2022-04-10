import ADP_Extracted
import ADP_settings

extracted = ADP_Extracted.Extract_Data(ADP_settings.PATH, ADP_settings.subfolders, ADP_settings.filename,
                                       ADP_settings.excel_path)
extracted.action()

# if __name__ == '__main__':
#
#     print(extracted.Extracted_Data.data_list_ADP)

