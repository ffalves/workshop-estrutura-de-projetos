from pipeline.extract import extract_from_excel
from pipeline.transform import concat_data_frame
from pipeline.load import load_excel


listas_de_df = extract_from_excel("data/input")
print(listas_de_df)

if __name__ == '__main__':
    data_frame_list = extract_from_excel('data/input')
    data_frame = concat_data_frame(data_frame_list)
    load_excel(data_frame, 'data/output', 'output')