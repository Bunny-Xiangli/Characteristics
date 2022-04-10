import PCG_Extracted
import PCG_settings

if __name__ == '__main__':
    extracted = PCG_Extracted.Extract_Data_2nd_PCG(PCG_settings.PATH,PCG_settings.filename,PCG_settings.excel_path)
    extracted.action()

