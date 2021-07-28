from abc import ABC, abstractmethod, abstractstaticmethod, abstractclassmethod


class Band:


    all_bands=[]
    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.all_bands.append(self.name)




    def play_solos(self):
        for x in self.members:
            pass

    
    def __str__(self):
        pass

    def __repr__(self):
        pass

    
    def to_list(cls):
        pass


class Musician(ABC):
    def __init__(self,name,instrument,role,solo_play):
        self.name=name
        self.instrument=instrument
        self.solo_play=solo_play
        self.role=role

    def __str__(self):
        return f"My name is {self.name} and I play {self.instrument}"
    
    def __repr__(self):
        return f"{self.role} instance. Name = {self.name}"

    def get_instrument(self):
        return self.instrument

    
    def play_solo(self):
        return self.solo_play


class Guitarist(Musician):
    instrument="guitar"
    solo_play="face melting guitar solo"
    role="Guitarist"

    def __init__(self, name):
        super().__init__(name,Guitarist.instrument,Guitarist.role,Guitarist.solo_play)

class Bassist(Musician):
    instrument="bass"
    solo_play="bom bom buh bom"
    role="Bassist"
  

    def __init__(self, name):
        super().__init__(name,Bassist.instrument,Bassist.role,Bassist.solo_play)

class Drummer(Musician):
    instrument="drums"
    solo_play="rattle boom crash"
    role="Drummer"
    def __init__(self, name):
        super().__init__(name,Drummer.instrument,Drummer.role,Drummer.solo_play)