from pepe_semantics import config
from pepe_semantics.model.index import GIFIndex


# used only to quickly build index from the authors data
def main():
    index = GIFIndex.from_csv(
        csv_features_fpath=config.GIF_ID_TO_INFERRED_FEATURE_PATHS[1],
        gif_ids_mapping_fpath=config.GIF_ID_TO_GIPHY_ID_PATHS[1],
    )
    index.save(config.INDEX_DIR)


if __name__ == "__main__":
    main()
