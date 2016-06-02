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
        if device in device_list :
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
        count_list = {}
        for dev in self.devices :
            if count_list.has_key(dev[0].name) :
                count_list[dev[0].name] += 1
            else :
                count_list[dev[0].name] = 1
        return count_list

    def count_components(self) :
        count_list = {}
        for dev in self.devices :
            dev_count = dev[0].count()

            for key,val in dev_count.iteritems() :
                if count_list.has_key(key) :
                    count_list[key] += val
                else :
                    count_list[key] = val

        return count_list
