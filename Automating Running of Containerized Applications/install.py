import os

cmd1 = 'apt install curl'
os.system(cmd1)

cmd2 = 'apt remove docker docker.io containerd runc'
os.system(cmd2)

cmd3 = 'curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -'
os.system(cmd3)

cmd4 = 'add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"'
os.system(cmd4)

cmd5 = 'apt update'
os.system(cmd5)

cmd6 = 'apt-cache policy docker-ce'
os.system(cmd6)

cmd7 = 'apt install docker-ce docker-ce-cli containerd.io'
os.system(cmd7)