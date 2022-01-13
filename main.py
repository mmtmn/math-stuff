class Universe:
    def __init__(self,delta_v,muon_a):
        # change in velocity
        self.delta_v = delta_v
        # the standard gravitational parameter μ of a celestial body is the product of the gravitational constant G and the mass M of the body.
        # g-factor −2.002 331 83620(86)
        self.muon_a = muon_a

    print("Always executed")
    
    if __name__ == "__main__":
        def StandardModel(self):
            Lsm = (-0.5 * self.delta_v * self.muon_a)
            return Lsm
    else:
        def Relativity():
            pass

universe = Universe(1,2)
print(universe.StandardModel())