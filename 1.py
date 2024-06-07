def convolution(x, h):
    """
    
    
    :param x: 
    :param h: 
    :return: 
    """
    N = len(x)
    M = len(h)
    y = [0] * (N + M - 1)  

    for n in range(N + M - 1):
        for k in range(max(0, n - M + 1), min(N, n + 1)):
            y[n] += x[k] * h[n - k]

    return y


x = [1, 2, 3, 4]
h = [0.5, 0.25, 0.1]

result = convolution(x, h)
print(result)
