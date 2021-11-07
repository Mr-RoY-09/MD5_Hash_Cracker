import hashlib
print("This is MD5 hash password cracker only")
pass_hash = input("Enter md5 hash: ")
wordlist = input("File name: ")

counter = 0
flag = 0

#For Controling Error
try:
    pass_file = open(wordlist, "r")
    
except:
    print("No file found")
    quit()

#For Loop for keep trying every password combination 
for word in pass_file:
    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()
    
    #For Cheeking or Seeing every single line checking


    #print(word)
    #print(digest)
    #print(pass_hash)
    counter = +1


if digest == pass_hash:
    print("Password Found")
    print("Password is " + word)    
    flag = 1    
    breakpoint


if flag == 0:
    print("Password is not in the list.")
    print("Please try another file.")