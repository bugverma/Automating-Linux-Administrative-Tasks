import os

# CHECKING STATUS OF DOCKER
def checkingStatusOfDocker():
	cmd = 'systemctl status docker'
	return cmd

# TESTING INSTALLATION
def testingInstallation():
	cmd = 'docker container run hello-world'
	return cmd

# DOCKER INFORMATION

## VERSION BASIC
def dockerVersionBasic():
	cmd = 'docker --version'
	return cmd

## VERSION ADVANCED
def dockerVersionAdvanced():
	cmd = 'docker version'
	return cmd

## SYSTEM WIDE INFORMATION
def systemWideInformation():
	cmd = 'docker info'
	return cmd

# HELP

## GENERAL HELP
def generalHelp():
	cmd = 'docker help'
	return cmd

## MANAGEMENT COMMAND HELP
def managementCommandHelp(managementCommandName):
	cmd = 'docker {} help'.format(managementCommandName)
	return cmd

# SEARCH IMAGE ON HUB
def searchImage(imageName):
	cmd = 'docker search {}'.format(imageName)
	return cmd

# PULL IMAGE FROM HUB
def pullImage(imageName,version):
	cmd = 'docker image pull {}:{}'.format(imageName,version)
	return cmd

# LIST LOCALLY INSTALLED IMAGES
def listImages():
	cmd = 'docker image ls'
	return cmd

# LIST CONTAINERS

## RUNNING CONATINER
def listRunningContainer():
	cmd = ' docker container ls'
	return cmd

## EXITED CONTAINERS
def listExitedContainers():
	cmd = 'docker container ls -a -f status=exited'
	return cmd

##ALL CONTAINERS
def listAllContainers():
	cmd = 'docker container ls -a'
	return cmd

# RUN A CONTAINER

## WITHOUT A SHELL
def runWithoutShell(imageName):
	cmd = 'docker container run {}'.format(imageName)
	return cmd

## WITH A SHELL
def runWithShell(containerName,imageName):
	cmd = 'docker container run -it --name={} {}'.format(containerName,imageName)
	return cmd

# CREATE A CONTAINER
def createAContainer(portNumber,containerName,imageName):
	cmd = 'docker container create -p {}:80 --name {} {}'.format(portNumber,containerName,imageName)
	return cmd

# STARTING A CONTAINER
def startAContainer(containerName):
	cmd = 'docker container start {}'.format(containerName)
	return cmd

# STOPPING A CONTAINER
def stoppingAContainer(containerName):
	cmd = 'docker container stop {}'.format(containerName)
	return cmd

# CONNECT TO A CONTAINER
def connectToAContainer(containerName):
	cmd = ' docker container exec -it {} bash'.format(containerName)
	return cmd

# REMOVING CONTAINERS

## SPECIFIC
def removingSpecificContainer(containerName):
	cmd = 'docker container rm {}'.format(containerName)
	return cmd

## ALL CONTAINERS
def removingAllContainer():
	cmd = ' docker container rm $(docker container ls -a -f status=exited -q)'
	return cmd

# REMOVING IMAGES

## SPECIFIC
def removingSpecificImage(imageName):
	cmd = 'docker image rm {}'.format(imageName)
	return cmd

## ALL IMAGES
def removingAllImages():
	cmd = 'docker system prune -a'
	return cmd
print('\n')
print('\n')
print('KARTIK VERMA - 190BTCCSECS014 - SUSHANT UNIVERSITY - 6 SEMESTER PROJECT')
print('\n')
print('AUTOMATING RUNNING OF CONTAINERIZED APPLICATIONS USING DOCKER')
print('\n')
print('\n')

returnedCommand = ''

