from model.village import *
from model.event import *
from model.scene import *
from driver.nfcreader import *

includeIO = True

if includeIO:
    cards = NFC()

app = TroubleVillage()

app.mainloop()

