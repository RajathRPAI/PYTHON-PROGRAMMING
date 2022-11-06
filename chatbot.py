#designing a simple chat bot using if else
print("hello, i am a chatbot")
print("how may i help you ? \n")
print("hit 1 for software installation request")
print("hit 2 for software update request")
print("hit 3 for software uninstall request")
print("hit 4 for software repair request")
print("hit 5 for other request")

#accepting the user inputs
userinput=int(input("enter the choice:"))


#using if else to process the user input
if userinput==1:
    softwareneeded=input("please provide the software name")
elif userinput == 2:
    softwareupdate = input("please provide the software name to be updated")
elif userinput==3:
    softwareuninstall= input("pls provide software name to be uninstalled")
elif userinput ==4:
    softwarerepair=input("pls provide soft name to be repaired")
else:
    otherrequest=input("please provide the details of our request")

print ("thank you for using ,our team will help you soon")

a=int(input("enter the 1st no:"))
b=int(input("enter the 2nd no"))
c=a+b
print("addition of two no=",c)

