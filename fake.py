
def count_create(list_v, seen_int, count, index):

        #-- best case 
        if(index == len(seen_int)):
                return count

        #-- Here is the main body
        intList = list(filter(lambda x: x == seen_int[index],  list_v))
        count[index]  = len(intList)

       
        return  count_create(list_v, seen_int, count, index + 1)
       

def combineArray(count_list, nums_list):

    return list(map(lambda x, y:(x,y), count_list, nums_list))

def print_toFile(tuple, fileName, index, k, count):


    #Here we need to output the tuple 
    if(k == count and index > 0):
        if(tuple[index][0] == tuple[index-1][0]):
             the_file.write(tuple[index][1] + " " + tuple[index][0])
             print_toFile(tuple, fileName, index-1, k, count+1)
        else: 
            return 

            
    with open(fileName, 'a') as the_file:
        the_file.write("integer: ")
        the_file.write(tuple[index][1] + " " + tuple[index][0])
        print_toFile(tuple, fileName, index-1, k, count+1)


    


def main():
    int_v = [1,2,4]
    int_v_duplicates = [1,1,2,2,2,4]    
   

    N = len(int_v)
    ar = [0]*N
    print(ar)
    index = 0


    case = count_create(int_v_duplicates, int_v, ar, index)
    print("Here is the new array: ")
    print(case)

    tuple = combineArray(case, int_v)
    print("Here is the tuple: ")
    print(tuple)
   




    


    
    

if __name__ == "__main__":
    main()