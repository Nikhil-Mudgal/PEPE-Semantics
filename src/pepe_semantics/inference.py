import torch
from transformers import AutoTokenizer

from pepe_semantics.model.tweet_encoder import TweetEncoder, TEXT_ENCODER_MODEL_NAME

class InferenceModel:
    def __init__(self, tweet_encoder_weights_path):
        self.tweet_encoder = TweetEncoder.load(tweet_encoder_weights_path)
        self._text_tokenizer = AutoTokenizer.from_pretrained(TEXT_ENCODER_MODEL_NAME)

    def tokenize_text(self, text):
        return self._text_tokenizer([text], return_tensors="pt")["input_ids"]

    def embed_text(self, text):
        with torch.no_grad():
            return self.tweet_encoder(self.tokenize_text(text))[0].cpu().detach().numpy()
