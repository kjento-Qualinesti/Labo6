import platform
import subprocess
from transform import transformBack,transformToJson


serverList = []
def loadServerList():
    serverList.extend(transformBack("servers.json"))

def toevoegen():
    print("-----------TOEVOEGEN SERVER-----------")
    serverName = input("Naam server: ")
    serverList.append(serverName)
    print("Server is succesvol toegevoegd.")

    print("-----------TOEVOEGEN SERVER-----------")
    print()
    return serverName

def verwijderen():
    print("-----------VERWIJDEREN SERVER-----------")
    
    if len(serverList) == 0:
        print("U moet eerst servers toevoegen voordat u er een kunt verwijderen.")
        print("-----------VERWIJDEREN SERVER-----------\n")
        return ""

    serverName = input("Naam server: ")

    if serverName in serverList:
        serverList.remove(serverName)
        print(f"Server {serverName} is verwijderd.")
    else:
        print(f"Server niet gevonden. Weet u zeker dat {serverName} in de lijst staat?")
    
    print("-----------VERWIJDEREN SERVER-----------\n")
    return serverName

def checkServer():
    print("------------CHECKING SERVER------------")
    serverName = input("Naam server: ")
    # Choose parameter based on OS
    parameter = "-n" if platform.system().lower() == "windows" else "-c"

    # Constructing the ping command
    command = ["ping", parameter, "1", serverName]
    response = subprocess.call(command)

    # Interpreting the response
    if response == 0:
        print(f"Server {serverName} is online")
        output = f"{serverName} = online"
    else:
        print(f"Server {serverName} is offline")
        output = f"{serverName} = offline"

    print("------------CHECKING SERVER------------")
    print()
    return [serverName, output ]
    


""" # Testing the function
print(myping("127.0.0.1")) """

def bekijkList():
    print("------------SERVERList------------")
    for el in serverList:
        print(f"- {el}")
    print("------------SERVERList------------")
    print()
    

serversCheck = []
def checkAllServers():
    print("------------CHECKING SERVER------------")
    for server in serverList:
    # Choose parameter based on OS
        parameter = "-n" if platform.system().lower() == "windows" else "-c"

        # Constructing the ping command
        command = ["ping", parameter, "1", server]
        response = subprocess.call(command)

        # Interpreting the response
        if response == 0:
            print()
            print(f"Server {server} is online")
            print()
            output = f"{server} = online"
        else:
            print()
            print(f"Server {server} is offline")
            print()
            output = f"{server} = offline"
        serversCheck.append(output)
    transformToJson(serversCheck, "AllServers.json")
    print("------------CHECKING SERVER------------")
    print()
        


    

