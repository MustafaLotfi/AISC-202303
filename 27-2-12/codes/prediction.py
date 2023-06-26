import numpy as np
from keras.models import load_model
from joblib import load
import os
import sklearn


PATH2ROOT = os.path.dirname(__file__) + '/../'
model = load_model(PATH2ROOT+'models//model_4fps_13inputs.h5')
scaler = load(PATH2ROOT+'models//scaler.bin')


def prepare_data(data, values):
	values['t'].append(int(data.split(':')[2].split(',')[0]))
	values['x'].append(float(data.split(':')[3].split(',')[0][1:-1]))
	values['y'].append(float(data.split(':')[4].split(',')[0][1:-1]))
	values['z'].append(float(data.split(':')[5].split(',')[0][1:-1]))

	return values


def predict(values, BATCH_SIZE):
	x = np.concatenate((np.array(values['x']).reshape((-1, 1)),
		np.array(values['y']).reshape((-1, 1)), np.array(values['z']).reshape((-1, 1))), 1)

	if x.shape[0] == BATCH_SIZE:
		x_nrm = scaler.transform(x)

		x = np.expand_dims(x_nrm, 0)

		y = model.predict(x).round()

		return y