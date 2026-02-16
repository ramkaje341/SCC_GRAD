"""
This is predictor.py file --single file for all the 4 models.
Model names: Densenet121,ConvNextinty,EfficientNet,MobileNet.
Model Path-- the models are stored in: backend/model_DL
input-- image
output-- predictions: well or mod and the confidence score

"""
import os
import numpy as np
from PIL import Image
import io

CLASS_NAMES=["well","mod"]

IMG_SIZE=(320,320)

Model_PATHS={
    "Densenet121": os.path.join("model_DL","model_densenet121.h5")


}

_loaded_models = {}


