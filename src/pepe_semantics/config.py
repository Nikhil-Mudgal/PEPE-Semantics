from pathlib import Path
# those paths are actually to the installed library path, not local repo copy
# better to save to /var or /opt, but permissions are needed for that
# temporarily saving to installed package location

#EXTERNAL_FILES_FOLDER = Path(__file__).resolve().parent
EXTERNAL_FILES_FOLDER = Path("/app/src/pepe_semantics/")
#EXTERNAL_FILES_FOLDER = Path("/Users/jobquiroz/OneDrive/MachineLearningHero/PEPE/PEPE-semantics/pepe_semantics")
MODELS_FOLDER = EXTERNAL_FILES_FOLDER / "model"
FEATURES_FOLDER = EXTERNAL_FILES_FOLDER / "features"
INDICES_FOLDER = EXTERNAL_FILES_FOLDER / "index"

# format: ("google_drive_unique_id", "path_where_to_save")

# INFERENCE MODEL
# resaved them separately from full PEPE model
BERTWEET_WEIGHTS_PATHS = (
    "1cxLrHoLe2R2c5mxrXtn6zres-kEybnML",
    MODELS_FOLDER / "bertweet_weights.pth",
)

# DATA
GIF_ID_TO_INFERRED_FEATURE_PATHS = (
    "15jTsnN6cYIf2KBcJ85Km_xH2pjH8HILN",
    FEATURES_FOLDER / "gif_id_to_feature.csv",
)  # 1k sample

GIF_ID_TO_INFERRED_FEATURE_PATHS_FULL = (
    "1GClR5KLOsYAgYSS3iKP1k6-qcynR7d7g",
    FEATURES_FOLDER / "full_gif_id_to_feature.csv",
)

# GIF_ID_TO_INFERRED_FEATURE_PATHS = \
# "1GClR5KLOsYAgYSS3iKP1k6-qcynR7d7g", FEATURES_FOLDER/"gif_id_to_feature.csv"  # full 115K dataset
GIF_ID_TO_GIPHY_ID_PATHS = (
    "1OBEWu4RKkLciwtDnR0ecVqbjCPU9cVG7",
    FEATURES_FOLDER / "gif_id_to_giphy_id.csv",
)

# WHERE TO SAVE OUR BUILT INDEX
INDEX_DIR = INDICES_FOLDER / "pepe_index"
print(INDEX_DIR)