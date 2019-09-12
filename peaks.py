import numpy as n

def calc_ddx(array):
    # Computes sign changes in 1st derivative 
    if len(array) == 0:
        return n.zeros(0)
    return n.diff(n.sign(n.diff(n.pad(array,1,mode='reflect'))))    

def find_peaks(array,iterations):
    working_array = n.array(array).copy()
    working_points = n.arange(len(working_array))
    for i in range(iterations):
        working_array,working_points = iterate(working_array,working_points)
    return working_array,working_points

def iterate(array,points):
    localmax = n.diff(n.sign(n.diff(n.pad(array,1,mode='reflect')))) < 0 
    return array[localmax],points[localmax]

def general_peaks(array,iterations,function):
    working_array = n.array(array).copy()
    working_points = n.arange(len(working_array))
    for i in range(iterations):
        working_array,working_points = iterate(working_array,working_points)
    return working_array,working_points    

def extremum_iterate(array,points):
    # where 1st derivative changes sign 
    ddx = calc_ddx(array)
    ddx_max = calc_ddx(array[ddx < 0].copy()) < 0 
    ddx_min = calc_ddx(array[ddx > 0].copy()) > 0
    extremum = n.zeros(len(array),dtype=bool)
    extremum[ddx < 0] = ddx_max
    extremum[ddx > 0] = ddx_min

    return array[extremum],points[extremum]

    
