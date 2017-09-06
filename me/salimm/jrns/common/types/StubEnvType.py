'''
Created on Jul 21, 2017

@author: Salim
'''
from enum import Enum


class StubEnvType(Enum):
    JAVA = 0
    PYTHON = 1 
    R = 2
    UNKNOWN = -1
    
    
    @classmethod
    def from_code(code):
        if(code == 1):
            return StubEnvType.JAVA
        elif(code == 2):
            return StubEnvType.PYTHON
        elif(code == 3):
            return StubEnvType.R
    
        return StubEnvType.UNKNOWN