def prime_numbers(number):
    if number <2:
        return False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            return False
    return True

def filter_prime(numbers):
    filter_numbers=[number for number in numbers if prime_numbers(number)]
    return filter_numbers

user_input=input()
number_list=[int(number) for number in user_input.split()]

prime_result=filter_prime(number_list)

print(prime_result)
