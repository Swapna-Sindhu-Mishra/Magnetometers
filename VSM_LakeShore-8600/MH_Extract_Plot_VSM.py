"""
Inputs: *.csv files generated by VSM placed in folderpath. Background correction should be made before, if required.
Parameters: folderpath, data_subfolder, plot_subfolder, headers
Outputs: Field(H) & Moment(M) data in corresponding *_MH.dat files in data_subfolder. Corresponding M vs H plots in a data_subfolder.
"""
folderpath = 'C:/Users/mishra/Downloads/VSM' #Location of inputs
data_subfolder = 'MH_Data' #Subfolder name for MH Data
plot_subfolder='MH_Plot' #Subfolder name for MH Plots
headers=50 #Number of headers in VSM data file i.e lines to ignore when importing

import numpy as np #For importing data
import matplotlib.pyplot as plt #For plotting data
import matplotlib.ticker as tick #For scientific format in axis ticklabels
import os #For changing and creating folders
import shutil #For deleting folders already present
import glob #For batch importing files

os.chdir(folderpath) #Changes working directory to folderpath
shutil.rmtree(data_subfolder, ignore_errors=True) #Deletes data_subfolder if already present
shutil.rmtree(plot_subfolder, ignore_errors=True) #Deletes plot_subfolder if already present
os.mkdir(data_subfolder) #Creates data_subfolder
os.mkdir(plot_subfolder) #Creates plot_subfolder
files = glob.glob('*.csv') #Imports filenames with .csv extension
filecount = len(files) #Counts number of files present in folderpath

print(f'The following {filecount} files will be processed:')
print(files) #Prints name of all files to be processed

for i in range(filecount): #Loops through all files
    #MH data processing
    data_raw = np.loadtxt(files[i], delimiter=',', skiprows=headers, usecols=[3,4]) #Loads column 3 (H) & 4 (M) from .csv file
    data = np.column_stack((data_raw[:,0],data_raw[:,1])) #Creates an array of MH data
    MH_filename = ''.join(files[i].split())[:-4] #Removes last 4 characters (.csv) from filename.
    MH_filepath = f'{folderpath}/{data_subfolder}/{MH_filename}_MH.dat' #Creates name and location of output
    np.savetxt(MH_filepath, data, delimiter='\t') #Saves extracted MH data in subdirectory
    #MH plotting
    #plt.title(f'{MH_filename}', fontsize=15) #Sets MH_filename as plot title
    #plt.figtext(.15, .8, f'{MH_filename}') #Adds MH_filename as text to plot
    plt.gca().yaxis.set_major_formatter(tick.FormatStrFormatter('%.1e')) #Scientific format for Y-axis
    plt.ylabel('Moment, $m$ (emu)', fontsize=15) #Sets Y label
    #plt.gca().xaxis.set_major_formatter(tick.FormatStrFormatter('%.1e')) #Scientific format for X-axis
    plt.xlabel('Field, $H$ (Oe)', fontsize=15) #Sets X label
    plt.plot(data_raw[:,0],data_raw[:,1], linewidth=1, color='b') #Line plot of MH data
    plt.scatter(data_raw[:,0],data_raw[:,1], s=5, color='r') #Scatter plot of MH data
    #plt.legend(loc='best', fontsize=10.5) #Adds legend to the plot
    plt.savefig(f'{folderpath}/{plot_subfolder}/{MH_filename}_MH.svg', bbox_inches='tight') #Saves plot as .svg
    #plt.savefig(f'{folderpath}/{plot_subfolder}/{MH_filename}_MH.png', bbox_inches='tight', dpi=300) #Saves plot as 300dpi .png
    plt.show() #Shows plot in python

print("All files were processed succesfully. MH data files and plots were saved.")