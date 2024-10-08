#sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Find the length of the set it_companies
print(len(it_companies))

#add Twitter to it_companies
it_companies.add('Twitter')
print(it_companies)

#Insert multiple IT companies at once to the set it_companies
it_companies.update(['LinkedIn', 'Instagram', 'Snapchat'])
print(it_companies)

#Remove one of the companies from the set it_companies
it_companies.remove('IBM')
print(it_companies)

#What is the difference between remove and discard
#remove will raise an error if the element is not found in the set

#Join A and B
print(A.union(B))

#Find A intersection B
print(A.intersection(B))

#Is A subset of B
print(A.issubset(B))

#Are A and B disjoint sets
print(A.isdisjoint(B))

#Join A with B and B with A
A.update(B)
B.update(A)
print(A)
print(B)

#What is the symmetric difference between A and B
print(A.symmetric_difference(B))

#Delete the sets completely
del A
del B
del it_companies

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(len(age_set))
print(len(age))

#Explain the difference between the following data types: string, list, tuple and set
#string is a sequence of characters, list is an ordered collection of items, tuple is an ordered collection of items that cannot be changed, set is an unordered collection of unique items

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?  Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
sentence_set = set(sentence.split())
print(len(sentence_set))

