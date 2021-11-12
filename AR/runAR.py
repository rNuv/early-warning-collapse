from statsmodels.tsa.ar_model import AutoReg
import pickle
from ARfromJSON import loadData

def runModel(data, model, sensorUnit, sensor):
	#number of previous data points loaded
	backtrack = 150

	#load dataset
	series = loadData(data, sensorUnit, sensor)
	prev = series[-backtrack:]

	#load model
	file_to_read = open(model, "rb")
	model_fit = pickle.load(file_to_read)
	file_to_read.close()
	coef = model_fit.params

	#run through model
	window = 2
	predictions = list()
	length = len(prev)
	lag = [prev[i] for i in range(length-window,length)]
	yhat = coef[0]
	for d in range(window):
		yhat += coef[d+1] * lag[window-d-1]
	prediction = yhat

	return prediction

def runModelFromArray(data, model):
	#number of previous data points loaded
	backtrack = 150

	#load dataset
	prev = data[-backtrack:]

	#load model
	file_to_read = open(model, "rb")
	model_fit = pickle.load(file_to_read)
	file_to_read.close()
	coef = model_fit.params

	#run through model
	window = 2
	predictions = list()
	length = len(prev)
	lag = [prev[i] for i in range(length-window,length)]
	yhat = coef[0]
	for d in range(window):
		yhat += coef[d+1] * lag[window-d-1]
	prediction = yhat

	return prediction

