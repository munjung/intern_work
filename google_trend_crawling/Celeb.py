class Celeb():
    def __init__(self, celebCode, startDate, endDate, searchCountry, celebName):
        self.celebName = celebName
        self.celebCode = celebCode
        self.startDate = startDate
        self.endDate = endDate
        self.searchCountry = searchCountry

    def totalPeriod(self):
        self.searchPeriod = self.startDate+' '+self.endDate
        return self.searchPeriod

    def convertAlpha(self):
        if(self.searchCountry.islower()):
            self.searchCountry = self.searchCountry.swapcase()

        return self.searchCountry
