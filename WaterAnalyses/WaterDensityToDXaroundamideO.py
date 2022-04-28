import numpy as np

ogdata = np.loadtxt("mVFj.gr3")
youngdata = np.zeros(27000000,dtype=float)
count = -1
amideO = [-0.549745, 1.154656, -2.199856]
for x in range(len(ogdata)):
    count+=1
    #if -14.95 <= ogdata[x,0] < 15.00:
    #    if -14.95 <= ogdata[x,1] < 15.00: 
    #        if -14.95 <= ogdata[x,2] < 15.00:
    if float(amideO[0] - 2.85) <= ogdata[x,0] < float(amideO[0] + 2.86):
        if float(amideO[1] - 2.86) <= ogdata[x,1] < float(amideO[1] + 2.86): 
            if float(amideO[2] - 2.86) <= ogdata[x,2] < float(amideO[2] + 2.86):
                youngdata[count]=ogdata[x,3]
print count 
np.savetxt("waterdxaroundamideO.dx",youngdata)
reshaped = np.reshape(youngdata, (len(youngdata)/3,3))
np.savetxt("reshapedwaterdxaroundamideO.dx",reshaped)



#vol=np.loadtxt("tempvolmap.dx")
#wat=np.loadtxt("tempreshaped.dx")
#prod=np.zeros((len(vol),3),dtype=float)
#for i in range(len(vol)):
#    for j in range(3):
#        prod[i,j]=vol[i,j]*wat[i,j]
#np.savetxt("newdx.dx", prod)

