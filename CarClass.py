class Abstrackt(object):
    def __init__(self,name,otagh,shasi,charkh):
        self.otagh=otagh
        self.shasi=shasi
        self.charkh=charkh
        self.name=name

    def Tedad_charkh(self,charkh):
        
        return "{} daraye {} charkh ast".format(self.name,charkh)
    
    def Harkat(self):
        return "{} harkat kard".format(self.name)

    def Tavaghof(self):
        return "{} tavaghof kard".format(self.name)

    def Otagh(self,otagh):
        return "{} {} darad".format(self.name,otagh)

    def Shasi(self,shasi):
        return "{} {} darad".format(self.name,shasi)


class Bus(Abstrackt):

    def __init__(self,name):
        self.name=name

    @staticmethod
    def Color(color):
        print('ootooboos ',color,' ast')

    def Nahve_kar (self):
        return "{} mosaferan ra be maghsad miresanad".format(self.name)

class Truck(Abstrackt):

    def __init__(self,name):
        self.name=name

    def Color(self):
        return "kamioon {} ast".format(self)
        
        
    def Nahve_kar(self,name):
        return "{} bar ra be mahle mored nazar mibarad".format(self.name)

Bus_1=Bus('ootooboos')
print(Bus_1.Harkat())
print(Bus_1.Tedad_charkh(9))

Bus_2=Bus('ootooboos')
print(Bus_2.Nahve_kar())

print(Truck.Color('ghahveei'))

Bus.Color('zard')