from pathlib import Path

EXTERNAL_FILES_FOLDER = Path(__file__).resolve().parent
# EXTERNAL_FILES_FOLDER = Path("/app/src/pepe_semantics/")

MODELS_FOLDER = EXTERNAL_FILES_FOLDER / "model"
FEATURES_FOLDER = EXTERNAL_FILES_FOLDER / "features"
INDICES_FOLDER = EXTERNAL_FILES_FOLDER / "index"

# format: ("path_where_to_save", "fname", "google_drive_unique_id")
# TODO: get rid of GIDs?

# INFERENCE MODEL
# resaved them separately from full PEPE model
BERTWEET_WEIGHTS_PATHS = (
    "tweet_encoder_weights.pth",
    MODELS_FOLDER / "bertweet_weights.pth",
    "1cxLrHoLe2R2c5mxrXtn6zres-kEybnML",
)

# DATA
GIF_ID_TO_INFERRED_FEATURE_PATHS = (
    "gif-pepe-inferred-features.csv",  # Full features
    FEATURES_FOLDER / "gif_id_to_feature.csv",
    "1GClR5KLOsYAgYSS3iKP1k6-qcynR7d7g",
)

GIF_ID_TO_GIPHY_ID_PATHS = (
    "gif_id_to_giphy_id.csv",
    FEATURES_FOLDER / "gif_id_to_giphy_id.csv",
    "1OBEWu4RKkLciwtDnR0ecVqbjCPU9cVG7",
)

# WHERE TO SAVE OUR BUILT INDEX
INDEX_DIR = INDICES_FOLDER / "pepe_index"
print(INDEX_DIR)

INDEX_FILE_PATHS = (
    "full-index",
    INDEX_DIR / "index_hnsw"
)

PKL_FILE_PATHS = (
    "full-giphy_ids.pkl",
    INDEX_DIR / "giphy_ids.pkl"
)
