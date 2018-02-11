import numpy as np
import ugradio

def collect_data(v, div, dualmode = True, nbloc = 1, nsamp = 16000):
    '''
    Collects and saves data from A and B port of pico sampler. Uses ugradio.pico.capture_data().

    Arguments:
    filename: (string) the name of file
    v: (string) volt_range same as pico.capture_data
    div: (int) Divide the 62.5 MHz sample clock by this number for sampling
    dual_mode: (bool) samples from both A and B. If False, samples only from A.
    nbloc: (int) number of blocks (each with nsample data points)
    nsamp: (int) number of samples. default is 16000
    
    Returns:
    Statement that data is saved to name of files
    '''

    A = ugradio.pico.capture_data(v, divisor = div, dual_mode = dualmode, nsamples = nsamp, nblocks = nbloc)[:nsamp]
    B = ugradio.pico.capture_data(v, divisor = div, dual_mode = dualmode, nsamples = nsamp, nblocks = nbloc)[nsamp:]
    np.savetxt('data_A.txt', A)
    np.savetxt('data_B.txt', B)
    print('Saved A port data to data_A')
    print('Saved B port data to data_B')
    return [A, B]

'''def fft_power(arrA =None, arrB=None,jkdfio):
    if arrA == None:
        # go get the data form the pico sampler
    if arrB == None:
        # go get B data from pico
    
'''