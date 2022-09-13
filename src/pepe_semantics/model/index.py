import csv
import hashlib
import pickle
from ast import literal_eval
from pathlib import Path

import faiss
import numpy as np

_INDEX_FNAME = "index"
_GIPHY_IDS_FNAME = "giphy_ids.pkl"


class GIFIndex:
    def __init__(self, giphy_ids, embeddings=None, index=None):
        if index is None and embeddings is None:
            raise ValueError("Embedding or built index should be provided")
        if index is None:
            self._create_index(embeddings)
        else:
            self._index = index
        self._giphy_ids = giphy_ids
        # TODO: save some unique id of the encoding model

    def _create_index(self, embeddings):
        emb_dim = embeddings.shape[1]
        # TODO: can add optimizations like HNSW search here
        self._index = faiss.IndexFlatIP(emb_dim)
        self._index.add(embeddings.astype("float32"))

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

    def save_index(self, save_dir):
        # TODO: can maybe compress before saving
        Path(save_dir).mkdir(exist_ok=True, parents=True)
        faiss.write_index(self._index, str(Path(save_dir) / _INDEX_FNAME))

    def save_giphy_ids(self, save_dir):
        with open(save_dir / _GIPHY_IDS_FNAME, "wb") as fout:
            pickle.dump(self._giphy_ids, fout, protocol=4)

    def save(self, save_dir):
        self.save_index(save_dir)
        self.save_giphy_ids(save_dir)

    @classmethod
    def load(cls, save_dir):
        giphy_ids = load_giphy_ids(save_dir)
        index = load_index(save_dir)
        return GIFIndex(index=index, giphy_ids=giphy_ids)

    @classmethod
    def from_csv(cls, csv_features_fpath, gif_ids_mapping_fpath):
        # TODO: resave all ids with only giphy ids in a single file
        gif_ids, embeddings = zip(*[el for el in read_csv_file(csv_features_fpath)])
        embeddings = np.array([literal_eval(emb) for emb in embeddings])
        gif_to_giphy_ids = read_gif_to_giphy_ids(gif_ids_mapping_fpath)
        giphy_ids = [gif_to_giphy_ids[gif_id] for gif_id in gif_ids]
        return cls(giphy_ids=giphy_ids, embeddings=embeddings)


def read_csv_file(csv_file):
    with open(csv_file) as f:
        # FIXME: maybe change to DictReader
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            yield row


def load_giphy_ids(save_dir):
    with open(save_dir / _GIPHY_IDS_FNAME, "rb") as fin:
        giphy_ids = pickle.load(fin)
    return giphy_ids


def load_index(save_dir):
    return faiss.read_index(str(Path(save_dir) / _INDEX_FNAME))


def read_gif_to_giphy_ids(gif_ids_mapping_path):
    gif_ids, giphy_ids = zip(*[el for el in read_csv_file(gif_ids_mapping_path)])
    return {gif_id: giphy_id for gif_id, giphy_id in zip(gif_ids, giphy_ids)}


def create_giphy_link(giphy_id):
    # TODO: maybe change the link - seems to work only for embedded
    return f"https://media.giphy.com/media/{giphy_id}/giphy.mp4"
