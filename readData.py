import pylab as plt

f = open("texto.txt", 'r')



trial = f.read().split()
print(trial)



category = []
for i in trial[0::2]:
    cleanedup = i.replace('=','')
    category.append(cleanedup)

values = trial[1::2]
print(category)
print(values)
'''intenta separar lo numerico'''


plt.plot()