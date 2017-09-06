'''
Created on Jul 23, 2017

@author: Salim
'''
from org.mouji.common.py.JRNSObject import JRNSObject
from org.mouji.common.py.types.StatusType import StatusType


class ResponseInfo(JRNSObject):
    
    def __init__(self, outputType, status):
        self.outputType = outputType
        if(type(status) is 'int'):
            self.status = StatusType.fromCode(status)
        else:            
            self.status = status
                
        
        
        
    def getStatus(self):
        return self.status
    
    
    def getOutputType(self):
        return self.outputType;
    
        