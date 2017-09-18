import numpy as np


#input
X = np.array([[1,0,1,0],[1,0,1,1],[0,1,0,1]])
# X=np.array([[1,0,1], [0,1,1], [1,1,0], [1,0,1]])
# y=np.array([[0], [1], [1], [0]])

#Real output
y = np.array([[1],[1],[0]])
#sigmoid Function
def sigmoid(x):
	return 1/(1 + np.exp(-x))

#derivative of a sigmoid function
def derivative_sigmoid(x):
	return x *(1-x)

#variable initialization
epoch = 50000
lr = 0.1
inputlayer_neuron = X.shape[1]
hiddenlayer_neuron1 = 3
hiddenlayer_neuron2 = 3
output_neuron = 1

#weight an d bias initialization
wh = np.random.random((inputlayer_neuron,hiddenlayer_neuron1))
wh1 = np.random.random((hiddenlayer_neuron1,hiddenlayer_neuron2))
wout = np.random.random((hiddenlayer_neuron2,output_neuron))

#bias initialization
bh = np.random.random((1,hiddenlayer_neuron1))
bh1 = np.random.random((1,hiddenlayer_neuron2))
bout = np.random.random((1,output_neuron))

for i in range(epoch):

	#froward propagation
	hiddenlayer1_input = np.dot(X,wh)
	hiddenlayer1_input1 = hiddenlayer1_input + bh
	hiddenlayer1_activation = sigmoid(hiddenlayer1_input1)

	hiddenlayer2_input = np.dot(hiddenlayer1_activation,wh1)
	hiddenlayer2_input2 = hiddenlayer2_input + bh1
	hiddenlayer2_activation = sigmoid(hiddenlayer2_input2)

	output_layer_input = np.dot(hiddenlayer2_activation,wout)
	output_layer_input1 = output_layer_input + bout
	output = sigmoid(output_layer_input1)

	#backward propagation
	error =  y - output
	slope_of_output_layer = derivative_sigmoid(output)
	delta_output = error * slope_of_output_layer

	error_of_hiddenlayer2 = delta_output.dot(wout.T)
	slope_of_hiddenlayer2 = derivative_sigmoid(hiddenlayer2_activation)
	delta_hiddenlayer2 = error_of_hiddenlayer2*slope_of_hiddenlayer2

	error_of_hiddenlayer1 = delta_hiddenlayer2.dot(wh1.T)
	slope_of_hiddenlayer1 = derivative_sigmoid(hiddenlayer1_activation)
	delta_hiddenlayer1 = error_of_hiddenlayer1*slope_of_hiddenlayer1

	#updating weights
	wh += (X.T).dot(delta_hiddenlayer1)*lr
	wh1 += (hiddenlayer1_activation.T).dot(delta_hiddenlayer2)*lr
	wout += (hiddenlayer2_activation.T).dot(delta_output)*lr

	#updating biasing
	bh += np.sum(delta_hiddenlayer1,axis = 0,keepdims = True)*lr
	bh1 += np.sum(delta_hiddenlayer2,axis = 0,keepdims = True)*lr
	bout += np.sum(delta_output,axis = 0,keepdims = True)*lr

print(output)
