#!/usr/bin/python

import math
import sys
import subprocess
import numpy as np

print "usage: python <program.py> <Infile>.pdb  <CA>"

def ReadFile(pdbfile, atreg):
    xcoor=[]
    ycoor=[]
    zcoor=[]
    for line in open(pdbfile):
        if line.startswith('ATOM'):
            line = line.split()
            name = line[2]
            if name == atreg:
                X_coordinates=line[5]
                Y_coordinates=line[6]
                Z_coordinates=line[7]
                #print X_coordinates, Y_coordinates, Z_coordinates
                xcoor.append(X_coordinates)
                ycoor.append(Y_coordinates) 
                zcoor.append(Z_coordinates)
    return (xcoor, ycoor, zcoor)

def GetDistance(xcoor, ycoor, zcoor):
    dist= []
    for i in range(0,len(xcoor)):
        for j in range(0,i):
            x_dist= (float(xcoor[i])-float(xcoor[j]))**2
            y_dist= (float(ycoor[i])-float(ycoor[j]))**2
            z_dist= (float(zcoor[i])-float(zcoor[j]))**2
            distance= math.sqrt(x_dist + y_dist + z_dist)
            dist.append(distance)
    return dist


def GetDistanceMatrix(xcoor, ycoor, zcoor):
    m = len(xcoor)
    dist = np.zeros((m,m), dtype=float )

    for i in range(0,len(xcoor)):
        for j in range(0,i):
            x_dist= (float(xcoor[i])-float(xcoor[j]))**2
            y_dist= (float(ycoor[i])-float(ycoor[j]))**2
            z_dist= (float(zcoor[i])-float(zcoor[j]))**2
            distance= math.sqrt(x_dist + y_dist + z_dist)
            dist[i][j] = distance
    return dist



if __name__ == '__main__':
    ff = open("TempFile", 'w')
    
    pdbfile=sys.argv[1]
    atreg = sys.argv[2]
    xpoints, ypoints, zpoints=ReadFile(pdbfile, atreg)
    dist=GetDistanceMatrix(xpoints, ypoints, zpoints)
    

    ff.write("#CA-CA distance\n")
    for i in dist:
        ff.write (str(i)+ '\n')

    ff.close()


