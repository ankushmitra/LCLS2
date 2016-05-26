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

