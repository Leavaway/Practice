#Start at 9:18
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import cm
words=['teams','work','companies','culture','reseach','leadership','management','organization','skills','together']
 
#ax=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
x_pos=np.arange(10)
ay=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
 
plt.bar
#fig=plt.figure()
plt.bar(x_pos,[33,31,28,24,20,18,17,12,11,11],color = cm.rainbow(np.linspace(0, 1, 10)),align = 'center',alpha = 1)
plt.xticks(x_pos,words)
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("high-frequency vocabulary")
 
# plt.show()
print(np.linspace(0, 1, 11))
print(np.arange(10))