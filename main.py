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
            """ a gauge quantum field theory containing
             the internal symmetries of the unitary 
             product group SU(3) × SU(2) × U(1). 
             The theory is commonly viewed as describing 
             the fundamental set of particles – the leptons,
             quarks, gauge bosons and the Higgs boson. 
            """
            Lsm = (-0.5 * self.delta_v * self.muon_a)
            return Lsm
    else:
        def Relativity():
            pass

universe = Universe(1,2)
print(universe.StandardModel())