string1 = "This is  CodeAcademy"
string2 = "CodeAcademy is an eductional center"
string3 = "This is a great day"
word = "CodeAcademy"



#Split the string into a list of words
word_list1 = string1.split()
word_list2 = string2.split()
word_list3 = string3.split()
print(word_list1)


'''for i, value in enumerate(word_list1, 1):
    print(i, value)# 1 Alice
    
if word in word_list1:
    position = range(word_list1, 1).index(word)
    print(f"{string1}\n I found {word} at {position}")

else:
    print(f"I didn't find {word}\n")'''
# 2 Bob
# 3 Charlie


#position = word_list.index(word)  # Find the position of the word in the list

#print(f"I found {word} at {position}")


  
    
if word in word_list1:
    position = word_list1.index(word)+1
    print(f"{string1}\n I found {word} at {position}")
else:
    print(f"I didn't find {word}\n")

if word in word_list2:
    position = word_list2.index(word)+1
    print(f"{string2}\nI found {word} at {position}")
else:
    print(f"I didn't find {word}")
    
if word in word_list3:
    position = word_list2.index(word)+1
    print(f"{string3}\nI found {word} at {position}")
else:
    print(f"{string3}\nI didn't find {word}.")
    
    
   
