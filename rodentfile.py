from rodents import Rodent

rodents = {}

for line in open('rodents.csv'):
    tag_id, weight = line.split(',')
    if tag_id not in rodents:
        rodents[tag_id] = Rodent(tag_id)
        rodents[tag_id].add_weight(weight)
    else:
        rodents[tag_id].add_weight(weight)
print rodents
for key in rodents:
    print rodents[key].tag_id, rodents[key].weights
