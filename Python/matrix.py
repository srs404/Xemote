from subprocess import call
from time import sleep
from sys import stdout
from os import system

# Clear Screen 
system('cls')

# Print Letter by Letter Like Matrix/Typerwriter
def delay_print(s, speed=0.25):
    for c in s:
        stdout.write(c)
        stdout.flush()
        sleep(speed)

# Flashing Lights [Green, Red]
def flashing_lights(how_mane_times=5, delays=0.5):
    for i in range(0, how_mane_times):
        call(["cmd.exe", "/c", "color 0a"]) # green
        sleep(delays)
        call(["cmd.exe", "/c", "color 0c"]) # red
        sleep(delays)

def main():
    # Print Matrix
    delay_print("\n\n\n                                                                           ", 0.001)
    delay_print("           _~_ _~_\n", 0.001)
    delay_print("           ==============================================", 0.001)
    delay_print("                            ", 0.001)
    delay_print("___   ___\n ", 0.001)
    delay_print("                                                                                    ", 0.001)
    delay_print("\  \ /  / \n ", 0.001)
    delay_print("                             ", 0.001)
    delay_print("Greetings!", 0.05)
    delay_print("                                             ", 0.001)
    delay_print(" \  V  /  \n ", 0.001)
    delay_print("              !! Do Not Even Think Of Shutting Down !!", 0.02)
    delay_print("                              ", 0.001)
    delay_print("  >   <   \n ", 0.001)
    delay_print("                                                                                    ", 0.001)
    delay_print(" /  .  \  \n", 0.001)
    delay_print("           ==============================================", 0.001)
    delay_print("                            ", 0.001)
    delay_print("/__/ \__\ \n\n", 0.001)

    # Flashing Lights
    flashing_lights(4)

    # Print Matrix
    delay_print("<>====================================================================================================<>\n|\t\t\t\t\t\t\t\t\t\t\t\t       |\n", 0.001)
    delay_print("|           You don't need to be scared, but this is not something to be taken lightly.\t\t       |\n", 0.04)
    delay_print("|           You are in my Game Now. I have your photo of tampering with my device.\t\t       |\n", 0.04)
    delay_print("|           Simply leave my device as is or there will be consequences.\t\t\t\t       |\n|\t\t\t\t\t\t\t\t\t\t\t\t       |\n", 0.04)
    delay_print("|           I WILL BE WATCHING YOU...", 0.1)
    delay_print("\t\t\t\t\t\t\t\t       |\n|\t\t\t\t\t\t\t\t\t\t\t\t       |\n", 0.001)
    delay_print("<>====================================================================================================<>\n", 0.001)


main()
# Infinite Loop
while True:
    sleep(5)
    flashing_lights(1, 3)