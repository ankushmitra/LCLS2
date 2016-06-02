# LCLS2
code to automate beamline buildout for LCLS2/LS2-I

For this code, I assume this hierarchy:
 - beamline is composed of devices
 - device is composed of components
 
For example, let's take the SXR beamline.
- the SXR beamline is composed of a MONO,COLLIMATOR,SLITS,IMAGER
- MONO is composed of 2 MOTORS, 2 ABSOLUTE_ENCODERS, 2 COLD_CATHODES
- SLITS is composed of 4 MOTORS, 2 RELATIVE ENCODERS, 2 COLD_CATHODES, 1 TURBO
- IMAGE is composed of 1 1KHz CAMERA

To run the test code, 
 - it assumes PANDAS is installed
  - this is true on PSANA machines
 - the components_list excel file is available

All the code is contained in the LCLS2 module
 - the LCLS2 module dictionary device_list is a list of all unique devices discovered
 
If you run the test code in ipython, you can use ipython 'tab' to see all the attributes of each device.

## todo...
 - ~~create a beamline_list that will have all the beamlines and how they are composed~~
 - Use read-in components list to generate _Excel File_ config 
 - check if PANDAS can read/write excel Formulas
 - 
