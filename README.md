# Filthy Peaks

A Filthy Way of Finding Peaks

I do not condone this for serious scientific purposes. 

# Basic Usage

    import filthypeaks.test as ft
    # contains tests    
    ft.alltests(1000,3)
    # runs tests on an array of length 1000 with 3 iterations

    import filthypeaks.peaks as fp
    # main code
    fp.find_peaks(array,iterations)
    # main function 
    fp.iterate(array,points)
    # perform a single iteration of max-of-max
    fp.extremum_iterate(array,points)
    # perform a single iteration of max-of-max and min-of-min

# Basic Idea

The basic idea is that local extrema form a hierarchy. On the root level are extrema of the array itself, and the next level are extrema of the extrema of that array. This can sometimes remove noise.

[[extremum.png]]
[[peaks.png]]