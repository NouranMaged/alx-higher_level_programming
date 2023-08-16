#!/usr/bin/python3
def search_replace(my_list, search, replace):
#    print(my_list)
#    return[replace if num == search else num for num in my_list]
   for i in my_list:
      if i == search:
         print ([replace])
         return [replace]
      else:
         print ([i])
         return [i]
   #for i in my_list: 
      #  if (i == search):
           # print(i)
            #i = replace
    #return 'my_list'
        # else:
        #     return i

search_replace([1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89],2,89)
