password='python'
for i in range(10):
    word=input("Wpisz słowo: ")
    if word==password:
        print('Gratulacje!')
        break
else:
        print('Przegrales!')
