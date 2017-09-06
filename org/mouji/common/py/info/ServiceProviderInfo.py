'''
Created on Jul 21, 2017

@author: Salim
'''
from org.mouji.common.py.JRNSObject import JRNSObject
from org.mouji.common.py.types.StubEnvType import StubEnvType


class ServiceProviderInfo(JRNSObject):
    
    def __init__(self, ip, port, providerName, stubType):
        self.ip = ip
        self.port = port
        self.providerName = providerName
        
        if(type(stubType) is 'int'):
            self.stubType = StubEnvType.from_code(stubType)
        else:            
            self.stubType = stubType
        
        
    def getIP(self):
        return self.ip;
    
    def getPort(self):
        return self.port;
    
    def getName(self):
        return self.port;
    
    def getType(self):
        return self.stubType
