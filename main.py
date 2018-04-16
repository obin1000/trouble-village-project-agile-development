from model.village import *
from model.event import *
from model.scene import *
from driver.nfcreader import *

import threading

includeIO = True

if includeIO:
    nfcThread = NFC("nfcThread")
    nfcThread.start()

app = TroubleVillage()

app.mainloop()

