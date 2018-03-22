from model.village import *

dorp = Village("Dorp 1", 100, 100, 50)

print("Naam:", dorp.getName())
print("Aantal inwoners:", dorp.getPopulation())
print("Aantal water:", dorp.getWater())
print("Aantal hout:", dorp.getWood())

from model.event import *

villageEvent = VillageEvent("", "...")

print("Effect op het dorp:", villageEvent.getEffect())

from model.scene import *

app = TroubleVillage()
app.mainloop()

