import numpy as np
from matplotlib import pyplot as plt

AR = 8 # Guess

CL = np.linspace(0, 1.0, 100)

CD0 = 0.02 # Zero lift drag coeff

e = 0.85 #Ostxald's efficiency factor
CD = CD0 + CL*CL / (np.pi * AR * 0.85) # (ZLD + Ind drag)

CL_CD = CL / CD
# Trouver l'indice du maximum de CL/CD
max_index = np.argmax(CL_CD)

# Extraire le CL correspondant au maximum de CL/CD
CL_max = CL[max_index]
CL_CD_max = CL_CD[max_index]

# Afficher les résultats
print(f"Le maximum de CL/CD est {CL_CD_max:.2f} pour CL = {CL_max:.2f}")


plt.plot(CL, CL/CD)
plt.xlabel('$CL$')
plt.ylabel('$CL/CD$')
plt.show()



# a (CL_alpha) 

#CL = CL_alpha * (alpha - alpha_L0)
