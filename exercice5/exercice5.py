import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("DonneesProjetSR.csv")
x = data.iloc[0:len(data),0] #colonne population ville
y = np.array(data.iloc[0:len(data),1]) #colonne gain mensuel

plt.scatter(x,y,label="Nuage de Point ")
plt.legend()
plt.xlabel("Population en Millier")
plt.ylabel("Prix en Millier")
axes = plt.axes()
axes.grid()
axes.set_xlim(0)
#plt.title("couple ville en fonction de la population")

# question 2 : verification des coefficients du modele 
a,b = np.polyfit(x,y,1)
print("a =",a,"b =",b)

def predict(x):
    return a * x + b 


fy = predict(x)
plt.plot(x, fy, c='r',label="regression lineaire")
plt.legend()
plt.show()

