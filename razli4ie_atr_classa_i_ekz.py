class Building:
    total = 0

    def __init__(self):
        Building.total += 1


obj = []
obj_size = 40
while len(obj) < obj_size:
    new_obj = Building()
    obj.append(new_obj)

print(Building.total)
