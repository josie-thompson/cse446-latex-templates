import numpy as np
import matplotlib.pyplot as plt

phi = (1 + np.sqrt(5))/2 + 0j # golden ratio as a complex number
def fib(n):
    """The n^th fibbonacci number"""
    return (phi**n - (-phi)**(-n))/np.sqrt(5)

def main():
    N_negative = np.linspace(-10, 0, 200)
    N_positive = np.linspace(0, 4.5, 200)

    fib_negative_n = np.array(list(map(fib, N_negative)))
    fib_positive_n = np.array(list(map(fib, N_positive)))

    plt.figure(figsize=(6.4,4.8)) # image size: 640x480 pixels
    plt.plot(np.real(fib_negative_n), np.imag(fib_negative_n))
    plt.savefig('fibonacci-negative-n.png')

    plt.clf() # clear the figure
    plt.figure(figsize=(7.2,4.8)) # make the image longer
    plt.plot(np.real(fib_positive_n), np.imag(fib_positive_n))
    plt.savefig('fibonacci-positive-n.png')

if __name__ == '__main__':
    main()
