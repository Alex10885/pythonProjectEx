import random


class Rectang(object):

    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed


class Molecule(object):

    def __init__(self, xc, yc, radius, speed):
        self.xc = xc
        self.yc = yc
        self.radius = radius
        self.speed = speed

    @classmethod
    def generate_moleculs(self, n):
        mass_curpuscul = []

        molecule = []
        for mol in range(n):
            X = random.randrange(10, 300, 10)
            mass_curpuscul.append(X)
            Y = random.randrange(10, 300, 10)
            mass_curpuscul.append(Y)
            R = random.randrange(5, 20)
            mass_curpuscul.append(R)
            V = random.randrange(1, 6)
            mass_curpuscul.append(V)

            for _ in mass_curpuscul:
                curpuscul = mass_curpuscul[:4]
                mol = Molecule(curpuscul[0], curpuscul[1], curpuscul[2], curpuscul[3])
                molecule.append(mol)
                del mass_curpuscul[:4]

        return molecule
