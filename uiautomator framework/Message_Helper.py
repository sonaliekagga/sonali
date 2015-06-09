import os
import sys

#from uiautomator import Device
from uiautomator import device as device
   
class TextMessage:

  def SendSMSFromContacts(self,name,message):
#    device = Device('4a25b8a')
    device.screen.on()
    device.press.home()

#device log info("move to contacts")
    device(scrollable=True).scroll.horiz.forward()
    device(scrollable=True).scroll.vert.backward()
    device(text="Contacts").click()

#device log info("select contact")
    device(scrollable=True).scroll.to(text=name)
    device(text = name).click()

#device log info("create message")
    device(className="android.widget.ImageView",resourceId="com.android.contacts:id/icon_alternate").click()

#device log info("input message")
    #device.input ("Test message")
    device(text="Type message").set_text(message)
    mb=raw_input

#device log info("send message")
    #device(className="android.widget.ImageView",resourceId="com.android.mms:id/send_button_sms").click()
    device.click(544,1176)
    device.press.home()





  def SendContactsviaSMS(self,numsend,sendnum):

    device.screen.on()
    device.press.home()

#device log info("move to contacts")
    device(text="Contacts").click()
    device(text = "All contacts").click()
    #device(scrollable=True).scroll.to(text=name)

#device log info("number to send")
    device(scrollable=True).scroll.to(text=numsend)
    device(text = numsend).click()
    device.press.menu()
    device(text="Send contact via SMS").click()
    device.click(640,242)

#device log info("send message")
    #device(text="To").set_text(str3)
    #mb=raw_input
    device(scrollable=True).scroll.to(text=sendnum)
    device(text = sendnum).click()
    device.click(552,58)
    device.press.menu()
    device(text="Send").click()
    device.press.back()
    device.press.back()
    device.press.home()





  def deleteAllSMS(self):
    device.screen.on()
    device.press.home()

#device log info ("select message field ")
    device(text ="Messaging").click()
    device.press.menu()

#device log info ("select all the message for delete")
    device(text = "Delete all threads").click()

#device log info ("Delete all the messages")
#(In the place of "Cancel" use "Delete")
    device(text ="Cancel").click()
    device.press.home() 






  def deleteSMS(self,name):
    device.screen.on()
    device.press.home()

#device log info ("select message field")
    device(text ="Messaging").click()

#device log info ("select message for delete")
    device(scrollable=True).scroll.to(text=name)
    device(text=name).long_click()
    device.click(552,58)
    #device.orientation="l"

#device log info ("Delete the message")
#(In the place of "Cancel" use "Delete")
    device(text="Cancel").click()
    device.press.home()





 
  def SMSfromMessaging(self,number,message):
    device.screen.on()
    device.press.home()

#device log info ("select message field")
    device(text ="Messaging").click()
    device(className="android.widget.ImageButton",index="0").click()
    device.click(576,1136)

#device log info ("select the number")
    device(text="To").set_text(number)
    nb=raw_input

#device log info ("write the message")
    device(text="Type message").set_text(message)
    mb=raw_input
    device.click(544,595)
    device.press.home()







#If any call came & it missed then send message to that number through notification.
  def SMSviaNotification(self,message):

#device log info ("open notification")
    device.open.notification() 

#device log info ("select number to send message")
    device(text="Missed call").swipe.down()
    device(text="Message").click()

#device log info ("Type Message")
    device(text="Type message").set_text(message)
    mb=raw_input

#device log info ("send message")
    device.click(544,1176)
    device.press.home()








  def sendSMSinGroup(self,numsend,sendnum,sendnum1,sendnum2):
    device.screen.on()
    device.press.home()

#device log info("move to contacts")
    device(text="Contacts").click()
    device(text = "All contacts").click()
    #device(scrollable=True).scroll.to(text=name)

#device log info("number to send")
    device(text = numsend).click()
    device.press.menu()
    device(text="Send contact via SMS").click()
    device.click(640,242)

#device log info("send message")
    #device(text="To").set_text(str3)
    #mb=raw_input
    device(scrollable=True).scroll.to(text=sendnum)
    device(text = sendnum).click()
    device(text = sendnum1).click()
    device(text = sendnum2).click()
   
    device.click(552,58)
    device.press.menu()
    device(text="Send").click()
    device.press.back()
    device.press.home()






  def makeCall(self,name):

#device log info ("select phone field")
    device(text="Phone").click()

#device log info ("Type number")
    #device(text="Type a name or phone number").set_text(number)
    #mb=raw_input
    #device.click(32,226)

#device log info ("select contact number")
    device(text="Contacts").click()
    device(scrollable=True).scroll.to(text=name)
    device(text=name).click()

#device log info ("Dial number")
    device(text=name).down(className="android.widget.RelativeLayout").click()





  
  def Screencast(self):
    device.screen.on()
    device.press.home()

#device log info("select screencast")
    device(text = "Screencast").click()
    device(text = "Start Screencast").click()
    device.open.notification()
    device(text="Recording?").swipe.down()
    device(text = "Stop").click()
    device.press.home()




  def wifi(self):
    device.screen.on()
    device.press.menu()
    device(text ="Settings").click()
    device(text ="Wireless & networks").down(className="android.widget.TextView").click()
    device.screenshot("home.png")
    device.swipe(591,191,688,245)
    device.press.home()

 
  def takephoto(self):
    device.screen.on()
    device(text ="Camera").click()
    device(className="android.widget.ImageView",index="3").click()
    

