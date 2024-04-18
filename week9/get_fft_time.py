import numpy as np
import scipy.io as sio
import scipy.io.wavfile
import matplotlib.pyplot as plt
import argparse 
from scipy import fftpack
import time

parser = argparse.ArgumentParser()
parser.add_argument('--filename', required=False, default='filename.wav')
args = parser.parse_args()

print("drawing plot for", args.filename)

samplerate, data = sio.wavfile.read(args.filename)
fftsize = len(data)

# Record the start time
start_time = time.time()

data_fft = fftpack.fft(data, fftsize)

# Record the end time
end_time = time.time()

# Calculate the time taken for FFT
duration = end_time - start_time
print("Time taken for FFT:", duration, "seconds")
