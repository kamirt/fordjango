
"""
There is two lists of different lengths. In the first keys, in second - values. This function makes a
dictionary of this two lists. If values is not enough, keys must be with a "None" value. If keys not enough, they must be ignored.
"""

list1= [1,2,3,4,5, 6, 7, 8, 9, 10, 11, 12, 13]
list2=['f','g','h','n','m','a','t','u','k','u']

def listbreaker(list1, list2):
	d = {}
	for i in list1:
		if i<len(list2):
			d[list1[i-1]]=list2[i-1]
		else:
			d[list1[i-1]]=None
	return d
print listbreaker(list1, list2)

