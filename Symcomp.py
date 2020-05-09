import matplotlib.pyplot as plt
import numpy as np
import math
import cmath

#Input Values
phaseA = [1.65, 46.8]
phaseB = [1.32, -67]
phaseC = [1.56, -121]

#Function takes two arguments as magnitude and angle and converts them to a complex number
def deg_car(mag, ang):                    
    x = mag * math.cos(math.radians(ang))
    y = mag * math.sin(math.radians(ang))
    return(complex(x, y))


def plotting(xs, ys, x, y, c):
    plt.quiver(xs, ys, x, y, angles='xy', scale_units='xy',
               scale=1, width=0.005, color=c)
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    
#calling the function to convert the phase values from degrees to cartesian co-ordinates
phaseAcar = deg_car(phaseA[0], phaseA[1])
phaseBcar = deg_car(phaseB[0], phaseB[1])
phaseCcar = deg_car(phaseC[0], phaseC[1])


# a operator 1<120
a = complex(-0.5+0.866j)
a2= a*a
# Symmetrical Components A Matrix
A = np.array([[1, 1, 1],
              [1, a**2, a],
              [1, a, a**2]], dtype=complex)

# calculates the inverse of the A matrix
Ainv = np.linalg.inv(A)  

# creates a 3x1 matrix
sys = np.array([[deg_car(phaseA[0], phaseA[1])],
                [deg_car(phaseB[0], phaseB[1])],
                [deg_car(phaseC[0], phaseC[1])]])

# calculated symmetrical components
sym = Ainv.dot(sys)  


plotting(0, 0, phaseAcar.real, phaseAcar.imag, 'red')
plotting(0, 0, phaseBcar.real, phaseBcar.imag, 'yellow')
plotting(0, 0, phaseCcar.real, phaseCcar.imag, 'blue')

plotting(0, 0, sym[1].real, sym[1].imag, 'black')
plotting(sym[1].real, sym[1].imag, sym[2].real, sym[2].imag, 'black')
plotting(sym[2].real+sym[1].real, sym[2].imag+sym[1].imag,
         sym[0].real, sym[0].imag, 'black')


plt.show()

print(sym[0])
print(sym[1])
print(sym[2])
