from scipy.signal import lfilter
import pandas as pd


class Preprocessor:
    def __init__(self):
        pass

    @staticmethod
    def process(data, chunk_size=256, smooth=20):
        timestamp = [i for i in range(0, len(data))]

        data_obj = {"data": data, "timestamp": timestamp}
        dataframe = pd.DataFrame(data_obj)

        if smooth > 0:
            n = smooth
            b = [1.0 / n] * n
            a = 1
            dataframe["data"] = lfilter(b, a, dataframe["data"].values)
        
        if len(dataframe["data"]) > chunk_size:
            dataframe = dataframe.iloc[-chunk_size:]
    
        dataframe.reset_index(drop=True, inplace=True)
        return dataframe
