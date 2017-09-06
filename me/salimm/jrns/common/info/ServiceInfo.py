'''
Created on Jul 21, 2017

@author: Salim
'''
from me.salimm.jrns.common.JRNSObject import JRNSObject


class ServiceInfo(JRNSObject):
    
    def __init__(self, name, sid):
        self.name = name
        self.sid = sid



    def getName(self):
        return self.name;
    
    def getId(self):
        return self.sid;                