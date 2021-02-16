import json


class MorseCode:
    def __init__(self):
        # load morse dictionary into module
        with open("./morse_code.json", mode='r', encoding="utf-8") as f:
            self.morse_code = json.load(f)

    # convert input sentence to morse code sentence
    def encrypt(self, sentence: str) -> str:
        converted_sentence = ""
        if sentence.strip() == '':
            raise ValueError("Invalid sentence detected!")
        for letter in sentence.strip():
            if letter == " ":
                converted_sentence = converted_sentence + "/"
            else:
                detection_sentence = converted_sentence
                for morse in self.morse_code:
                    # add in morse code to object sentence
                    if letter.lower() == morse.lower():
                        converted_sentence = converted_sentence + self.morse_code[morse] + "_"
                # pickup fallout and alert
                if len(converted_sentence) == len(detection_sentence):
                    raise ValueError(f"Missing morse code: {letter}")
        return converted_sentence

    # revert morse code sentence
    def decrypt(self, converted_sentence: str) -> str:
        reverted_sentence = ""
        if converted_sentence.strip() == '':
            raise ValueError("Invalid sentence detected!")
        morse_words = converted_sentence.split("/")  # break words into list of words
        for morse_word in morse_words:
            morse_letters = morse_word.strip("_")  # clean letters with trailing _
            morse_letters = morse_letters.split("_")  # break word into letters
            for morse_letter in morse_letters:
                for morse in self.morse_code:
                    if morse_letter == self.morse_code[morse]:
                        reverted_sentence = reverted_sentence + morse
            reverted_sentence = reverted_sentence + " "
        return reverted_sentence.strip()

    # view morse code source
    def view_source(self):
        for morse in self.morse_code:
            print(f"{morse}: {self.morse_code[morse]}")
        return None


if __name__ == '__main__':  # launch as terminal
    my_morse = MorseCode()
    kernel_activate = True
    ascii_activation = """
                                 `. ___
                                __,' __`.                _..----....____
                    __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
              _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
            ,'________________                          \`-._`-','
             `._              ```````````------...___   '-.._'-:
                ```--.._      ,.                     ````--...__\-.
                        `.--. `-`                       ____    |  |`
                          `. `.                       ,'`````.  ;  ;`
                            `._`.        __________   `.      \\'__/`
                               `-:._____/______/___/____`.     \  `
                                           |       `._    `.    \\
                                           `._________`-.   `.   `.___
                                                              `------'`
            
        
         _   __                     _    ___       _   _            _           _ 
        | | / /                    | |  / _ \     | | (_)          | |         | |
        | |/ /  ___ _ __ _ __   ___| | / /_\ \ ___| |_ ___   ____ _| |_ ___  __| |
        |    \ / _ \ '__| '_ \ / _ \ | |  _  |/ __| __| \ \ / / _` | __/ _ \/ _` |
        | |\  \  __/ |  | | | |  __/ | | | | | (__| |_| |\ V / (_| | ||  __/ (_| |
        \_| \_/\___|_|  |_| |_|\___|_| \_| |_/\___|\__|_| \_/ \__,_|\__\___|\__,_|
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    """
    count = 0
    while kernel_activate:
        if count == 0:
            print(ascii_activation)
            print("Welcome to Morse Code Center!")
            print("Input 'help' to view available commands")
        command = input("Please input your command ~\n$").strip().lower()
        if command == "exit":
            print("See you next time!")
            kernel_activate = False
        elif command == "encrypt":
            my_sentence = input("Encrypting below to morse code ~\n$")
            print(my_morse.encrypt(my_sentence))
        elif command == "decrypt":
            my_morse_code = input("Decrypting below to text message ~\n$")
            print(my_morse.decrypt(my_morse_code))
        elif command == "view":
            my_morse.view_source()
        elif command == "help":
            print("""
exit:    Exit terminal
encrypt: Convert input text into morse code
decrypt: Convert input morse code into text
view:    View the corresponding text: morse code
                  """)
        else:
            print("You have entered invalid command, please try again.")
        count = 1
