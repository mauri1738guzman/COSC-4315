import sys


def read_arguments(input):
        
        input = input.split(";")
        
        #-- assign vrariables here
        # pint("k: ")
        k = input[0]
        k = k.split("=")
        k = int(k[1])
        # print(k)
        # print("input file name: ")
        inputVal = input[1]
        inputVal = inputVal.split("=")
        inputVal = inputVal[1]
        # print(inputVal)
        # print("Output File name: ")
        output = input[2]
        output = output.split("=")
        output = output[1]
        # print(output)

        #Here we will store the input files into a list
        txt_file = open(inputVal, "r")
        input_X = txt_file.read()

        # print("Here is the file: ")
        # print(input_X)
        c1 = ''
        # print("element 8: ")
        # print(input_X[8])
        # if input_X[8].isupper or input_X[8].isupper:
        #         print("True")
        c2 = ' '
        c1 ='.'
        
  
        #This is the new array without letters/symbols/enters
        new = list(map(lambda x: x if (x=='0' or x=='1' or x=='2' or x=='3' or x=='4' or x=='5' or x=='6' or x=='7' or x=='8' or x=='9' or x=='-') else \
                c1 if (x==c1) else c2,input_X))
  
        
        just_Nums = ''.join(new)


       
        # print("Here is without letters: ")
        # print(just_Nums)

       
        
        B = list(map(lambda x: x, just_Nums.split()))
        # print(B)
        #-- Here we will assign these to a different list
        intList = list(filter(lambda x: x.lstrip('-').isdigit() or x.isdigit() , B))
        floatList = list(filter(lambda x: float(x) if str(float(x)) == x else '' , B))

        #-- Here is the strings converted to their respective variable format
        intList = list(map(lambda x: int(x), intList ))
        floatList = list(map(lambda x: float(x), floatList))



        

       
        
        # print("Floats are right here: ")
        # print(floatList)
        # print("Here is the intList")
        # print(intList)
       
        

       
        #-- Removed all the unnecesary spaces we dont need
        # file_content = re.sub("\n", ' ', file_content)
        # file_content = re.sub("  ", ' ', file_content)
        
        
        #store values in a list
        
        return intList, floatList, output, k
        

        #-- Here begins the sort function 

def sort_lambda(c):
    
    if(len(c) <= 2):
        final_array = lambda x: x if len(x) <= 1 else x if x[0] < x[1] else [x[1], x[0]] 
        fin = final_array(c)
        return fin
    else:
    
        #-- Assing the variables to be compared
        a = c[0]
        b = c[1]
        bs = c[2:]

        res = []

        #-- Here  and b will be compared and return the rest of the array with a or b sorted
        compare_ab = lambda a,b, bs: [a] + sort_lambda([b] + bs) if a < b else [b] + sort_lambda([a] + bs)
        res = compare_ab(a,b,bs)

        #Here is the sort function


        return sort_lambda(res[:-1]) + res[-1:]

def count_create(list_v, seen_int, count, index):

        #-- best case 
        if(index == len(seen_int)):
                return count

        #-- Here is the main body
        intList = list(filter(lambda x: x == seen_int[index],  list_v))
        count[index]  = len(intList)

       
        return  count_create(list_v, seen_int, count, index + 1)
       


def combineArray(count_list, nums_list):

    return list(map(lambda x, y:[x,y], count_list, nums_list))







#-- Here is the create file function for the intergers: 
def createFile(tuple, f, index, k):

        #when k == 0 check if next one is a tie
        if(k == 0 or index < 0):
                if(tuple[index + 1][0] == tuple[index][0]):
                        f.write(str(tuple[index][1]))
                        f.write(" ")
                        f.write(str(tuple[index][0]))
                        f.write("\n") 
                     
                
                f.close()
        else: 
                #This is the main recursive function that will repeat
                f.write(str(tuple[index][1]))
                f.write(" ")
                f.write(str(tuple[index][0]))
                f.write("\n")
                createFile(tuple, f, index -1, k - 1)


        




        

def main():
        input = sys.argv[1]
        
        #done getting argument values inputted 
        int_variables, float_variables, outputName, k = read_arguments(input)
        
        #-- Sort the int list
        int_list = sort_lambda(int_variables)
        print("This is sorted: ")
        print(int_list)
        float_list = sort_lambda(float_variables)
        print("This is float sorted: ")
        print(float_list)

        #Here we need to make list w/out duplicates
        seen_int = []
        seen_int = list(filter(lambda x: seen_int.append(x) is None if x not in seen_int else False, int_list))
        print("These are the list w/out duplicates: ")
        print(seen_int)
        #here is the float
        seen_float = []
        seen_float = list(filter(lambda x: seen_float.append(x) is None if x not in seen_float else False, float_list))
        print("These are the list w/out duplicates: ")
        print(seen_float)
        
        print("occurences(int): ")
        index = 0
        N_int = len(seen_int)
        count_int = [0] * N_int
        count_array_int = count_create(int_list, seen_int, count_int, index)
        print(count_array_int)

        print("occurences(float): ")
        N_float = len(seen_float)
        count_float = [0] * N_float
        count_array_float = count_create(float_list, seen_float, count_float, index)
        print(count_array_float)


        tuple_int = combineArray(count_array_int, seen_int)

        tuple_float = combineArray(count_array_float, seen_float)

        print("Here is the tuple of integers: ")
        print(tuple_int)
        print("Here is the tuple of float: ")
        print(tuple_float)

        sorted_tuple_int = sort_lambda(tuple_int)
        print("Here is the tuple sorted: ")
        print(sorted_tuple_int)

        sorted_tuple_float = sort_lambda(tuple_float)
        print("Here is the tuple sorted: ")
        print(sorted_tuple_float)


        f = open(outputName, "w")
        f.write("integer:\n")

        index_int = len(sorted_tuple_int) - 1
      
        createFile(sorted_tuple_int, f, index_int,k )



        f_float = open(outputName, "a")
        f_float.write("float:\n")

        
        index_float = len(sorted_tuple_float)-1
        createFile(sorted_tuple_float, f_float, index_float,k )


      
       
        
        

        


        

     
if __name__ == "__main__":
        main()

