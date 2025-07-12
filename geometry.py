#Libraries
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import math
from math import sqrt
import inquirer
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.tri import Triangulation

# Select which 3D shape 
questions = [
        inquirer.List('volume',
                      message="Which shape do you want to use?",
                      choices=['Sphere', 'Pyramid', 'Cube', 'Cone', 'Cylinder']),]
answers = inquirer.prompt(questions)
print(answers["volume"])
choice=answers["volume"]
if choice == 'Sphere':
   # put additional questions for area, volume
   r=float(input("Enter a radius of the sphere: "))
   phi, theta = np.mgrid[0:2*np.pi:50j, 0:np.pi:50j]
   V=4/3*math.pi*(r**3)   
   SA=4*np.pi*(r**2)
   print("The surface area of the sphere is: ", SA)
   print("The volume of the sphere is: ",V)
   x=r*np.sin(phi)*np.cos(theta)
   y=r*np.sin(phi)*np.sin(theta)
   z=r*np.cos(phi)
   fig = plt.figure()
   ax = plt.axes(projection='3d')
   ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8, edgecolor='green')
   ax.set_title('Sphere')
   ax.set_box_aspect((np.ptp(x), np.ptp(y), np. ptp(z)))
   plt.show()
elif choice == 'Pyramid':
   l=float(input("Enter a base length: "))
   w=float(input("Enter a base width: "))
   h=float(input("Enter a base height: "))
   V=(l*w*h)/3
   SA=l*w+(l*(np.sqrt(((w/2)**2)+(h**2))))+(w*(np.sqrt(((l/2)**2)+(h**2))))
   print("The surface area of the right rectangular pyramid is: ", SA)
   print("The volume of the right rectangular pyramid is: ",V)
   # define vertices
   v= np.array([[0, 0, 0], [l, 0, 0], [l, w, 0], [0, w, 0],[l/2, w/2, h]])
   # define faces
   faces = [[v[0], v[1], v[2], v[3]], [v[0], v[1], v[4]], [v[1], v[2], v[4]], [v[2], v[3], v[4]], [v[3], v[0], v[4]]]
   fig = plt.figure()
   ax = fig.add_subplot(111,projection='3d')
   poly3d = Poly3DCollection(faces, facecolors='cyan', linewidths=1, edgecolors='r', alpha =0.6)
   ax.add_collection3d(poly3d)
   ax.set_title('Pyramid')
   ax.set_label('X')
   ax.set_label('Y')
   ax.set_label('Z')
   gt=max(l,w,h)
   ax.set_xlim([0, gt+1])
   ax.set_ylim([0, gt+1])
   ax.set_zlim([0, gt+1])
   ax.set_box_aspect([1,1,1])
   plt.show()
elif choice == 'Cube':
   a=float(input("The side length of the cube is: "))
   V=a*a*a
   SA=6*a**2
   print("The surface area of the cube is: ", SA)
   print("The volume of the cube is: ",V)
   x=[0,a,a,0,0,a,a,0]
   y=[0,0,a,a,0,0,a,a]
   z=[0,0,0,0,a,a,a,a]
   vertices=[[0,1,2,3],[1,5,6,2],[3,2,6,7],[4,0,3,7],[5,4,7,6],[4,5,1,0]]
   tupleList = list(zip(x, y, z))
   poly3d = [[tupleList[vertices[ix][iy]] 
   for iy in range(len(vertices[0]))] for ix in range(len(vertices))]
   fig = plt.figure()
   ax = fig.add_subplot(111, projection='3d')
   ax.scatter(x,y,z)
   ax.add_collection3d(Poly3DCollection(poly3d, facecolors='r', linewidths=1, alpha=0.5))
   ax.set_title('Cube')
   ax.set_label('X')
   ax.set_label('Y')
   ax.set_label('Z')
   ax.set_xlim([0, a+1])
   ax.set_ylim([0, a+1])
   ax.set_zlim([0, a+1])
   ax.set_box_aspect([1,1,1])
   plt.show()
elif choice == 'Cone':
   radius=float(input("Enter a radius: "))
   h=float(input("Enter the height of the right cylinder cone: "))
   V=math.pi*(radius**2)*(h/3)
   SA=np.pi*r*(r+(np.sqrt((h**2)+(r**2))))
   print("The surface area of the cone is: ", SA)
   print("The volume of the cone is: ",V)
   num_points =50
   theta=np.linspace(0, 2*np.pi, num_points)
   r = np.linspace(0, radius, num_points)
   theta_grid, r_grid = np.meshgrid(theta,r)
   X=r_grid * np.cos(theta_grid)
   Y=r_grid * np.sin(theta_grid)
   Z= (h/radius) * r_grid
   fig = plt.figure()
   ax = fig.add_subplot(111,projection='3d')
   ax.plot_surface(X, Y, Z, color='skyblue', alpha=0.8)
   ax.set_title('Cone')
   ax.set_xlabel('X axis')
   ax.set_ylabel('Y axis')
   ax.set_zlabel('Z axis')
   gt=max(r,h)
   ax.set_xlim([0, gt+1])
   ax.set_ylim([0, gt+1])
   ax.set_zlim([0, gt+1])
   ax.set_box_aspect([1,1,1])
   plt.show()
elif choice == 'Cylinder':
   r=float(input("Enter a radius for the right cylinder: "))
   h=float(input("Enter the height for the right cylinder: "))
   V=math.pi*(r**2)*h
   SA=(2*np.pi*r*h)+(2*np.pi*(r**2))
   print("The surface area of the cylinder is: ", SA)
   print("The volume of the cylinder is: ",V)
   theta=np.linspace(0, 2*np.pi, 100)
   z=np.linspace(0,h, 50)
   theta, z=np.meshgrid(theta,z)
   x=r*np.cos(theta)
   y=r*np.sin(theta)
   fig = plt.figure()
   ax = fig.add_subplot(111,projection='3d')
   ax.plot_surface(x, y, z, cmap='viridis', edgecolor='green')
   ax.set_title('Cylinder')
   ax.set_xlabel('X axis')
   ax.set_ylabel('Y axis')
   ax.set_zlabel('Z axis')
   gt=max(r,h)
   ax.set_xlim([0, gt+1])
   ax.set_ylim([0, gt+1])
   ax.set_zlim([0, gt+1])
   ax.set_box_aspect([1,1,1])
   plt.show()
