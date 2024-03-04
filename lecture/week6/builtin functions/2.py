def count_upper_lower(string):
    upper_count=sum(1 for char in string if char.isupper())
    lower_count=sum(1 for char in string if char.islower())
    return upper_count,lower_count
string=str(input())
upper_count,lower_count=count_upper_lower(string)
print("Upper count:",upper_count,"and","lower count:",lower_count)