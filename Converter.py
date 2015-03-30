# -*- coding: cp1252 -*-



import sys,os
from PIL import Image

#minimal char table
chars = ['@', '%', '#', '*', '+', '=', '-', ':', '.', ' ' ]

#chars=["$","@","B","%","8","&","W","M","#","*","o","a","h","k","b","d","p","q","w","m","Z","O","0","Q","L","C","J","U","Y","X","z","c","v","u","n","x","r","j","f","t","/","\\","|","(",")","1","{","}","[","]","?","-","_","+","~","<",">","i","!","l","I",";",":",",","^","`","'","."," "]
'''
ASCII SHADE TABLE CORTESY OF:
http://paulbourke.net/dataformats/asciiart/
'''
print '''  _____ __  __    _____   _                    _____  _____ _____ _____ 
 |_   _|  \/  |/ ____|   | |            /\    / ____|/ ____|_   _|_   _|
   | | | \  / | |  __    | |_ ___      /  \  | (___ | |      | |   | |  
   | | | |\/| | | |_ |   | __/ _ \    / /\ \  \___ \| |      | |   | |  
  _| |_| |  | | |__| |   | || (_) |  / ____ \ ____) | |____ _| |_ _| |_ 
 |_____|_|  |_|\_____|    \__\___/  /_/    \_\_____/ \_____|_____|_____|
   _____                          _            
  / ____|                        | |           
 | |     ___  _ ____   _____ _ __| |_ ___ _ __ 
 | |    / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
 | |___| (_) | | | \ V /  __/ |  | ||  __/ |   
  \_____\___/|_| |_|\_/ \___|_|   \__\___|_|
                                                        by: Lucas Sabiao

                                                        
 '''
arquivo = sys.argv[-1]
if len(sys.argv) < 2:
    arquivo = raw_input("Input the file: ")
try:
    print "Searching for the file: "+arquivo,
    original = Image.open(arquivo)
except IOError:
    print "File not found!"
    sys.exit()
print "[Found]"
print "Preparing .txt file",
output = file(arquivo[:-4]+".txt","w")
print "[Done]"
loaded = original.load()
print "Converting file... Please wait",
for a in range(0,original.size[1]):
    for b in range(0,original.size[0]): 
        buf = loaded[b,a]
        greyScale = int(buf[0]*0.299+buf[1]*0.587+buf[2]*0.114)
        saturation = int((greyScale / 255.0)*(len(chars)-1))
        output.write(chars[saturation])
    output.write("\n")
print "[Done]"
print "Flushing .txt",
output.close()
print "[Done]"
print "\n\n"
print "Flushed at "+os.getcwd()+os.sep+arquivo[:-4]+".txt"
        

