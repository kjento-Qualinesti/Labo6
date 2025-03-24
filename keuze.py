from transform import transformToJson,transformBack
from Servers import toevoegen,verwijderen,checkServer,bekijkList,checkAllServers


inputList = [] 
outputList = []
serverList = []
inputList += transformBack("input.json")
outputList += transformBack("output.json")
serverList += transformBack("servers.json")


def keuze(nummer):
    match nummer:
        case 1:
            inputList.append(nummer)
            server = toevoegen()
            inputList.append(server)
            serverList.append(server)
        case 2:
            inputList.append(nummer)
            server = verwijderen()
            if server == "":
                inputList.append(server)
            else:
                inputList.append(server)
                serverList.remove(server)
        case 3:
            inputList.append(nummer)
            bekijkList()
        case 4:
            inputList.append(nummer)
            List = checkServer()
            inputList.append(List[0])
            outputList.append(List[1])
        case 0:
            inputList.append(nummer)
            print("Tot de volgende keer")
            transformToJson(inputList, "input.json")
            transformToJson(outputList, "output.json")
            transformToJson(serverList,"servers.json")
            checkAllServers()
            quit()
        case _:
            inputList.append(nummer)
            print(f"{nummer} is geen optie. Probeer opniew.")