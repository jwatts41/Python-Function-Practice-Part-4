# Write a function to find the maximum of three numbers
def max_num(a, b, c):
    return max([a,b,c])


print(max_num(10,20,30))


#Write a function to multiply all the numbers in a list
def mult_list(numbers):
    result = 1
    for number in numbers:
        result += number
    return result 

print(mult_list([2,4,6,8]))  

#Write a function to reverse a string
def rev_string(my_rev):
    return my_rev[::-1]
    
text = rev_string("I love Python")

print(text)

#Write a function to check whether a number falls in a given range
def num_within(a, b, c):
    return a in range(b, c+1)

print(num_within(8,4,2))


#Write a function that out the first n rows of Pascal's Triangle
def pascal(n):
    for i in range(n):
        row = [1]*(i+1)
        for j in range(1, i):
            prev_row = row
            row[j] = prev_row[j-1] + prev_row[j]
            print(row)

pascal(5)
