from . import device_list


class Beamline :
    def __init__(self) :
        self.components = [] 

    # Allow devices to be dynamically added to beamline, so they can
    # be accessed by Beamline.device notation
    def add_device(self, device, location) :
        # check if device object exits
        if device_list.has_key(device) :
            self.components.append( (device_list[device],location) )
        else :
            print device,"has not been defined"

        
    def __repr__(self) :
        desc_string = "[ "
        for comp in self.components :
            desc_string = desc_string + \
                          "(" + comp[0].name + "," + str(comp[1]) + "),"
        desc_string = desc_string + " ]"

        return desc_string

    
            

