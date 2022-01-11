<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 23:53:52 2017

@author: LSayhi
"""

class Employee():
    """创建雇员信息，返回年薪"""
    def __init__(self,firstname,lastname,year_rasie):
        self.firstname=firstname
        self.lastname =lastname
        self.year_rasie=year_rasie
    def give_raise(self,new_rasie=5000):
        self.year_rasie+=int(new_rasie)
        return (self.year_rasie)
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 23:53:52 2017

@author: LSayhi
"""

class Employee():
    """创建雇员信息，返回年薪"""
    def __init__(self,firstname,lastname,year_rasie):
        self.firstname=firstname
        self.lastname =lastname
        self.year_rasie=year_rasie
    def give_raise(self,new_rasie=5000):
        self.year_rasie+=int(new_rasie)
        return (self.year_rasie)
>>>>>>> 44df36ffcbf1d4daced980d12300e7efa2c4f8e2
        