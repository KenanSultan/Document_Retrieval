def create_list():
    with open('ap_docs.txt', 'r') as file:
        genel = file.read().split('<NEW DOCUMENT>')
    return genel

def search(genel):
    myMap = map(lambda x: set(x.replace('\n', ' ').lower().replace('.', '').replace(',', '').split(' ')), genel)
    words = set(input("\nEnter search words: ").lower().strip().split(' '))
    numbers = (str(i) for i, j in enumerate(myMap) if words.issubset(j))
    print('\nDocuments fitting search:'," ".join(numbers), "\n")

def read(genel):
    num = input('\nEnter document number: ')
    print('\nDocument #' + num)
    print('\n--------------------------------------------')
    print(genel[int(num)])
    print('--------------------------------------------\n')

while True:
    print("1. Search for documents")
    print("2. Read Document")
    print("3. Quit Program")

    option = input("What would you like to do? ")

    if option == '1':
        genel = create_list()
        search(genel)
    elif option == '2':
        genel = create_list()
        read(genel)
    elif option == '3':
        print("\nBye\n")
        exit()
    else:
        print("Choose 1 or 2 or 3")
        continue