import os

shutdown = input("Do you want to shut down the PC? (yes / no):")


if shutdown == "no":
    exit()
elif shutdown == "yes":
    os.system("shutdown /s /t 5")
else:
    os.system("shutdown -t 5 -r -f")