from predict import Predictor
import os
pred = Predictor()
pred.setup()
pred.predict('data/flower.png', False)