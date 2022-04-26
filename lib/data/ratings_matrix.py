import data.plot as pl
import torch
import pytorch_common.util as pu
import logging


class RatingsMatrix:
    @classmethod
    def from_dataframe(cls, df, user_seq_column, item_seq_column, rating_column, device=pu.get_device()):
        sw = pu.Stopwatch()
        n_users = df[user_seq_column].max() + 1
        n_items = df[item_seq_column].max() + 1
        tensor = torch.zeros([n_users, n_items], dtype=torch.float).to(device)

        for _, row in df.iterrows():
            tensor[int(row[user_seq_column]), int(row[item_seq_column])] = row[rating_column]

        logging.info(f'Create ratting matrix - computing time: {sw.to_str()}')
        return cls.from_tensor(tensor)

    @staticmethod
    def from_tensor(tensor, device=pu.get_device()): return RatingsMatrix(tensor, device) 

    def __init__(self, data, device=pu.get_device()): self.__data = data.to(device)

    def plot(self, figsize = (10, 10)):        
        pl.headmap(self.__data.cpu(), title=f'Rating Matrix ({self.__data.shape[0]},{self.__data.shape[1]})', figsize=figsize)

    def __getitem__(self, index):  return self.__data[index[0], index[1]]
  
    def __setitem__(self, index, value):  self.__data[index[0], index[1]] = value

    @property
    def n_rows(self): return self.__data.shape[0]

    @property
    def n_columns(self): return self.__data.shape[1]

    @property
    def shape(self): return (self.n_rows, self.n_columns)

    def mean_row(self, row_idx): return self.__data[row_idx, :].mean()

    def row_deviation(self, row_idx, col_idx): return self[row_idx, col_idx] - self.mean_row(row_idx)