while True:

	print('CHOOSE AN OPTION: ')
	print('''
			 1. CHECKING STATUS OF DOCKER\n
			 2. TESTING INSTALLATION\n
			 3. DOCKER INFORMATION\n
			 4. HELP\n
			 5. SEARCH IMAGE ON HUB\n
			 6. PULL IMAGE FROM HUB\n
			 7. LIST LOCALLY INSTALLED IMAGES\n
			 8. LIST CONTAINERS\n
			 9. RUN A CONTAINER\n
			 10. CREATE A CONTAINER\n
			 11. STARTING A CONTAINER\n
			 12. STOPPING A CONTAINER\n
			 13. CONNECTING TO A CONTAINER\n
			 14. REMOVING CONTAINERS\n
			 15. REMOVING IMAGES\n
			 16. EXIT\n
			''')

	option = int(input('ENTER OPTION: '))
	print('\n')
	if option==1:
		returnedCommand = checkingStatusOfDocker()
	elif option==2:
		returnedCommand = testingInstallation()
	elif option==3:
		print('''
				 1. VERSION BASIC
				 2. VERSION ADVANCED
				 3. SYSTEM WIDE INFORMATION
				 
				 ''')
		internalOption = int(input('ENTER OPTION: '))
		if internalOption==1:
			returnedCommand=dockerVersionBasic()
		elif internalOption==2:
			returnedCommand=dockerVersionAdvanced()
		elif internalOption==3:
			returnedCommand=systemWideInformation()
	elif option==4:
		print('''
				 1. GENERAL HELP
				 2. MANAGEMENT COMMAND HELP
				 ''')
		internalOption = int(input('ENTER OPTION: '))
		if internalOption==1:
			returnedCommand=generalHelp()
		elif internalOption==2:
			managementCommandName = input('ENTER MANAGEMENT COMMAND NAME: ')
			returnedCommand=managementCommandHelp(managementCommandName)
	elif option==5:
		imageName = input('ENTER IMAGE NAME: ')
		returnedCommand=searchImage(imageName)
	elif option==6:
		imageName = input('ENTER IMAGE NAME: ')
		version = input('ENTER VERSION: ')
		returnedCommand=pullImage(imageName,version)
	elif option==7:
		returnedCommand=listImages()
	elif option==8:
		print('''
				 1. RUNNING CONTAINERS
				 2. EXITED CONTAINERS
				 3. ALL CONTAINERS
				 ''')
		internalOption = int(input('ENTER OPTION: '))
		if internalOption==1:
			returnedCommand=listRunningContainer()
		elif internalOption==2:
			returnedCommand=listExitedContainers()
		elif internalOption==3:
			returnedCommand=listAllContainers()
	elif option==9:
		print('''
				 1. WITHOUT A SHELL
				 2. WITH A SHELL
				 ''')
		internalOption = int(input('ENTER OPTION: '))
		if internalOption==1:
			imageName = input('ENTER IMAGE NAME: ')
			returnedCommand=runWithoutShell(imageName)
		elif internalOption==2:
			containerName = input('ENTER CONTAINER NAME: ')
			imageName = input('ENTER IMAGE NAME: ')
			returnedCommand=runWithShell(containerName,imageName)
	elif option==10:
		portNumber = input('ENTER PORT NUMBER: ')
		containerName = input('ENTER CONTAINER NAME: ')
		imageName = input('ENTER IMAGE NAME: ')
		returnedCommand=createAContainer(portNumber,containerName,imageName)
	elif option==11:
		containerName = input('ENTER CONTAINER NAME: ')
		returnedCommand=startAContainer(containerName)
	elif option==12:
		containerName = input('ENTER CONTAINER NAME: ')
		returnedCommand=stoppingAContainer(containerName)
	elif option==13:
		containerName = input('ENTER CONTAINER NAME: ')
		returnedCommand=connectToAContainer(containerName)
	elif option==14:
		print('''
				 1. SPECIFIC CONTAINERS
				 2. ALL CONTAINERS
				 ''')
		internalOption = int(input('ENTER OPTION: '))
		if internalOption==1:
			containerName = input('ENTER CONTAINER NAME: ')
			returnedCommand=removingSpecificContainer(containerName)
		elif internalOption==2:
			returnedCommand=removingAllContainer()
	elif option==15:
		print('''
				 1. SPECIFIC IMAGES
				 2. ALL IMAGES
				 ''')
		internalOption = int(input('ENTER OPTION: '))
		if internalOption==1:
			imageName = input('ENTER IMAGE NAME: ')
			returnedCommand=removingSpecificImage(imageName)
		elif internalOption==2:
			returnedCommand=removingAllImages()
	elif option==16:
		print('\n')
		print('\n')
		print('THANK YOU FOR USING THIS PROGRAM!')
		print('\n')
		print('\n')
		exit(0)
	else:
		print('WRONG OPTION ENTERED!')
		print('\n')

	os.system(returnedCommand)

	print()
	ch = input("DO YOU WANT TO CONTINUE (Y/n): ")
	if (ch=='n'or ch=='N'):
		break

print('\n')
print('THANK YOU FOR USING THIS PROGRAM!')
print('\n')
print('\n')