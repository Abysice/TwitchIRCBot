#Test Twitch Bot 21/02/2014 - Adam Bysice
import socket
import string
import win32com, win32api, win32con
import time
from time import gmtime, strftime

timeout = 10

def stuff():

    then = time.time()
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

    ##loop letting the bot run.
    while (done == False):
            ##Receiving data from IRC and spitting it into manageable lines.
            readbuffer=readbuffer+ s.recv(1024)
            temp=string.split(readbuffer, "\n")
            readbuffer=temp.pop( ) #clears readbuffer
            for i in range(0,len(temp)):
                #print temp[0]# find each line
                subline = temp[i].split(':') #split each line by ":"
                nameline = temp[0].split('!') #split by ! for name
                
                #print len(subline)

                if (len(subline) == 3): # we only carry about the words sent
                    #print subline[2] # The message sent
                        COMMAND = subline[2]
                        
                        #z = 0x5A  = up
                        if (COMMAND[0:2].find("up") != -1):
                            print nameline[0] + " : " + COMMAND
                            print "Pressed: up"
                            win32api.keybd_event(0x5A, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x5A,0 ,win32con.KEYEVENTF_KEYUP ,0)

                        #c = 0x43 = down
                        if (COMMAND[0:4].find("down") != -1):
                            print nameline[0] + " : " + COMMAND
                            print "Pressed: down"
                            win32api.keybd_event(0x43, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x43,0 ,win32con.KEYEVENTF_KEYUP ,0)

                        #x = 0x58 = left
                        if (COMMAND[0:4].find("left") != -1):
                            print nameline[0] + " : " + COMMAND
                            print "Pressed: left"
                            win32api.keybd_event(0x58, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x58,0 ,win32con.KEYEVENTF_KEYUP ,0)

                        #v = 0x56 = right
                        if (COMMAND[0:5].find("right") != -1):
                            print nameline[0] + " : " + COMMAND
                            print "Pressed: right"
                            win32api.keybd_event(0x56, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x56,0 ,win32con.KEYEVENTF_KEYUP ,0)

                        #w = 0x57 = a
                        if (COMMAND[0:1].find("a") != -1):
                            print nameline[0] + " : " + COMMAND
                            print "Pressed: a"
                            win32api.keybd_event(0x57, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x57,0 ,win32con.KEYEVENTF_KEYUP ,0)

                        #q = 0x51 = b
                        if (COMMAND[0:1].find("b") != -1):
                            print nameline[0] + " : " + COMMAND
                            print "Pressed: B"
                            win32api.keybd_event(0x51, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x51,0 ,win32con.KEYEVENTF_KEYUP ,0)

                        #e = 0x45 = y
                        if (COMMAND[0:1].find("y") != -1):
                            print nameline[0] + " : " + COMMAND
                            print "Pressed: y"
                            win32api.keybd_event(0x45, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x45,0 ,win32con.KEYEVENTF_KEYUP ,0)

                        #r = 0x58 = x
                        if (COMMAND[0:1].find("x") != -1):
                            print nameline[0] + " : " + COMMAND
                            print "Pressed: x"
                            win32api.keybd_event(0x58, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x58,0 ,win32con.KEYEVENTF_KEYUP ,0)



                        #a = 0x41 = start
                        if (COMMAND[0:5].find("start") != -1):
                            print nameline[0] + " : " + COMMAND
                            print "Pressed: start"
                            win32api.keybd_event(0x41, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x41,0 ,win32con.KEYEVENTF_KEYUP ,0)

                        #s = 0x53 = select
                        if (COMMAND[0:6].find("select") != -1):
                            print nameline[0] + " : " + COMMAND
                            print "Pressed: select"
                            win32api.keybd_event(0x53, 0,0,0)
                            time.sleep(.1)
                            win32api.keybd_event(0x53,0 ,win32con.KEYEVENTF_KEYUP ,0)

                                      
                        if (COMMAND[0:5].find("!help") != -1):# 0:9 because of newline ect
                            #send reply to channel
                            reply = "PRIVMSG "+CHANNEL+" : Commands: up down left right a b x y start select"+ "\r\n"
                            print reply
                            #send reply to socket
                            s.send(reply)

                        now = time.time()
                        if ((now-then) > 60):
                            done = True

                        elif(subline[0]=="PING"):
                            s.send("PONG %s\r\n" % line[1])
                            print "PINGED"
    
                
while(1):
    stuff()#restarts every 60 seconds

#keylist
##0x30 - 0 key
##0x31 - 1 key
##0x32 - 2 key
##0x33 - 3 key
##0x34 - 4 key
##0x35 - 5 key
##0x36 - 6 key
##0x37 - 7 key
##0x38 - 8 key
##0x39 - 9 key
##0x41 - A key
##0x42 - B key
##0x43 - C key
##0x44 - D key
##0x45 - E key
##0x46 - F key
##0x47 - G key
##0x48 - H key 
##0x49 - I key
##0x4A - J key
##0x4B - K key
##0x4C - L key
##0x4D - M key
##0x4E - N key
##0x4F - O key
##0x50 - P key
##0x51 - Q key
##0x52 - R key
##0x53 - S key
##0x54 - T key
##0x55 - U key
##0x56 - V key
##0x57 - W key
##0x58 - X key
##0x59 - Y key
##0x5A - Z key
                 
