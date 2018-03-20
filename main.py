from model.village import *

dorp = Village("Dorp 1", 100, 100, 50)

print("Naam:", dorp.getName())
print("Aantal inwoonders:", dorp.getPopulation())
print("Aantal water:", dorp.getWater())
print("Aantal hout:", dorp.getWood())

from model.scene import *

app = TroubleVillage()
app.mainloop()