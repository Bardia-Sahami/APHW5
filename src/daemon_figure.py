import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from time import sleep

fig = plt.figure(1)
fig.patch.set_facecolor('xkcd:red')

# image 1
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8], frame_on = False)
img = mpimg.imread('../resources/image.jpeg')
imgplot = ax.imshow(img)

# image 2
img2 = img.copy()
img2[:, :, 0] = img2[:, :, 1] = img2[:, :, 2] = np.dot(img2, [0.8, 0.6, 0.6])
ax2 = fig.add_axes([0.5, 0.5, 0.5, 0.55], frame_on = False)
ax2.imshow(img2, aspect = 'equal')

# remove labels
ax.tick_params(axis='both', bottom = False, left = False, labelleft = False, labelbottom = False)
ax2.tick_params(axis='both', bottom = False, left = False, labelleft = False, labelbottom = False)

# text
text = '''
   DAEMON   
'''
props = dict(alpha = 1, facecolor = 'white')
ax.text(0.011, 0.015, text, transform = ax.transAxes, fontsize = 15, va = 'bottom', ha = 'left', bbox = props)

# function
x = np.linspace(0, 30, 300)
# y = np.cos(x+np.pi/8)
y = np.cos(x)
for i in range (32):
   y = np.cos(x+np.pi*(32-i)/8)
   ax3 = fig.add_axes([0.061, 0.3, 0.878, 0.2], frame_on = False)
   ax3.plot(x, y, 'k')
   ax3.tick_params(axis='both', bottom = False, left = False, labelleft = False, labelbottom = False)

   fig.savefig('test.pdf')
   sleep(0.1)
   ax3.remove()