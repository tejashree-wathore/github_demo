# TODO: Find all one digit to 10 digit numbers for which abcd * 4 = dcba

def find_all_pallindrome_numbers():
    for number in range(1000, 10000):
        num_rev = int(str(number)[::-1])
        if number * 4 == num_rev:
            return number
ans = find_all_pallindrome_numbers()
print(ans)