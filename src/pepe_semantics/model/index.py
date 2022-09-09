import csv
from ast import literal_eval

import numpy as np
import faiss


class GIFIndex:
    def __init__(self, embeddings, gif_ids, giphy_ids):
        self._create_index(embeddings)
        self._gif_ids = gif_ids
        self._giphy_ids = giphy_ids

    def _create_index(self, embeddings):
        emb_dim = embeddings.shape[1]
        self._index = faiss.IndexFlatIP(emb_dim)
        self._index.add(embeddings.astype('float32'))

    def _get_nearest_ids(self, text_embedding, k=5):
        # TODO: pre-check if already unsqueezed
        text_embedding = np.expand_dims(text_embedding, 0)
        _, ids = self._index.search(text_embedding, k)
        return np.squeeze(ids)

    def get_giphy_links(self, text_embedding, k=5):
        ids = self._get_nearest_ids(text_embedding, k)
        giphy_ids = [self._giphy_ids[id_] for id_ in ids]
        giphy_links = [create_giphy_link(giphy_id) for giphy_id in giphy_ids]
        return giphy_links

    @classmethod
    def from_csv(cls, csv_features_fpath, gif_ids_mapping_fpath):
        # TODO: resave all ids with only giphy ids in a single file
        gif_ids, embeddings = zip(*[el for el in read_csv_file(csv_features_fpath)])
        embeddings = np.array([literal_eval(emb) for emb in embeddings])
        gif_to_giphy_ids = read_gif_to_giphy_ids(gif_ids_mapping_fpath)
        giphy_ids = [gif_to_giphy_ids[gif_id] for gif_id in gif_ids]
        return cls(gif_ids=gif_ids, giphy_ids=giphy_ids, embeddings=embeddings)


def read_csv_file(csv_file):
    with open(csv_file) as f:
        # FIXME: maybe change to DictReader
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            yield row

def read_gif_to_giphy_ids(gif_ids_mapping_path):
    gif_ids, giphy_ids = zip(*[el for el in read_csv_file(gif_ids_mapping_path)])
    return {gif_id:giphy_id for gif_id, giphy_id in zip(gif_ids, giphy_ids)}


def create_giphy_link(giphy_id):
    return f"https://media.giphy.com/media/{giphy_id}/giphy.mp4"