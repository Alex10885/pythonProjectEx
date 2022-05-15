import random
from visuals.classes_models import Molecule


def generate_moleculs(n):
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

        for mol in mass_curpuscul:
            curpuscul = mass_curpuscul[:4]

            mol = Molecule(curpuscul[0], curpuscul[1], curpuscul[2], curpuscul[3])
            molecule.append(mol)
            del mass_curpuscul[:4]

    return molecule