def reverse_string(sentance):
    string = sentance.split()
    sentance_reversed=' '.join(reversed(string))
    return sentance_reversed
user_input=input()
result=reverse_string(user_input)
print(result)
