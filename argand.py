import matplotlib.pyplot as plt
from numpy import *


'''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
This draws the axis for argand diagram
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
'''
r = 1
Y = [r*exp(1j*theta) for theta in linspace(0,2*pi, 200)]
Y = array(Y)
plt.plot(real(Y), imag(Y), 'r')
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.axhline(y=0,color='black')
plt.axvline(x=0, color='black')


def argand(complex_number):
    '''
    This function takes a complex number.
    '''
    y = complex_number
    x1,y1 = [0,real(y)], [0, imag(y)]
    x2,y2 = [real(y), real(y)], [0, imag(y)]
    

    plt.plot(x1,y1, 'r') # Draw the hypotenuse
    plt.plot(x2,y2, 'r') # Draw the projection on real-axis

    plt.plot(real(y), imag(y), 'bo')

[argand(r*exp(1j*theta)) for theta in linspace(0,2*pi,100)]
plt.show()
