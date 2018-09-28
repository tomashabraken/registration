
#asking for firstname and lastname
firstname = input("What is firstname?")
print("Welcome " + firstname + " ,welcome to my program.") 

lastname = input("What is your lastname?")

#check if the lastname is the same as my lastname
mylastname = "Habraken"

if lastname.lower() == mylastname.lower() :
	print("You are a family member of me!") 

else:
	print("Welcome " + firstname + " " + lastname)

#ask for birthyear	
birthyear = input("What is your birthyear?")

#loop when user doesn't fill in numbers	
while birthyear.isdigit() == False:
	print("You have to fill in numbers!") 
	birthyear = input("What is your birthyear?")
	continue

#checking if users are older then 18	
if birthyear > "2000":
	print("You can not drink beer yet. So goodbye.")
	exit()

else:
	print("Great, you can drink a beer!")

#asking for gender
gender = input("What is your gender? (Male, female or other)")	

#control if the user fits in the perfect profile for the network
if len(lastname.lower()) > 8 or (birthyear < "1993" and birthyear > "1953") or gender.lower() == "male":
	print("You are the perfect match for our network!!")

elif len(lastname.lower()) < 8 or birthyear < "1953" or gender.lower() == "female":
	print("Sorry, you are not what we are looking for. Thank you for participate.")
	exit()

#asking for hobby
hobby = input("What is your 1st place hobby?")
print("That is a great hobby!")

#asking if they are excited to join the network with multiple choice
registration = input("Are you excited to join the network? A) Yes of course B) Mwaa, I don't know C) No, my father forced me [A/B/C]? : ").lower()	
	
while registration != "a" and registration != "b" and registration != "c":
	print("Fill in A, B or C please.")	
	registration = input("Are you excited to join the network? A) Yes of course! B) Mwaa, I don't know. C) No, my father forced me.. [A/B/C]? : ").lower()
	continue
	
if registration == "a":
	print("Great, welcome to the network!")
elif registration == "b":
	print("Come on, you can be more excited about this network!")
elif registration == "c":
	print("Ok, you have to work on your own motivation. Otherwise you are failling in life.")
       
print("Goodbye, thank you for joining the network.")
