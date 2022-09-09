import torch
import torch.nn as nn
from transformers import AutoModel

TEXT_ENCODER_MODEL_NAME = 'vinai/bertweet-base'

class TweetEncoder(nn.Module):
    def __init__(self, output_dim=512):
        super().__init__()
        self._hidden_size = 768
        self.bertweet = AutoModel.from_pretrained(TEXT_ENCODER_MODEL_NAME)
        self.linear_transform = nn.Linear(self._hidden_size, output_dim)
        nn.init.xavier_normal_(self.linear_transform.weight)

    def forward(self, tweet_input_ids):
        features = self.bertweet(tweet_input_ids)
        return self.linear_transform(features["pooler_output"])

    @classmethod
    def load(cls, weights_path):
        model = cls()
        model.load_state_dict(torch.load(weights_path))
        model.eval()
        return model
