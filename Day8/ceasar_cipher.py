running = True

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while running:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def ceasar(direction, text, shift):
        if shift > 26:
            shift = shift % 26
        if direction.lower() == "encode":
            return encrypt(text, shift)
        elif direction.lower() == "decode":
            return decrypt(text, shift)
        else:
            return "enter valid direction"

    #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
    def encrypt(text, shift):
        new_letters=[]
        for letter in list(text):
            if letter in alphabet:
                alphabet_index = alphabet.index(letter)
                new_index = alphabet_index + shift
                if new_index >= 26:
                    new_index = new_index % 26
                new_letters.append(alphabet[new_index])
            else:
                new_letters.append(letter)
        return "".join(new_letters)
        #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
        #e.g. 
        #plain_text = "hello"
        #shift = 5
        #cipher_text = "mjqqt"
        #print output: "The encoded text is mjqqt"

        ##HINT: How do you get the index of an item in a list:
        #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

        ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


    def decrypt(text, shift):
        new_letters=[]
        for letter in list(text):
            if letter in alphabet:
                alphabet_index = alphabet.index(letter)
                new_index = alphabet_index - shift
                new_letters.append(alphabet[new_index])
            else:
                new_letters.append(letter)
        return "".join(new_letters)

    #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
    print(ceasar(direction,text, shift))
    run_again = input("do you wanna try again? type 'yes' or 'no':")
    if run_again == 'no':
        running = False
        print("thank you for playing")
