'''
python revision after my first week
practice python 
'''
square_num :list[int] = [i*i for i in range(10)]
print(square_num)

# to print even numbers in list comprehension
even_num : list[int]= [i for i in range(20)if i%2==0]
print(even_num)

#length of words 

words : list[str] = ["apple" , "orange" , " preserves","mango", "gauva"]
words_length :list[int]=[len(word) for word in words]
print (words_length)

#filter and modify words:
to_filter :list[int]=[i for i in range(30)if i%3==0 ]
print(to_filter)
# to print numbers in reverse order

list_of_lists :list[list[int]] = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
flatened_list :list[int] =[item for sublists in list_of_lists for item in sublists ]
print(flatened_list)

list_of_fruits : list[str]= ["apple", "orange", "mango", "watermelon", "pineapple"]
first_letter : list[str]=[word[0] for word in list_of_fruits]
print(first_letter)