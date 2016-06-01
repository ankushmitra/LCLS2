from . import device_list


class Beamline :
    """
    A beamline is composed of devies.
    Thus the beamline class has an internal list of devices
    """
    
    def __init__(self) :
        self.devices = [] 

    # Allow devices to be dynamically added to beamline, so they can
    # be accessed by Beamline.device notation
    def add_device(self, device, location) :
        # check if device object exits
        if device_list.has_key(device) :
            self.devices.append( (device_list[device],location) )
        else :
            print device,"has not been defined"

        
    def __repr__(self) :
        desc_string = "[ "
        for dev in self.devices :
            desc_string = desc_string + \
                          "(" + dev[0].name + "," + str(dev[1]) + "),"
        desc_string = desc_string + " ]"

        return desc_string


    def count_devices(self) :
        pass
        
    

