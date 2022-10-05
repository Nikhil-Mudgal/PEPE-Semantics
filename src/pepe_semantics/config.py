from pathlib import Path

#EXTERNAL_FILES_FOLDER = Path(__file__).resolve().parent
EXTERNAL_FILES_FOLDER = Path("/app/src/pepe_semantics/")

MODELS_FOLDER = EXTERNAL_FILES_FOLDER / "model"
FEATURES_FOLDER = EXTERNAL_FILES_FOLDER / "features"
INDICES_FOLDER = EXTERNAL_FILES_FOLDER / "index"

# format: ("google_drive_unique_id", "path_where_to_save")

# INFERENCE MODEL
# resaved them separately from full PEPE model
BERTWEET_WEIGHTS_PATHS = (
    #"1cxLrHoLe2R2c5mxrXtn6zres-kEybnML",
    "tweet_encoder_weights.pth",
    MODELS_FOLDER / "bertweet_weights.pth",
)

# DATA
GIF_ID_TO_INFERRED_FEATURE_PATHS = (
    #"15jTsnN6cYIf2KBcJ85Km_xH2pjH8HILN",
    #"1GClR5KLOsYAgYSS3iKP1k6-qcynR7d7g", # Full features..
    "gif-pepe-inferred-features.csv",  # Full features
    #"gif_id_to_feature.csv",  # 1 k sample
    FEATURES_FOLDER / "gif_id_to_feature.csv",
)  # 1k sample

# GIF_ID_TO_INFERRED_FEATURE_PATHS = \
# "1GClR5KLOsYAgYSS3iKP1k6-qcynR7d7g", FEATURES_FOLDER/"gif_id_to_feature.csv"  # full 115K dataset
GIF_ID_TO_GIPHY_ID_PATHS = (
    #"1OBEWu4RKkLciwtDnR0ecVqbjCPU9cVG7",
    "gif_id_to_giphy_id.csv",
    FEATURES_FOLDER / "gif_id_to_giphy_id.csv",
)

# WHERE TO SAVE OUR BUILT INDEX
INDEX_DIR = INDICES_FOLDER / "pepe_index"
print(INDEX_DIR)

INDEX_FILE_PATHS = (
    "index",
    INDEX_DIR / "index"
)

PKL_FILE_PATHS = (
    "giphy_ids.pkl",
    INDEX_DIR / "giphy_ids.pkl"
)

