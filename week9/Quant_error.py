import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt
import argparse 

parser = argparse.ArgumentParser()
parser.add_argument('--stu_id', required=True, default='20232108')
args = parser.parse_args()

last_digit = int(args.stu_id[-1])

BW1 = last_digit + 1
BW2 = 10 - last_digit

def quantization_error(BitWidth):
    # generating x from 0 to 4pi and y using numpy library
    x = np.arange(0, 4 * np.pi, 0.1)  # start, stop, step
    y = np.sin(x)
    data = y
    print("Quantization in:", BitWidth, "bit")

    # Calculate scale factor for quantization
    max_val = np.max(data)
    min_val = np.min(data)
    levels = 2 ** BitWidth
    Scale_factor = (max_val - min_val) / (levels - 1)

    # Quantize data using scale factor
    Quantized_value = np.round((data - min_val) / Scale_factor) * Scale_factor + min_val

    # Calculate error caused by quantization
    Error = np.sum(np.abs(Quantized_value - data))

    # Plotting sine curve and its quantized version using matplotlib
    print('Error for {0} bit quantization: {1:.2f}'.format(BitWidth, Error))
    plt.figure()
    plt.plot(x, y, label='Original')
    plt.plot(x, Quantized_value, label='Quantized', linestyle='--')
    plt.title('Quantization: {} bits'.format(BitWidth))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.show()

quantization_error(BW1)
quantization_error(BW2)
