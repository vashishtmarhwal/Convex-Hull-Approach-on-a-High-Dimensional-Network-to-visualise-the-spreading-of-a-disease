
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def RightTurn(p1, p2, p3):
	if (p3[1]-p1[1])*(p2[0]-p1[0]) >= (p2[1]-p1[1])*(p3[0]-p1[0]):
		return False
	return True
	
def GrahamScan(P):
	P.sort()			
	L_upper = [P[0], P[1]]		
	for i in range(2,len(P)):
		L_upper.append(P[i])
		while len(L_upper) > 2 and not RightTurn(L_upper[-1],L_upper[-2],L_upper[-3]):
			del L_upper[-2]
	L_lower = [P[-1], P[-2]]	
	
	for i in range(len(P)-3,-1,-1):
		L_lower.append(P[i])
		while len(L_lower) > 2 and not RightTurn(L_lower[-1],L_lower[-2],L_lower[-3]):
			del L_lower[-2]
	del L_lower[0]
	del L_lower[-1]
	L = L_upper + L_lower		
	return np.array(L)

df = pd.read_csv('U.S._Chronic_Disease_Indicators.csv')
df = df.fillna(0)
P = []
print("Into Data")
for i in range(len(df)):
    if((df['GeoLocation'][i] != 0) and (df['Unnamed: 23'][i][:-1]!=0) and ((float(df['GeoLocation'][i][1:]),float(df['Unnamed: 23'][i][:-1])) not in P)):
        x, y = float(df['GeoLocation'][i][1:]), float(df['Unnamed: 23'][i][:-1])
        P.append((x,y))
print("Data Ready")



	
print("Into Algo")
L = GrahamScan(P)
P = np.array(P)
print(P)
plt.figure()
plt.plot(L[:,0],L[:,1], 'b-', picker=5)
plt.plot([L[-1,0],L[0,0]],[L[-1,1],L[0,1]], 'b-', picker=5)
plt.plot(P[:,0],P[:,1],".r")
plt.axis('off')
plt.grid()
plt.show()
