from predict import Predictor
import os

os.environ["TORCH_CUDNN_SDPA_ENABLED"] = "1"

pred = Predictor()
pred.setup()
pred.predict('data/hunter_room.jpg', False)