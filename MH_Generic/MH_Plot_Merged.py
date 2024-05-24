"""
Inputs: *.dat files containing H and M columns separated by Tab. Background correction should be made before, if required.
Parameters: folderpath, plot_name, headers
Outputs: M vs H plots of all the *.dat files in a single figure saved in same folder.
"""
folderpath = 'C:/Users/mishra/Downloads/MPMS3/MH_Corrected' #Location of inputs
plot_name = 'Moment vs Field' #Name of the final plot
headers = 0 #Number of headers in MH data file i.e lines to ignore when importing

import numpy as np #For importing and manipulating data
import os #For changing and creating folders
import glob #For batch importing files
import matplotlib.pyplot as plt #For plotting figures
import matplotlib.ticker as tick #For scientific format in axis ticklabels

os.chdir(folderpath)#Changes directory to folderpath
files = glob.glob('*.dat') #Imports filenames with .dat extension
filecount = len(files)  #Counts number of files in folderpath

print(f'The following {filecount} files will be plotted together:')
print(files) #Prints name of all files to be plotted together

for i in range(filecount): #Loops through all files
    data = np.loadtxt(files[i], delimiter='\t', skiprows=headers, usecols=[0,1]) #Loads column 0 (H) & 1 (M) from .dat file
    label=files[i] #Defines filename as label for corresponding plot
    plt.scatter(data[:,0],data[:,1], s=5) #Scatter plot of MH data
    plt.plot(data[:,0],data[:,1], label=f'{label}', linewidth=1) #Lineplot of MH data
plt.title(f'{plot_name}', fontsize=15) #Sets plot_name as title
plt.gca().yaxis.set_major_formatter(tick.FormatStrFormatter('%.1e')) #Scientific format for Y-axis
plt.ylabel('Moment, $m$ (emu)', fontsize=15) #Sets Y label
#plt.gca().xaxis.set_major_formatter(tick.FormatStrFormatter('%.1e')) #Scientific format for X-axis
plt.xlabel('Field, $H$ (Oe)', fontsize=15) #Sets X label
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.5), fontsize=10) #Adds legend to the plot below X axis
#plt.savefig(f'{plot_name}.png', bbox_inches = "tight", dpi=300) #Saves plot as 300dpi .png
plt.savefig(f'{plot_name}.svg', bbox_inches = "tight") #Saves plot as .svg
plt.show() #Shows plot in python

print("All files were plotted and saved as a single figure succesfully.")