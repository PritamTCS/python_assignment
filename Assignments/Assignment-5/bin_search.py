#! /usr/bin/python3

class myTest:
    def __init__(self,array,upper):
        self.upper=upper
        self.array=array

    def binary(self,n):
        lower=0
        upper=self.upper
        while lower <= upper :
            mid = int((lower+upper)/2)

            if (n < array[mid]) :
                upper = mid - 1
            elif n > array[mid] :
                lower = mid + 1
            elif n==array[mid] :
                return mid
        return -1

if __name__ == '__main__' :
    #array=[0,1,2,3,4,5,6,7,8,9,10]
    ip_list=input("Please enter the numbers to be included in the list separated by space :\t")
    array=[]
    for i in ip_list.split(' ') :
        array.append(int(i))
    no_to_search=int(input("Please enter the number to be searched in the array : \t"))
    t=myTest(array,len(array)-1)
    x=t.binary(no_to_search)

    if x == -1 :
        print ("Not found")
    else :
        print ("found at %d " %x)