import torch
class LOR_Dataset(torch.utils.data.Dataset):
    def __init__(self, signal, dense_seqs, channel_df, file_lengths):
        self.signal = signal
        self.dense_seqs = dense_seqs
        self.channel_df = channel_df
        self.frame_rate = frame_rate
        self.file_lengths = file_lengths
        
        sequence = np.empty([len(self.dense_seqs[1][1]), len(np.unique(self.channel_df["unit"]))* len(np.unique(self.channel_df["circuit"]))])
        for idx in range(len(self.dense_seqs[1][1])):
            arr_idx = 0
            for unit in np.unique(self.channel_df["unit"]):
                for circuit in np.unique(self.channel_df[self.channel_df["unit"] == unit]["circuit"]):
                    sequence[idx, arr_idx] = self.dense_seqs[unit][circuit][idx]
                    arr_idx += 1
                
        self.signal = torch.Tensor(signal)
        self.sequence = torch.Tensor(sequence)

    def __len__(self):
        return len(self.dense_seqs[1][1])

    def __getitem__(self, idx):
        return self.signal[idx], self.sequence[idx]