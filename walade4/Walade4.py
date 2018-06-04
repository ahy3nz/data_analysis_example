import numpy as np
import matplotlib.pyplot as plt
info = 'temp.xvg'

data = np.loadtxt(info, comments=['#','@'], delimiter=None, converters=None, skiprows=0)
data1 = data[:,1]
data2 = data[:,2]

dev1 = np.std(data[:,1])
dev2 = np.std(data[:,2])

mean1 = np.mean(data[:,1])
mean2 = np.mean(data[:,2])
data3 = np.random.normal(loc=mean1, scale=dev1,size = 46000)
plt.hist(data1, 8, label= 'Temperature Distribution',alpha=0.6, density=True)
plt.hist(data3, 8, label= 'Normal Distribution', alpha=0.6, density= True)
plt.xlabel('Temperature')
plt.ylabel('Probability')
plt.title('$\mu=305.0K$, $\sigma=3.72K$')
plt.show()

