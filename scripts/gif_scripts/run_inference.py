import argparse
from pepe_semantics.inference import InferenceModel
from pepe_semantics.model.index import GIFIndex


_TWEET_ENCODER_WEIGHTS_PATH = "/Users/u_brixton/Documents/git/prj/pepe-semantics/gif-reply/src/pepe/data/tweet_encoder/tweet_encoder_weights.pth"


def main(input_text, csv_features_fpath, gif_ids_mapping_fpath):
    model = InferenceModel(_TWEET_ENCODER_WEIGHTS_PATH)
    text_emb = model.embed_text(input_text)
    index = GIFIndex.from_csv(
        csv_features_fpath=csv_features_fpath, gif_ids_mapping_fpath=gif_ids_mapping_fpath,
    )
    giphy_links = index.get_giphy_links(text_emb)
    print(giphy_links)

def _parse_args():
    # FIXME: add arguments
    parser = argparse.ArgumentParser(description="Returns relevant gif in addition to texts")
    parser.add_argument("-i", "--input-text", required=True, help="Input text")
    parser.add_argument(
        "-c", "--csv-features-fpath", required=True, help="CSV file with gif ids and embs"
    )
    parser.add_argument(
        "-g", "--gif-ids-mapping-fpath", required=True, help="CSV file with gif to giphy id mapping"
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = _parse_args()
    main(
        input_text=args.input_text,
        csv_features_fpath=args.csv_features_fpath,
        gif_ids_mapping_fpath=args.gif_ids_mapping_fpath,
    )
