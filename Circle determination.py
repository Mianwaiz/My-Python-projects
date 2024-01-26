# for pie
import math
pi_value = math.pi 
#code starts here
class Circle:
    def get_radius(self, radius):
        self.radius = radius
    def calculate_circle(self):
    	self.area=pi_value*self.radius**2
    	self.perim=2*pi_value*self.radius
    	print(f'area is {self.area} and perimeter is {self.perim}')
circle = Circle()
add_radius=circle.get_radius(5)
print(circle.calculate_circle())
