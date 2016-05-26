# Collections of functions to import data to build a beamline

import pandas as pd

from . import Device
from . import device_list

import re

def from_excel(excel_file) :

    data_df = pd.read_excel(excel_file,
                            sheetname="Controlled Devices",
                            header=1,skiprows=0,
                            parse_cols="A:D,H,L:BU")

    # Convert all NAN to zero
    data_df.fillna(0, inplace=True)

    # Go through all device names and remove spaces, parentheses, and
    # periods and replace with underscore

    # Go through each row to create devices
    def create_device(s, headers) :
        print "In create device"
                
        dev = Device(s['Instrument'])

        print "input data",s


        print "About to loop"
        for col in headers[5:-1] :
            print col, s[col]
            dev.add_component(col, s[col])

        return dev

    print "About to start apply"
    
    # Replace unicode character u'\u2026' with underscore
    data_df.columns = [ re.sub(u'\u2026','_',s) for s in data_df.columns]
    data_df.columns = [ re.sub(r'-(\d+k)','neg\g<1>',s) for s in data_df.columns]
    data_df.columns = [ re.sub(r'<','lt',s) for s in data_df.columns]
    data_df.columns = [ re.sub(r'\s+','_',s) for s in data_df.columns]

    # Go through each row and create an instance of the Device object
    data_df['device'] = data_df.apply(create_device,axis=1,
                                      headers=data_df.columns )


    # Go through each row and build out beamline and device unique
    # devices.
    # - For unique devices, take a row to define an instance of Device
    #   Go through global device list and check it is unique
    #   If there's a collision in names append
    #      - beamline
    #      - append a number, starting from 2
    # - For uniqueness, need to define custom comparison function
    #     add __eq__ and __ne__ to Device
    # - as global device list is a dictionary, use new-instance Device
    # name to look for key in global device list
    #    - then do comparison.
    #    if same, then just used the global version
    #    if different, then create unique name and add to list    
    #

    # Go through devices and find all unique occurances.
    # those with same name, add additional info to make then unique
            
    return data_df




    

    
