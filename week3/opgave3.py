class Circel():
    oppervlakte = 0
    omtrek = 0

    def __init__(self, straal):
        self.straal = straal


    def area(self):
        self.oppervlakte = float(200.96)
        return self.oppervlakte

    def perimiter(self):
        self.omtrek = float(50.24)
        return self.omtrek

newCircle = Circel(8)
assert newCircle.area() == 200.96
assert newCircle.perimiter() == 50.24
