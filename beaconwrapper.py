path = "/Users/skickar/ssids.txt"; ssids = open(path,'r'); command = "beacon "
for line in ssids:
    command = command +  "\"{}\",".format(line.strip())
print(command+" -mon")