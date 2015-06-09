from Message_Helper import TextMessage

a=TextMessage()

#send sms from contact field .
#Give the name and message)
a.SendSMSFromContacts("Sonali","hello")

#send contact number via sms.
#Give the contact numbersend &give to whom sendnum)
a.SendContactsviaSMS("Sonali","Sonali")

#Delete all the messages(But here i have given cancel )
a.deleteAllSMS()

#Delete message one by one.
# give which message to delete.
a.deleteSMS("655020")

#send SMS from messaging.
#Give the number &type the Message.
a.SMSfromMessaging("8904707796","Hello")

#Send SMS via notification(if any missed call in notification it send the message to that number)
#Give the message.
a.SMSviaNotification("I am in meeting")

#send sms to group of number
#4 number to send sms

a.sendSMSinGroup("AAAAA","rihhi","Sonali","debabrat boruah")

#To make a call from contacts.
#Give a name/number to make a call
a.makeCall("AAAAA")

#for recording.
#video record running phone details.
a.Screencast()

# wifi on and off.
#If wifi is off then it on the wifi or viceversa.
a.wifi()


#Take photo from Camera.
a.takephoto()
