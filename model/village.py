# Abstracte weergaven van een dorp
class Village:
    # Constructor voor Village
    def __init__(self, name, population, wood, water, players):
        self.name = name
        self.population = population
        self.wood = wood
        self.water = water
        self.players = players
        self.turn = 1
        self.state = 0
        self.points = 0
        self.well = False
        self.stockpile = False
        self.hospital = False
        self.ship1 = False
        self.ship2 = False
        self.ship3 = False
        self.ship4 = False
        self.setPoints()

    def getPopulation(self):
        return self.population

    # 0 = default; 1 = burning; 2 = flood;
    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def getPoints(self):
        return self.points

    def setPoints(self):

        if (self.population > 80 and (self.population < 10000)):
            self.points = 5
        elif (self.population > 60 and (self.population < 79)):
            self.points = 4
        elif (self.population > 40 and (self.population < 59)):
            self.points = 3
        elif (self.population > 1 and (self.population < 39)):
            self.points = 2
        elif (self.population == 0):
            self.points = 0

    def buildWell(self):
        if self.wood - 500 >= 0:
            self.wood -= 500
            self.well = True

        else:
            return False

    def buildStockpile(self):
        if self.water - 500 >= 0:
            self.water -= 500
            self.stockpile = True
            return True
        else:
            return False

    def buildHospital(self):
        if self.wood - 2000 >= 0:
            self.water -= 2000
            self.stockpile = True
            return True
        else:
            return False

    def buildShip1(self):
        if self.wood - 2500 >= 0:
            self.wood -= 2500
            self.ship1 = True
            return True
        else:
            return False

    def buildShip2(self):
        if self.wood - 1500 >= 0:
            self.wood -= 1500
            self.ship2 = True
            return True
        else:
            return False

    def buildShip3(self):
        if self.wood - 1500 >= 0:
            self.wood -= 1500
            self.ship3 = True
            return True
        else:
            return False

    def buildShip4(self):
        if self.wood - 500 >= 0:
            self.wood -= 500
            self.ship4 = True
            return True
        else:
            return False

    def getStateImg(self):
        villageImg = ""
        if self.state == 0:
            villageImg = ""
        elif self.state == 1:
            villageImg = "img/flame.png"
        elif self.state == 2:
            villageImg = "img/wave.png"
        elif self.state == 3:
            villageImg = "img/fire.png"
        return villageImg

    def addPopulation(self, population):
        self.population += population

    def lowerPopulation(self, population):
        self.population -= population
        if self.population < 0:
            print("Game over!")
            self.population = 0

    def getName(self):
        return self.name

    def addWood(self, wood):
        if self.stockpile:
            wood *= 1.5

        self.wood += wood

        if self.wood < 0:
            self.wood = 0

    def setWood(self, wood):
        self.wood = wood
        if self.wood < 0:
            self.wood = 0

    def getWood(self):
        return int(self.wood)

    def addWater(self, water):
        if self.well:
            water *= 1.5

        self.water += water

        if self.water < 0:
            self.water = 0

    def setWater(self, water):
        self.water = water
        if self.water < 0:
            self.water = 0

    def getWater(self):
        return int(self.water)

    # for next turn use the one in scene
    def nextTurn(self):
        if self.population > 0:
            self.turn += 1
            return self.turn

    def getTurn(self):
        return self.turn
