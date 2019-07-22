import numpy as np
import random as rand

class NeuralNetwork:
    lr = 0.1

    def randWeights(self, weights):
        for i in range(weights.shape[0]):
            for j in range(weights.shape[1]):
                weights[i][j] = rand.random()
    
    def __init__(self, num_inputs, num_hiddens, num_outputs):
        self.num_inputs = np.array(num_inputs)
        self.num_hiddens = np.array(num_hiddens)
        self.num_outputs = np.array(num_outputs)

        # Weights from input to hidden, or hidden to output
        # Each row is the recieving node, each column is the sending node
        self.weights_ih = np.zeros((num_hiddens, num_inputs))
        self.weights_ho = np.zeros((num_outputs, num_hiddens))
        # self.weights_ih = np.arange(num_hiddens * num_inputs).reshape(num_hiddens, num_inputs)
        # self.weights_ho = np.arange(num_outputs * num_hiddens).reshape(num_outputs, num_hiddens)
        # self.weights_ih = self.weights_ih.astype(float)
        # self.weights_ho = self.weights_ho.astype(float)


        self.randWeights(self.weights_ih)
        self.randWeights(self.weights_ho)

    def sigmoidAll(self, array):
        # Casts all values to floats, otherwise the values might just all become 0
        array = array.astype(float)
        for i in range(array.shape[0]):
            # Sigmoid is 1 / (1 + e^(-x))
            array[i] = 1 / (1 + np.e**-array[i])
        
        return array
    
    def feedForward(self, inputs):
        hiddens = np.dot(self.weights_ih, inputs) # Matrix multiplication of weights and inputs
        hiddens = self.sigmoidAll(hiddens) # Activation function
        outputs = np.dot(self.weights_ho, hiddens) # Matrix multiplication of weights and inputs
        outputs = self.sigmoidAll(outputs) # Activation function

        return outputs

    def transpose_1d(self, array):
        return array.reshape(array.size, 1)

    def train(self, inputs, targets):
        # Repeating feedForward() code to get hiddens array
        hiddens = np.dot(self.weights_ih, inputs)
        hiddens = self.sigmoidAll(hiddens)
        outputs = np.dot(self.weights_ho, hiddens)
        outputs = self.sigmoidAll(outputs)

        errors_o = targets - outputs

        # Adjusting weights_ho
        gradients = outputs * (1 - outputs) # dSigmoid
        gradients *= errors_o
        gradients *= self.lr
        dW_ho = np.dot(self.transpose_1d(gradients), hiddens.reshape(1, hiddens.size)) # Change in weights between hidden and output
        self.weights_ho += dW_ho

        # Adjusting weights_ih
        errors_h = np.dot(np.transpose(self.weights_ho), errors_o) # Comes out horizontal
        gradients_h = hiddens * (1 - hiddens) # dSigmoid
        gradients_h *= errors_h
        gradients_h *= self.lr
        dW_ih = np.dot(self.transpose_1d(gradients_h), inputs.reshape(1, inputs.size))
        self.weights_ih += dW_ih

if __name__ == "__main__":
    nn = NeuralNetwork(2, 3, 2)
    inputs = np.array([1, 2])
    original = nn.feedForward(inputs)

    for i in range(10000):
        nn.train(inputs, [1, 0])
    print(original)
    print(nn.feedForward(inputs))
# Add bias
# sigmoidAll might be unnecessary?