from selenium import webdriver 
from selenium.webdriver.chrome.options import Options

import time
from selenium.webdriver.common.keys import Keys

import requests


class InstaBot:
    
    def __init__(self, user, passw):
        self.password = passw
        self.username = user
        self.uri = "https://instagram.com/"
        self.driver = webdriver.Chrome("./chromedriver.exe")
        self.islog = False

    def Connect(self):
        self.driver.get(self.uri)
        time.sleep(3)
        self.driver.find_element_by_name("username").click()
        self.driver.find_element_by_name("username").click()
        self.driver.find_element_by_name("username").send_keys(self.username)
        self.driver.find_element_by_name("username").click()
        self.driver.find_element_by_name("password").send_keys(self.password)
        time.sleep(2)
        element = self.driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']")
        self.driver.execute_script("arguments[0].removeAttribute('disabled');", element)
        self.driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy   y3zKF     ']").click()

    def checkLoggin(self):
        time.sleep(2)
        self.driver.get(self.uri);
        logClass = self.driver.find_elements_by_class_name("logged-in")
        if(len(logClass) > 0):
            self.islog = True
            return True
        else:
            self.islog = False
        return False

    def isLog(self):
        return self.islog


    def canContact(self, username):
        classButtonContact = "fAR91"
        btn = self.driver.find_elements_by_class_name(classButtonContact)
        if(len(btn) > 0):
            return True
        return False

    def sendMessageTo(self, username, message):

        if(self.isLog()):
            
            self.driver.get(self.uri + username + "/")
            time.sleep(2)
            print("[REDIRECT TO] "  + self.uri + username + "/")
            if(self.canContact(username)):
                print("[REQUEST TO] " + username + ", action to send direct message")
                self.driver.find_element_by_xpath("//button[@class='fAR91 sqdOP  L3NKy _4pI4F   _8A5w5    ']").click()

                time.sleep(5)
                self.driver.find_element_by_tag_name('textarea')
                self.driver.find_element_by_tag_name('textarea').send_keys(message)
                time.sleep(1)
                self.driver.find_element_by_tag_name('textarea').send_keys(Keys.RETURN)
                print("[MESSAGE TO] " + username + " bot have send : {" + message + "}")
                # _7UhW9   xLCgt      MMzan  KV-D4             p1tLr      hjZTB
                time.sleep(1)
                listMessages = self.driver.find_elements_by_class_name("_7UhW9")
                for mess in listMessages:
                    if("<span>" in mess.get_attribute('innerHTML') and "</span>" in mess.get_attribute('innerHTML')):
                        print(mess.get_attribute('innerHTML').replace('<span>', '').replace('</span>'))
    def sendText(self, message):
        self.driver.find_element_by_tag_name('textarea')
        self.driver.find_element_by_tag_name('textarea').send_keys(message)
        time.sleep(1)
        self.driver.find_element_by_tag_name('textarea').send_keys(Keys.RETURN)
        print("[MESSAGE BOT] bot have send : {" + message + "}")
        # _7UhW9   xLCgt      MMzan  KV-D4             p1tLr      hjZTB
        time.sleep(1)


    def initBotChat(self, username):
        
        self.driver.get(self.uri + username + "/")
        time.sleep(2)
        print("[SEND BOT CHAT FOR] " + username)

        if(self.canContact(username)):
            print("[REQUEST TO] " + username + ", BOT INITIALIZED")
            self.driver.find_element_by_xpath("//button[@class='fAR91 sqdOP  L3NKy _4pI4F   _8A5w5    ']").click()
            time.sleep(2)

            self.chatUri = self.driver.current_url

    def launchBotChat(self, username):
        try:
            LIST = []
            listMessages = self.driver.find_elements_by_class_name("_7UhW9")
            for mess in listMessages:
                if("<span>" in mess.get_attribute('innerHTML') and "</span>" in mess.get_attribute('innerHTML')):
                    LIST.append(mess.get_attribute('innerHTML')) 

            last_str = str(LIST[len(LIST) - 1]).replace('<span>', '').replace('</span>', '')

            if(last_str[0] == '!'):
                if(last_str.replace('!', '') == "help"):
                    self.sendText("""
                    --------------- INSTABOT ----------------
                    -------------version v1.0.0--------------

                    You have execute Help commands:
                    - !help -> get help
                    """)

                    #Add code here for more function bot chat :)
        except:
            pass
    def alreadyFollowed(self, username):
        isFollow = self.driver.find_elements_by_class_name("_5f5mN")
        if(len(isFollow) > 0):
            return True
        return False;   
    def getProfil(self, username):
        self.driver.get(self.uri + username + "/")
        time.sleep(2)
        infos = self.driver.find_elements_by_class_name("g47SY")
        name = self.driver.find_elements_by_class_name("rhpdm")

        print("[SEARCH FROM {" + username + "}] Followers : " + str(infos[1].get_attribute('innerHTML')))
        print("[SEARCH FROM {" + username + "}] Following : " + str(infos[2].get_attribute('innerHTML')))
        print("[SEARCH FROM {" + username + "}] Posts : " + str(infos[0].get_attribute('innerHTML')))
        print("[SEARCH FROM {" + username + "}] Name : " + str(name[0].get_attribute('innerHTML')))
        if(self.alreadyFollowed(username)):
            print("[SEARCH FROM {" + username + "}] This users is followed by you !")


    def followProfil(self, username):
        self.driver.get(self.uri + username + "/")
        time.sleep(2)






        



bot = InstaBot("aq.twins", "Anonymes12");
bot.Connect();
bot.checkLoggin();

if(bot.isLog()):
    bot.getProfil("alexunivex")


def command():
    cmd = str(input("InstaBot>> "))
    command()






