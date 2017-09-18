import cPickle as pickle
import numpy as np

X=np.array([[1,0,1,0],[1,0,1,1],[0,1,0,1]])
with open('wh.sav','rb') as f:
	wh=pickle.load(f)
with open('bh.sav','rb') as f:
	bh=pickle.load(f)
with open('wout.sav','rb') as f:
	wout=pickle.load(f)
with open('bout.sav','rb') as f:
	bout=pickle.load(f)

def sigmoid (x):
    return 1/(1 + np.exp(-x))

hidden_layer_input=np.dot(X,wh)+bh
hiddenlayer_activations = sigmoid(hidden_layer_input)
output_layer_input1=np.dot(hiddenlayer_activations,wout)
output_layer_input= output_layer_input1+bout
output = sigmoid(output_layer_input)
print(output)