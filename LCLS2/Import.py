# Collections of functions to import data to build a beamline

import pandas as pd

from . import Device
from . import Beamline
from . import device_list
from . import beamline_list

import re



# Go through each row to create devices
def create_device(s, headers) :
#        print "In create device"

        dev = Device(s['Instrument'])
#        print "Created instance of Device",dev.name
        
        for col in headers[5:-1] :
            #print col, s[col]
            dev.add_component(col, s[col])
        
        
#        print "Does this device exist in global list ?"
        # Rather than check each device, a similar device should have
        # similar name
        # find all devices in global list that start with same name
        similar_devs = [d for d in device_list.keys() if dev.name in d]
#        print similar_devs
        
        # if the list is empty, found a new, unique device.
        # add it to the global list & return the device name
        if len(similar_devs) == 0 :
#            print "Found new unique device",dev.name
            device_list[dev.name] = dev
            return dev.name

#        print "Not unique device"

        # ...got here..so not a unique device..does it match a
        # previously defined device ?
        alt_dev = [d for d in similar_devs if dev == device_list[d]]
#        print "ALT_DEV",alt_dev
        
        if len(alt_dev) > 0 :
                # found dev matches a definition of similar device
                # return this name
 #               print dev.name,"is really",alt_dev[0]
                return alt_dev[0] 

        #...got here...found another definition of the current
        # device. Create a unique name for it.

#        print "Doesn't match...create unique name"

        # start by appending Source name and check this it's not
        # defined
        dev.name = dev.name + "_" + s['Source']
#        print "New Device name",dev.name

        alt_dev = [d for d in similar_devs if dev.name == d]
#        print "Alt Dev",alt_dev

        if len(alt_dev) == 0 :
            # new unique name found.  add it to global list and
            # return new device name
#            print "Found new unique name",dev.name
            device_list[dev.name] = dev
            return dev.name

        
#        print "Doesn't match...create unique name"
        #...got here.  Appending Source is not unqiue.  Now append
        # Line
        dev.name = dev.name + "_" + s['Line']
#        print "New Device name",dev.name

        alt_dev = [d for d in similar_devs if dev.name == d]
#        print "Alt Dev",alt_dev
        
        if len(alt_dev) == 0 :
            # new unique name found.  add it to global list and
            # return new device name
#            print "Found new unique name",dev.name
        
            device_list[dev.name] = dev
            return dev.name

        #...got here.  Appending Line is not unique. Now append Area
        dev.name = dev.name + "_" + s['Area']
#        print "New Device name",dev.name
        
        alt_dev = [d for d in similar_devs if dev.name == d]
#        print "Alt Dev",alt_dev
        
        if len(alt_dev) == 0 :
                # new unique name found.  add it to global list and
                # return new device name

#                print "Found new unique name",dev.name        
                device_list[dev.name] = dev
                return dev.name

        #...got here.  Appending Area is not unique.  Find a version
        # number and increment it        
        version_num = re.findall(r'\d+$',alt_dev[0])
#        print "Version Num",version_num

        if len(version_num) == 0 :
                # no version number. start with 2
                dev.name = dev.name + "_V2"
#                print "Adding",dev.name
                device_list[dev.name] = dev
                return dev.name
        else :
                # found version number..increment by 1
                version_num = int(version_num[0]) + 1
                dev.name = dev.name + "_V%d"%version_num
#                print "Adding",dev.name
                device_list[dev.name] = dev
                return dev.name

        
        
# Add device to beamline
def create_beamline(s) :

#    print beamline_list
#    print "Line:%s   Device:%s"%(s.Line,s.Device)
    
    if s.Line not in beamline_list :
        # Create beamline object & key
#        print "Appended",s.Line,"to beamline_list"
        beamline_list[s.Line] = Beamline()
                
    # Append Device to beamline using global device list    
    beamline_list[s.Line].add_device(s.Device,s["Z-Loc_(m)"])

#    print "Beamline List:",beamline_list
#    print "**********"




def from_excel(excel_file) :

    data_df = pd.read_excel(excel_file,
                            sheetname="Controlled Devices",
                            header=1,
                            skiprows=0,
                            parse_cols="A:D,H,L:BU")

    # Replace Instrument NaN/NA as "TBD"
    data_df.Instrument = data_df.Instrument.fillna("TBD")

    # Convert all NAN to zero
    data_df.fillna(0, inplace=True)
        
#    print "About to start apply"
    
    # Replace unicode character u'\u2026' with underscore
    # Go through all device names and remove spaces, parentheses, and
    # periods and replace with underscore
    data_df.columns = [ re.sub(u'\u2026','_',s) for s in data_df.columns]
    data_df.columns = [ re.sub(r'-(\d+k)','neg\g<1>',s) for s in data_df.columns]
    data_df.columns = [ re.sub(r'<','lt',s) for s in data_df.columns]
    data_df.columns = [ re.sub(r'\s+','_',s) for s in data_df.columns]

    # Go through each row and find all unique devices
    data_df['Device'] = data_df.apply(create_device,axis=1,
                                        headers=data_df.columns )


    # Go through each row and create beamlines
    data_df.apply(create_beamline,axis=1)
    
    
    return data_df




    

    
