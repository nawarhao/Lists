#create an empty list
empty_list = []
print()

#a list of numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)

#use * operator
triples = [1, 2, 3] * 3
print(triples)

#reverse the given list
aList = [100, 200, 300, 400, 500]
aList = aList[::-1]
print(aList,"\n")

#word matching

#function to check whether
#first and last character of words match
def match_words(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word [-1]:
            ctr += 1
            lst.append(word)
            
    print("List 0f words with first and last character seem\n", lst)
    return ctr

count = match_words(['abc', 'cfc', 'xyz', 'aba', '1221'])
print("Number of words having first and last character same:", count)


#activity 3
L = [4, 5, 1, 2, 9, 7, 10, 8]
print("Original list:", L)

#variable to store the sum of
# the list
sum = 0

#finding the sum
for i in L:
    count += i
    
#divide the total element by
#number of elements
avg = count/len(L)

print("sum= ", count)
print("average=", avg)

#sorting the element of the list
L.sort()

print("The sorted list is", L)

#printing the first element
print("Sallest element is:", L[0])

#printing the last element
print("Largest element is:", L[-1])