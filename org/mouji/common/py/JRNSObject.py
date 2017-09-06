'''
Created on Jul 21, 2017

@author: Salim
'''

import json

class JRNSObject(object):
        
        
    @classmethod
    def from_json(cls, json_str):
        json_dict = json.loads(json_str)
        return cls(**json_dict)
    
    def to_json(self):
        return json.dumps(self.__dict__)
        
    @classmethod
    def from_dict(cls, fieldsDict):    
        return cls(**fieldsDict) 