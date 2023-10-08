# W&B parameters
PROJECT_NAME = "pis_course"
ENTITY = "rca-dev"  # change this to you wandb team/entity name
WANDB_NOTEBOOK_NAME = "prepare_data.ipynb"

# ENTITY = None

# parameters for the dataset
RAW_DATA_FOLDER = "lemon-dataset"
IMAGES_FOLDER = "images"
ANNOTATIONS_FILE = "annotations/instances_default.json"
ARTIFACT_NAME = "lemon_data"
# DATA_AT = f"{PROJECT_NAME}/{ARTIFACT_NAME}:v0"
DATA_AT = f"{ENTITY}/{PROJECT_NAME}/{ARTIFACT_NAME}:v0"  # if Entity is not None