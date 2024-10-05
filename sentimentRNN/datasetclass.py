import torch
from torch.utils.data import Dataset
from sentimentRNN import textpreprocess

class TextSentimentDataset(Dataset):
    def __init__(self, file_paths, tokenizer, vocab, label_map):
        self.file_paths = file_paths
        self.tokenizer = tokenizer
        self.vocab = vocab
        self.label_map = label_map

    def __len__(self):
        return len(self.file_paths)

    def __getitem__(self, idx):
        file_path = self.file_paths[idx]
        
        # ground truth sentiment
        label = 'pos' if 'pos' in file_path else 'neg'
        label = self.label_map[label]

        # load text
        with open(file_path) as f:
            text = f.readlines()[0]
        text = textpreprocess.clean_text(text)

        # Tokenize text and convert to indices
        tokens = self.tokenizer(text)
        token_indices = [self.vocab[token] for token in tokens]

        return torch.tensor(token_indices), torch.tensor(label)
