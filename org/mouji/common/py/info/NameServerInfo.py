'''
Created on Jul 21, 2017

@author: Salim
'''
from org.mouji.common.py.JRNSObject import JRNSObject


class NameServerInfo(JRNSObject):
    
    def __init__(self, address, port):
        self.address = address
        self.port = port
        
        
        
    def getAddress(self):
        return self.address;
    
    def getPort(self):
        return self.port;            