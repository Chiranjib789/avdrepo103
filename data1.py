a = [5,9,12,8,10];

num = int(input('Enter any number : '));

for i in a:
    if i == num:
        print('Your number found');
        break;
else:
    print('Sorry number not available');