word1=''
word2='python'
for i in range(10):
    word1=input("Wpisz słowo: ")
    if word1!=word2:
        print('Złe słowo')
    else:
        print('Gratulacje!')
        break