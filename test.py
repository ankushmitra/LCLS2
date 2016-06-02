import LCLS2 

shutter = LCLS2.Device("shutter")
shutter.add_component("motor",2)
shutter.add_component("gauge",2)

shutter2 = LCLS2.Device("shutter_2")
shutter2.add_component("motor",2)
shutter2.add_component("gauge",2)


print shutter == shutter2



collimator = LCLS2.Device("collimator")
collimator.add_component("motor",1)
collimator.add_component("gauge",3)


LCLS2.device_list["shutter"] = shutter
LCLS2.device_list["collimator"] = collimator


#device_list = "FISH HEAD"


sxr = LCLS2.Beamline()
sxr.add_device("shutter", 0.0)
sxr.add_device("collimator",1.0)
sxr.add_device("FISH",10.0)

print sxr

print shutter.count()
print shutter.count("gauge")
print shutter.count("FISH")

print sxr
print sxr.count_devices()
print sxr.count_components()



df = LCLS2.from_excel("Component List.xlsx")
print LCLS2.device_list.keys()
print LCLS2.beamline_list



