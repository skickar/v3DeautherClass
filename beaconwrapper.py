path = input("What is the list of SSID's the broadcast?\n>"); ssids = open(path,'r'); command = "beacon "
for line in ssids:
    command = command +  "\"{}\",".format(line.strip())
print(command+" -mon")
