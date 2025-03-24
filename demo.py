""" import platform
import subprocess


def myping(host):
    # Choose parameter based on OS
    parameter = "-n" if platform.system().lower() == "windows" else "-c"

    # Constructing the ping command
    command = ["ping", parameter, "1", host]
    response = subprocess.call(command)

    # Interpreting the response
    return response == 0


# Testing the function
print(myping("127.0.0.1")) """

serverList = ["127.0.0.1", "www.google.com", "127.0.0.1"]
serverName = "127.0.0.1"

for server in serverList:
            if(server == serverName):
                serverList.remove(serverName)
                print(f"server {serverName} is verwijderd.")
                break
            else:
                print(f"server niet gevonden. Weet u zeker dat {serverName} er instaat?")
print(serverList)
