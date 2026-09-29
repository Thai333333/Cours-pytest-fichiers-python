from math import*

class point():
    mx=0
    my=0
    def __init__ (self):
        self.mx=0
        self.my=0

    def __init__(self, x, y):
        self.mx = x
        self.my = y

    def get_x(self):
        return self.mx

    def get_y(self):
        return self.my

    def set_x(self,x):
        self.mx = x
 
    def set_y(self,y):
        self.my = y

    def translation_x(self,trans_x):
        return self.mx + trans_x

    def translation_y(self,trans_y):
        return self.my + trans_y

    def coordonnees_du_point_apres_translation (self,trans_x,trans_y):
        mouvement_x=self.translation_x(trans_x)
        mouvement_y=self.translation_y(trans_y)
        return mouvement_x, mouvement_y

    def distance_entre_deux_points(self,p_2):
        return sqrt((self.mx - p_2.get_x())**2 + (self.my - p_2.get_y())**2)
    

a = point(0,0)
b = point(3,4)
print(a.distance_entre_deux_points(b))