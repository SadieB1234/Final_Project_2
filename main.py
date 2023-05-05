import random
import game_gui
def read(file):
    word_bank = []
    with open(file,'r') as file:
        for line in file:
            word_bank.append(file.readline())
            word_bank = [i.strip() for i in word_bank]

    return word_bank

def main():
    file = 'words'
    word_bank = read(file)
    word = word_bank[random.randint(0,len(word_bank))]
    game_gui.game(word)

if __name__ == '__main__':
    main()