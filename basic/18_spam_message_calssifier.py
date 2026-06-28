def countInvalidChar(content):
    count = 0
    for c in content:
        if not c.isalnum() and c != ' ':
            count += 1
    return count

user = input()
content = input()

isInvalidSender = user.isdigit()
isInvalidContent = countInvalidChar(content) > (len(content) / 2) and 'spam' in content.lower()

if isInvalidContent and isInvalidSender:
    print('Fully Invalid')

elif isInvalidContent:
    print('Invalid Content')
    
elif isInvalidSender:
    print('Invalid Sender')

else:
    print('Not Spam')
