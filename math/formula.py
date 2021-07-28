import matplotlib

class bangundatar:
    class persegi:
        def __init__(self, sisi=0.0):
            self.sisi = sisi
        
        def keliling(self):
            return self.sisi * 4
    
        def luas(self):
            return self.sisi * self.sisi
    
    class persegip:
        def __init__(self, p, l):
            self.panjang = p
            self.lebar = l
    
        def keliling(self):
            return (self.panjang + self.lebar) * 2
        
        def luas(self):
            return self.panjang * self.lebar

    class segitiga:
        def __init__(self, lebar):
            self.lebar = lebar

        def keliling(self, sisi1, sisi2):
            self.sisi1 = sisi1
            self.sisi2 = sisi2
            return self.lebar + self.sisi1 + self.sisi2

        def luas(self, tinggi):
            self.tinggi = tinggi
            return self.lebar * self.tinggi / 2


        

            

a = bangundatar()
b = a.persegi(3)
print(b.luas())

