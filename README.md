# GIS_Task
# Code (For Windows System):

1.	Ensure that Python is installed on your system. Open a command prompt (preferably as administrator) or terminal and type:
   
         python3 –version
  	
  	If Python is not installed, you need to install it from python.org
  
3.	Check if pip is installed:
   
         python -m pip –version
  	
   •	If pip is not installed, you can install it by downloading get-pip.py and running it:
  	
       •	Go to https://bootstrap.pypa.io/get-pip.py (its a binary code). Copy it in command terminal and run it.

       •	Now, run the following command in terminal: python get-pip.py
  	
4.	If Python and pip are installed but not recognized, you need to add them to your system’s PATH:
   
         •	In the System Properties window, click on the “Environment Variables”.
     	
         •	In the Environment Variables window, select the Path variable in the “System variables” section and click the “Edit” button.
     	
         •	Click “New” and add the path to your Python installation. For example: C:\Python39\ (or wherever your Python installation is located)
     	
         •	Click “OK” to close all windows.
     	
  	
6.	Authenticate with Google Earth Engine. Run the following command in the terminal to authenticate your Google Earth Engine account (a new browser will open Earth Engine window, now log in using the credentials):
  	
          earthengine authenticate

7.	Install matplotlib Using pip (Run the following command to install matplotlib)
   
       •	If you are using python3 and pip3, the command would be:
     	
          pip3 install matplotlib
  	
       •	Verify Installation (To ensure that matplotlib is installed correctly), you can run:
     	
          python -c "import matplotlib.pyplot as plt; print('matplotlib is installed')"

Now run the python code


# Note:

# Avoid naming conflicts such as with library/syntax name.
# Make sure to replace the geojson file with the actual path to your downloaded GeoJSON file
# Set the start_date and end_date to your desired analysis period. 
