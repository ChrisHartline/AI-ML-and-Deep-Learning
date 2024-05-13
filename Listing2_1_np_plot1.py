import numpy as np
import matplotlib.pyplot as plt

x = np.random.rand(15,1) # 15 random numbers
y = 2.5*x + 5 + 0.2*np.random.randn(15,1) # y = 2.5x + 5 + noise 

print("x: ", x) # print x
print("y: ", y) # print y

plt.scatter(x, y) # scatter plot
plt.show() # show plot    
