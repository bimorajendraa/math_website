import matplotlib
import math

class bangundatar:
    class persegi:
        def __init__(self, sisi=0.0):
            self.sisi = sisi
        
        def keliling(self):
            return self.sisi * 4
    
        def luas(self):
            return self.sisi * self.sisi
        
        def luas_sisi(self, luas):
            return math.sqrt(luas)

        def kel_sisi(self, kel):
            return kel / 4
    
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

class gerak:
    class glb:
        def jarak(self, kecepatan, waktu):
            return kecepatan * waktu
        
        def kecepatan (self, jarak, waktu):
            return jarak / waktu
        
        def waktu(self, jarak, kecepatan):
            return jarak / kecepatan

        def vt(self, vo, a, t):
            return vo + a * t

    class glbb:
        def kecepatan(self, jarak, waktu):
            return jarak / waktu
        def jarak(self, waktu, kecepatan):
            return kecepatan / waktu
    
    class gv:
        def smaks(self, vo, vt, t):
            return (vo * t) + (vt * t) / 2

        


        

            

a = bangundatar()
b = a.persegi()