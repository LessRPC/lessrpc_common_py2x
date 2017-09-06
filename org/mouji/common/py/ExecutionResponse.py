'''
Created on Jul 23, 2017

@author: Salim
'''
import json

from org.mouji.common.py.JRNSObject import JRNSObject
from org.mouji.common.py.info.ResponseInfo import ResponseInfo
from org.mouji.common.py.types.StatusType import StatusType

class ExecutionResponse(JRNSObject):
    
    
    def __init__(self, info, resultJson):        
        if(type(info) is 'dict'):
            self.stubType = ResponseInfo.from_dict(info)
        else:            
            self.info = info
        self.resultJson = resultJson


    def getResponseInfo(self):
        return self.info;
    
    
    def getObjectJson(self):
        return self.resultJson;
    
    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return ExecutionResponse(ResponseInfo(json_dict["info"]['outputType'], StatusType.fromCode(json_dict["info"]['statusType'])), json_dict['resultJson']);
    
        
    @classmethod
    def from_dict(cls, fieldsDict):  
        return ExecutionResponse(ResponseInfo(fieldsDict["info"]['outputType'], StatusType.fromCode(fieldsDict["info"]['statusType'])), fieldsDict['resultJson']);
    