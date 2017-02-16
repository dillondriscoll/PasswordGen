import random

def main():
    
    choice = int(input("Enter the length of the password(12+ characters is safest)"))
    print(generator(choice))

def generator(choice):
    
    letterbank = 'aeiouyAEIOUYbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ123456789'
    randomChars = ['!','@','#','$','%','^','&','*','(',')']
    name = []
    for i in range(0,choice-1):
        name.insert(i,random.choice(letterbank))
    randomNewChar = random.randint(0,len(name))
    name.insert(randomNewChar,randomChars[random.randint(0,len(randomChars))])
    newName = "".join(name)
    return newName

main()
