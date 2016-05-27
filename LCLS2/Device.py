class Device :
    def __init__(self,device_name) :
        self.name = device_name
        pass

    # Allow components to be dynamically added to Device, so they can
    # accessed by Device.component notation
    def add_component(self,component, quantity) :
        # Check if component already exisits
        try:
            if getattr(self, component) :
                print component,"already exists"
                                
        except AttributeError :
            # Attribute doesn't exist .. add it
            setattr(self, component, quantity)


    # Equality test
    def __eq__(self, testobj) :
        # Check testobj is instance of Device class
        if isinstance(testobj,self.__class__) == False:
            return False

        # check all attributes are identical
        for attr,value in testobj.__dict__.iteritems() :
            if attr == "name" :
                continue
            if getattr(self,attr) != value :
                return False
        
        # got here...everything matched
        return True


