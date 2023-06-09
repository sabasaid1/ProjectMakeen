# Print the number that has a value greater than or equal to the values on the right side?

#input:{1,4,5,7,3,0} output: 0 3 7
#nput:{1,2,3,4} output: 4



numbers = input("Enter a number: ").split()
result = []

for i in range(len(numbers)):
    current_number = numbers[i]
   
    right_side_values = numbers[i+1:]
    if all(current_number >= num for num in right_side_values):
        result.append(current_number)
result.sort()
for i in result:
  print(i,end=" ")


