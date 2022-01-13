class Universe:
    def __init__(self,delta_v,gravity_mu):
        # change in velocity
        self.delta_v = delta_v
        # the standard gravitational parameter μ of a celestial body is the product of the gravitational constant G and the mass M of the body.
        self.gravity_mu = gravity_mu

    print("Always executed")
    
    if __name__ == "__main__":
        def StandardModel(self):
            Lsm = (-0.5 * self.delta_v * self.gravity_mu)
            return Lsm
    else:
        def Relativity():
            pass

universe = Universe(1,2)
print(universe.StandardModel())