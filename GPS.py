'''

(Geography: estimate areas) Find the GPS locations for Atlanta, Georgia;
Orlando, Florida; Savannah, Georgia; and Charlotte, North Carolina from
www.gps-data-team.com/map/ and compute the estimated area enclosed by these
four cities. (Hint: Use the formula in Programming Exercise 3.2 to compute the
distance between two cities. Divide the polygon into two triangles and use the formula in Programming Exercise 2.14 to compute the area of a triangle.)

'''
import math

from Assignments import myLib

#coordinates
atlanta_x , atlanta_y = -84.4253829 , 33.768659
orlando_x, orlando_y = -81.30652 , 28.45627
savannah_x,savannah_y = -94.829037 , 39.941143
ncarolina_x,ncarolina_y = -80.271346 , 36.0895533

#degrees
ncarolina_x_degree,ncarolina_y_degree = math.radians(80), math.radians(36)
savannah_x_degree,savannah_y_degree = math.radians(94), math.radians(39)
orlando_x_degree,orlando_y_degree =math.radians(81), math.radians(28)
atlanta_x_degree,atlanta_y_degree =math.radians(84), math.radians(33)



#Calculate distances

d_orl_atl = myLib.great_circle_distance(orlando_x_degree,atlanta_x_degree,orlando_y_degree,atlanta_y_degree)
d_atl_sav =myLib.great_circle_distance(atlanta_x_degree,savannah_x_degree,atlanta_y_degree,savannah_y_degree)
d_orl_sav = myLib .great_circle_distance(orlando_x_degree,savannah_x_degree,orlando_y_degree,savannah_y_degree)
d_sav_ncarol =myLib.great_circle_distance(savannah_x_degree,ncarolina_x_degree,savannah_y_degree,ncarolina_y_degree)
d_atl_nacarol = myLib.great_circle_distance(atlanta_x_degree,ncarolina_x_degree,atlanta_y_degree,ncarolina_y_degree)

area1 = myLib.area_of_triangle_sides(d_orl_sav,d_atl_sav,d_orl_sav)
area2 = myLib.area_of_triangle_sides(d_atl_nacarol,d_sav_ncarol,d_atl_sav)
totalArea = area1 + area2

print("Total Area =  " + str(totalArea))
