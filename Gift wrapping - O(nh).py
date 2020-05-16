# Gift wrapping algorithm

import matplotlib.pyplot as plt




#The given points: 
Px=[2,0,2,6,12,15,10,4,5,6,8,9,8,8,6,6,11,10,6,5,4, 7, 8, 9, 1] #x coordinates
Py=[3,-2,-5,-8,-3,3,-2,-4,-5,-5,-5,-3,-3,-3,-3,-3,-2,-1,2,1,1, -7, 10, -9, 20] #y coordinates


Points  = [[2, 3], [0, -2], [2, -5], [6, -8], [12, -3], [15, 3], [10, -2], [4, -4],\
           [5, -5], [6, -5], [8, -5], [9, -3], [8, -3], [8, -3], [6, -3], [6, -3], \
           [11, -2], [10, -1], [6, 2], [5, 1], [4, 1], [7, -7], [8, 10], [9, -9], [1, 20]] #x,y coordinates in nested list
if(len(Points) < 3): #convex hull can be created only if the number of points is greater than 3
    print("Not enough points")


def giftWrap(S = Points): #Time complexity: O(nh)
    n = len(S)
    P = []
    k = outermost(S) #will find the outermost point by index
    p = k
    once = False
    while(True):
        if(p == 1 and once == True): #The outermost point is the part of the Convex Hull for sure.
            break
        P.extend([S[p]]) #Adds the outermost point first, then the other points based on coditions.
        q = (p + 1) % n # We need to save the last point we checked but the index cannot be greater than n so we use %n
        for i in range(n):
            if(orientation(S[p], S[i], S[q]) == 2): #if the point in i index has a greater counterclockwise angle than the current point on q index, then q = i
                q = i
        #After the loop we have the greatest angle, so we save it
        p = q
        once = True

    
    print("The points of the convex hull are: ", P)
    #if you don't want to use matplotlib just remove the following two lines
    P.extend([P[0]]) 
    plotter(P)



def outermost(p):
    l = 0
    for i in range(1, len(p)): #This function finds the outermost point on the left side
        if(p[i][0] < p[l][0]):
            l = i;
    return l# and it returns its index

def orientation(p, q, r): # this function decides the orientation of ordered triplet(p, q, r)
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0 #the three points are collinear
    if (val > 0):
        return 1 #Clockwise
    else:
        return 2 #Counterclockwise




def plotter(P): # it's a basic matplotlib plotter
    P.append(P[0])
    #print(P)
    m = len(P)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid(True)
    resultX = []
    resultY = []
    for i in range(m):
        resultX += [P[i][0]]
        resultY += [P[i][1]]
    ax.plot(Px,Py, 'r*')
    ax.plot(resultX, resultY)
    plt.show()


giftWrap()

    
