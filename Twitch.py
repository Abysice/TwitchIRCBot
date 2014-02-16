#Test Twitch Bot 15/02/2014 - Adam Bysice
import socket
import string
import win32com, win32api, win32con

import time
from time import gmtime, strftime

while (1):

    strftime("%Y-%m-%d %H:%M:%S", gmtime())
    inputs = 0
    done = False
     
    #Config
    HOST="199.9.253.199" #Twitch IRC ip, don't change it.
    PORT=6667 ##Same with this port
    NICK="twitchplaysanything" ##bots username.
    PASS="" ##use this http://twitchapps.com/tmi/ instead of PW
    IDENT="twitchplaysanything" ##Bot username again
    REALNAME="Kirbys Bot" ##This doesn't really matter.
    CHANNEL="#hyperbolicbubble" ##This is the channel
     
    s = socket.socket( ) ##Creating the socket variable
    s.connect((HOST, PORT)) ##Connecting to Twitch
    s.send("PASS %s\r\n" % PASS) ##Notice how I'm sending the password BEFORE the username!
    ##Just sending the rest of the data now.
    s.send("NICK %s\r\n" % NICK)
    s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
    ##Connecting to the channel.
    s.send("JOIN %s\r\n" % CHANNEL)

    readbuffer = ""

    ##Eternal loop letting the bot run.
    while (done == False):
            ##Receiving data from IRC and spitting it into manageable lines.
            readbuffer=readbuffer+ s.recv(1024)
            temp=string.split(readbuffer, "\n")
            readbuffer=temp.pop( ) #clears readbuffer
            for i in range(0,len(temp)):
                #print temp[i]# find each line
                subline = temp[i].split(':') #split each line by ":"
                #print len(subline)

                if (len(subline) == 3): # we only carry about the words sent
                    #print subline[2] # The message sent
                    #if(subline[2][0:1] == "!"):
                        COMMAND = subline[2]
                        print COMMAND
                        #zero = 0x30 = up
                        if (COMMAND[0:2].find("up") != -1):
                            print "Pressed: up"
                            inputs +=1
                            win32api.keybd_event(0x30, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x30,0 ,win32con.KEYEVENTF_KEYUP ,0)

                        #one = 0x31 = down
                        if (COMMAND[0:4].find("down") != -1):
                            print "Pressed: Down"
                            inputs +=1
                            win32api.keybd_event(0x31, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x31,0 ,win32con.KEYEVENTF_KEYUP ,0)

                        #two = 0x32 = left
                        if (COMMAND[0:4].find("left") != -1):
                            print "Pressed: Left"
                            inputs +=1
                            win32api.keybd_event(0x32, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x32,0 ,win32con.KEYEVENTF_KEYUP ,0)

                        #three = 0x33 = right
                        if (COMMAND[0:5].find("right") != -1):
                            print "Pressed: Right"
                            inputs +=1
                            win32api.keybd_event(0x33, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x33,0 ,win32con.KEYEVENTF_KEYUP ,0)

                        #four = 0x34 = a
                        if (COMMAND[0:1].find("a") != -1):
                            print "Pressed: A"
                            inputs +=1
                            win32api.keybd_event(0x34, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x34,0 ,win32con.KEYEVENTF_KEYUP ,0)

                        #five= 0x35 = b
                        if (COMMAND[0:1].find("b") != -1):
                            print "Pressed: B"
                            inputs +=1
                            win32api.keybd_event(0x35, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x35,0 ,win32con.KEYEVENTF_KEYUP ,0)

                        #six = 0x36 = start
                        if (COMMAND[0:5].find("start") != -1):
                            print "Pressed: Start"
                            inputs +=1
                            win32api.keybd_event(0x36, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x36,0 ,win32con.KEYEVENTF_KEYUP ,0)

                        #seven = 0x37 = select
                        if (COMMAND[0:6].find("select") != -1):
                            print "Pressed: select"
                            inputs +=1
                            win32api.keybd_event(0x37, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x37,0 ,win32con.KEYEVENTF_KEYUP ,0)

                                      
                        if (COMMAND[0:5].find("!help") != -1):# 0:9 because of newline ect
                            #send reply to channel
                            reply = "PRIVMSG "+CHANNEL+" : Commands: up down left right a b start select"+ "\r\n"
                            print reply
                            #send reply to socket
                            s.send(reply)

                        if (inputs >= 40):
                            done = True

                        
                        elif(subline[0]=="PING"):
                            s.send("PONG %s\r\n" % line[1])
                            print "PINGED"
    
                
     
                        
            
                
