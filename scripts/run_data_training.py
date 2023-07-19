import logging
import os
import shutil
from datetime import datetime
from pathlib import Path

from interpretability.data_modeling.lfads_torch.run_model import run_model

logger = logging.getLogger(__name__)

# ---------- OPTIONS -----------
OVERWRITE = True
PROJECT_STR = "0719_MotorNet_DataTrain"
DATASET_STR = "RTR"
RUN_TAG = datetime.now().strftime("%Y%m%d-%H%M%S")
RUN_DIR = (
    Path("/snel/share/runs/lfads-NODE") / PROJECT_STR / DATASET_STR / "single" / RUN_TAG
)
# ------------------------------

# Overwrite the directory if necessary
if RUN_DIR.exists() and OVERWRITE:
    shutil.rmtree(RUN_DIR)
RUN_DIR.mkdir(parents=True)
# Copy this script into the run directory
shutil.copyfile(__file__, RUN_DIR / Path(__file__).name)
# Switch to the `RUN_DIR` and train the model
os.chdir(RUN_DIR)
run_model(
    project_str=PROJECT_STR,
    overrides={
        "datamodule": DATASET_STR,
        "model": DATASET_STR,
    },
    config_path=f"../configs/{DATASET_STR}.yaml",
)
