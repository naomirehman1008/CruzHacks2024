import numpy as np

conv_filter = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])



for i in range(10):
    input = np.floor(np.random.rand(3,3) * 255)
    output = np.dot(input, conv_filter)
    print(input)
    print(output)



