'''
Created on Jul 23, 2017

@author: Salim
'''

from enum import Enum


class StatusType(Enum):
    
    OK = 0
    INPUT_ERROR = 1
    SERVER_CRASH = 2
    CLIENT_STUB_TYPE_NOT_SUPPORTED = 3
    UNKNOWN = -1
    
    @classmethod
    def parse(cls, name):
        if(name == StatusType.OK.name):
            return StatusType.OK; 
        elif(name == StatusType.INPUT_ERROR.name):
            return StatusType.INPUT_ERROR;
        elif(name == StatusType.SERVER_CRASH.name):
            return StatusType.SERVER_CRASH;
        elif(name == StatusType.CLIENT_STUB_TYPE_NOT_SUPPORTED.name):
            return StatusType.CLIENT_STUB_TYPE_NOT_SUPPORTED; 
        return StatusType.UNKNOWN;
    
    def getCode(self):
        return StatusType.toCode(self);
    
    @classmethod
    def toCode(cls, tpe):        
        if(tpe is StatusType.OK):
            return StatusType.OK.value;
        elif(tpe is StatusType.INPUT_ERROR):
            return StatusType.INPUT_ERROR.value;
        elif(tpe is StatusType.SERVER_CRASH):
            return StatusType.SERVER_CRASH.value;
        elif(tpe is StatusType.CLIENT_STUB_TYPE_NOT_SUPPORTED):
            return StatusType.CLIENT_STUB_TYPE_NOT_SUPPORTED.value;
        return StatusType.UNKNOWN.value;
         
            
    @classmethod        
    def fromCode(self, code):
        
        if(code is StatusType.OK):
            return StatusType.OK;
        elif(code is StatusType.INPUT_ERROR):
            return StatusType.INPUT_ERROR;
        elif(code is StatusType.SERVER_CRASH):
            return StatusType.SERVER_CRASH;
        return StatusType.UNKNOWN;
        
        
        
        
    
    
