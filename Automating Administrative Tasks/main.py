import os

def checksSSHAuthenticationToEachHost(remainingCmd):
	print('''
			 1. PING MODULE
			 2. SETUP MODULE''')
	choice = int(input("ENTER CHOICE: "))
	if choice==1:
		remainingCmd = '-m ping'
	elif choice==2:
		remainingCmd = '-m setup'
	
	return remainingCmd

def shellModule(remainingCmd):
	print('''
		     1. FILE SYSTEM DISK SPACE USAGE
		     2. FREE AND USED MEMORY
		     3. LAST 3 USERS
		     4. MAC ADDRESS
		     5. CUSTOM''')
	choice = int(input("ENTER CHOICE: "))

	if choice==1:
		command = 'df -h'
	elif choice==2:
		command = 'free -m'
	elif choice==3:
		command = 'tail -n 3 /etc/passwd'
	elif choice==4:
		command="ip address show dev eth0|grep ether| cut -d' ' -f6 "
	elif choice==5:
		command = input("COMMAND: ")

	remainingCmd = '-m shell -a "{}"'.format(command)
	return remainingCmd

def scriptModule(remainingCmd):
	scriptName = input("ENTER SCRIPT NAME: ")
	scriptPath = input("ENTER {} PATH: ".format(scriptName))
	remainingCmd = '-m script -a "{}" --become'.format(scriptPath)
	return remainingCmd

def aptModule(remainingCmd):
	whatSoftware = ''
	print("ENTER THE TASK YOU WANT TO DO: ")
	print('''
			 1. INSTALL
			 2. UNINSTALL
			 3. FULL UPGRADE
			 4. REMOVE ADDITIONAL PACKAGES''')

	whatAction = int(input("ENTER OPTION : "))
	if whatAction==1:
		whatSoftware = input("ENTER SOFTWARE NAME: ")
		remainingCmd = '-m apt -a "name={} state=present update_cache=true" --become'.format(whatSoftware)
		return remainingCmd
	elif whatAction==2:
		whatSoftware = input("ENTER SOFTWARE NAME: ")
		remainingCmd = '-m apt -a "name={} state=absent purge=yes update_cache=true" --become'.format(whatSoftware)
		return remainingCmd
	elif whatAction==3:
		remainingCmd = '-m apt -a "upgrade=full" --become'
		return remainingCmd
	elif whatAction==4:
		remainingCmd = '-m apt -a "autoremove=yes autoclean=yes" --become'
		return remainingCmd
	else:
		print("THIS OPTION HAS NOT BEEN ADDED YET!")

def serviceModule(remainingCmd):
	whichService = ''
	print("CHOOSE WHAT YOU WANT TO DO WITH THE SERVICE: ")
	print('''
			 1. START
			 2. RESTART
			 3. STOP
			 4. ENABLE''')

	whatAction = int(input("ENTER OPTION: "))
	if whatAction==1:
		whichService = input("ENTER SERVICE NAME: ")
		remainingCmd = '-m service -a "name={} state=started" --become'.format(whichService)
		return remainingCmd
	elif whatAction==2:
		whichService = input("ENTER SERVICE NAME: ")
		remainingCmd = '-m service -a "name={} state=restarted" --become'.format(whichService)
		return remainingCmd
	elif whatAction==3:
		whichService = input("ENTER SERVICE NAME: ")
		remainingCmd = '-m service -a "name={} state=stopped" --become'.format(whichService)
		return remainingCmd
	elif whatAction==4:
		char = input("YES/ NO: ")
		if char=="yes":
			whichService = input("ENTER SERVICE NAME: ")
			remainingCmd = '-m service -a "name={} enabled=yes" --become'.format(whichService)
		else:
			whichService = input("ENTER SERVICE NAME: ")
			remainingCmd = '-m service -a "name={} enabled=no" --become'.format(whichService)
		return remainingCmd
	else:
		print("THIS OPTION HAS NOT BEEN ADDED YET!")

def usersAndGroup(remainingCmd):
	print('''
			 1. USER
			 2. GROUP
		''')
	usersOrGroup = int(input("ENTER CHOICE: "))
	if usersOrGroup==1:
		name = input("ENTER USER NAME: ")
		print('''
				 1. ADD
				 2. DELETE 
			  ''')
		choice = int(input("ENTER CHOICE: "))
		if choice==1:
			remainingCmd = '-m user -a "name={} state=present" --become'.format(name)
			return remainingCmd
		else:
			remainingCmd = '-m user -a "name={} state=absent" --become'.format(name)
			return remainingCmd
	elif usersOrGroup==2:
		name = input("ENTER GROUP NAME: ")
		print('''
				 1. ADD
				 2. DELETE
			  ''')
		choice = int(input("ENTER CHOICE: "))
		if choice==1:
			pass
			remainingCmd = '-m group -a "name={} state=present" --become'.format(name)
			return remainingCmd
		else:
			remainingCmd = '-m group -a "name={} state=absent" --become'.format(name)
			return remainingCmd


file = input("NAME OF THE INVENTORY FILE: ")
path = input("PATH OF {}: ".format(file))
commandToWhom = input("APPLY COMMANDS TO (host/ group/ all): ")
commandTo = input("NAME OF {}: ".format(commandToWhom))

stdCmd = "ansible -i {} {} ".format(path, commandTo)
remainingCmd = ''
returnedCommand = ''

while True:
	print("OPTIONS: ")
	print('''
			 1. CHECH SSH AUTHENTICATION TO EACH HOST
			 2. SHELL COMMANDS
			 3. USE SCRIPTs
			 4. USE APT 
			 5. SERVICES
			 6. USER AND GROUP
			 7. LIST ALL THE HOSTS IN THE INVENTORY FILE
			 8. EXIT''')
	options = int(input("ENTER OPTION: "))

	if options==1:
		returnedCommand = checksSSHAuthenticationToEachHost(remainingCmd)
	elif options==2:
		returnedCommand = shellModule(remainingCmd)
	elif options==3:
		returnedCommand = scriptModule(remainingCmd)
	elif options==4:
		returnedCommand = aptModule(remainingCmd)
	elif options==5:
		returnedCommand = serviceModule(remainingCmd)
	elif options==6:
		returnedCommand = usersAndGroup(remainingCmd)
	elif options==7:
		command = 'ansible -i ./hosts --list-hosts all'
		os.system(command)
		print('\n')
		continue;
	elif options==8:
		print('\n')
		print('THANK YOU FOR USING THIS PROGRAM!')
		print('\n')
		exit(0)
	else:
		print("WRONG OPTION ENTERED!")

	fullCommand = stdCmd + returnedCommand

	os.system(fullCommand)
	#print(fullCommand)

	print()

	ch = input("DO YOU WANT TO CONTINUE (y/ n): ")
	if (ch=='n'or ch=='N'):
		break

print('\n')
print('THANK YOU FOR USING THIS PROGRAM!')
print('\n')