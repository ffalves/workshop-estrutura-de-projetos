"""Orquestrador de todos os módulos."""

from pipeline.extract import extract_from_excel
from pipeline.load import load_excel
from pipeline.transform import concat_data_frame

if __name__ == "__main__":
    data_frame_list = extract_from_excel("data/input")
    data_frame = concat_data_frame(data_frame_list)
    load_excel(data_frame, "data/output", "output")
