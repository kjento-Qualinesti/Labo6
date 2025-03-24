import json

input = []
output = []

def transformToJson(list,bestandsnaam):
    input.append(list)
    with open(bestandsnaam, "w") as overschrijven:
        json.dump(list,overschrijven)

def transformBack(bestandnaam):
    try:
        with open(bestandnaam, "r") as overschrijven:
            history = json.load(overschrijven)
            if len(history) > 0:
                return history
            else:
                return []
    except:
        return []