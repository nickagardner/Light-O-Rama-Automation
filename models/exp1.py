import torch
class SimpleLinear(torch.nn.Module):
    def __init__(self):
        super(SimpleLinear, self).__init__()
        
        self.activation = torch.nn.ReLU()
        self.dropout = torch.nn.Dropout(p=0.1)
        self.linear1 = torch.nn.Linear(68, 256)
        self.linear2 = torch.nn.Linear(256, 128)
        self.linear3 = torch.nn.Linear(128, 64)
        self.linear4 = torch.nn.Linear(64, 48)

    def forward(self, x):
        x = self.dropout(self.linear1(x))
        x = self.activation(x)
        x = self.dropout(self.linear2(x))
        x = self.activation(x)
        x = self.dropout(self.linear3(x))
        x = self.activation(x)
        x = self.dropout(self.linear4(x))
        x = self.activation(x)
        return x