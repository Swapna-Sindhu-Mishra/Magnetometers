"""
Inputs: *.dat files generated by MPMS3.
Parameters: folderpath, subfolder
Outputs: *.dat files containing Temperature (T) and VSM Moment (M) in a subfolder.
"""
folderpath = 'C:/Users/mishra/Downloads/MPMS3' #Location of inputs
subfolder = 'MT_Extracted' #Subfolder name for output files+
headers = 45

import numpy as np #For creating data arrays
import os #For changing and creating folders
import shutil #For deleting folders already present
import glob #For batch importing files

os.chdir(folderpath) #Changes working directory to folderpath
shutil.rmtree(subfolder, ignore_errors=True) #Deletes subfolder if already present
os.mkdir(subfolder) #Creates subfolder
files = glob.glob('*.dat') #Imports filenames with .dat extension
filecount = len(files) #Counts number of filenames imported

print(f'The following {filecount} files will be processed:')
print(files) #Prints the names of all imported filenames
for i in range(filecount): #Loops through all files
    data_raw = np.loadtxt(files[i], delimiter=',', skiprows=headers, usecols=[2,4]) #Load column 2 (T) and 4 (M) from MPMS3 file
    data = np.column_stack((data_raw[:,0],data_raw[:,1])) #Makes an array of T and M data
    #Save files
    filename = ''.join(files[i].split())[:-4] #Removes last 4 characters (.dat) from filename
    filepath = f'{folderpath}/{subfolder}/{filename}_{subfolder}.dat' #Location for saving M-T data
    np.savetxt(filepath, data) #Saves M-T data in subfolder
    
print("All files were extracted and saved in subfolder.")