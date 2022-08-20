import subprocess
class connectLinux(object):
    
    def __init__(self):
        self.iface=input("please enter current interface: ")
        self.address=input("please choose ip: ") # ip that is on the same network as the domain
        self.netmask=input("please enter your subnet: ")
        self.gateway=input("please enter your gateway: ")
        self.domain=input("please enter your domain *optional: ")
        self.dns=input("please enter your DNS: ")
        
    def cmd(self,command):
        p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        return p.stdout.read().decode(errors='replace').strip()


    def connectKali(self):
        if len(self.domain) < 1:
            return 'auto '+self.iface+'\n iface '+self.iface+' inet static\n address '+self.address+'\n netmask '+self.netmask+'\n gateway '+self.gateway+'\n dns-nameservers '+self.dns
        return 'auto '+self.iface+'\n iface '+self.iface+' inet static\n address '+self.address+'\n netmask '+self.netmask+'\n gateway '+self.gateway+'\n dns-domain '+self.domain+'\n dns-nameservers '+self.dns

    def connectubuntu(self):
        return 'network:\n  version: 2\n  ethernets:\n    '+self.iface+'\n      '+'dhcp4: no\n      dhcp6: no\n      addresses: ['+self.address+'/'+self.netmask+']\n      gateway4:  '+self.gateway+'\n      nameservers:\n              ['+self.dns+',8.8.8.8]'
        
        
        
    def writeScript(self,script,path,typ):
        if typ == 'a':
            script='\n'+script
        file = open(path,typ)
        file.write(script)
        file.close()
        return True
    
if __name__=='__main__':
    machine=input('what is your opretion system: ')
    test = connectLinux()
    if machine=='ubuntu':
        test.writeScript(test.connectubuntu(),'/etc/netplan/*.yaml','a')
        print('True')
        print(test.cmd('sudo netplan apply'))
    else:
        test.writeScript(test.connectKali(),'/etc/network/interfaces','a')
        print(test.cmd('systemctl restart networking'))
        test.cmd('shutdown -r now')
        
    
