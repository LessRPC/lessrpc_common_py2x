'''
Created on Jul 21, 2017

@author: Salim
'''
from org.mouji.common.py.JRNSObject import JRNSObject
from org.mouji.common.py.types.StubEnvType import StubEnvType



class ClientInfo(JRNSObject):
    
    
    def __init__(self, url, stubType):
        self.url = url
        if(type(stubType) is 'int'):
            self.stubType = StubEnvType.from_code(stubType)
        else:            
            self.stubType = stubType
        
        
    
    def getURL(self):
        return self.url;
    
    
    def getType(self):
        return self.stubType;
    
