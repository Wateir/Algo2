def H (n , a , b ):
    print ("yeah")
    if ( n ==0):
        return b +1
    elif ( b ==0):
        if ( n ==1):
            return a
        elif ( n ==2):
            return 0
        else :
            return 1
    else :
        return H (n -1 , a , H (n , a , b -1));
def tests ():
#    print ( " ***** H (1 , 2 , 3) = " + str ( H (1 ,2 ,3)))
#    print ( " ***** H (1 , 3 , 3) = " + str ( H (1 ,3 ,3)))
#    print ( " ***** H (2 , 3 , 3) = " + str ( H (2 ,3 ,3)))
#    print ( " ***** H (3 , 2 , 3) = " + str ( H (3 ,2 ,3)))
    print ( " ***** H (4 , 2 , 3) = " + str ( H (4 ,2 ,3)))

tests()
