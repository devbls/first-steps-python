def move_disc(origin, destiny):
    disc = origin.pop()
    destiny.append(disc)

def print_towers(towerA, towerB, towerC):
    print("A:", towerA)
    print("B:", towerB)
    print("C:", towerC)
    print()

def hanoi_towers(disc_quantity, origin, destiny, aux):
    if disc_quantity == 1:
        move_disc(origin, destiny)
        print_towers(towerA, towerB, towerC)
    else:
        hanoi_towers(disc_quantity - 1, origin, aux, destiny)
        move_disc(origin, destiny)
        print_towers(towerA, towerB, towerC)
        hanoi_towers(disc_quantity - 1, aux, destiny, origin)

disc_quantity = 3
towerA = list(range(disc_quantity, 0, -1))
towerB = []
towerC = []

print_towers(towerA, towerB, towerC)
hanoi_towers(disc_quantity, towerA, towerC, towerB)