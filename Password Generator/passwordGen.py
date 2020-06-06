import string
import random

class Characters:
    def __init__(self, symbols, num):
        self.symbols = symbols
        self.numbers = num

    def capital_letters(self):
        capitals = list(string.ascii_uppercase)
        return capitals

    def small_letters(self):
        smalls = list(string.ascii_lowercase)
        return smalls

    def _numbers(self):
        numbers = self.numbers.split(" ")
        return numbers

    def _symbols(self):
        symbols = self.symbols
        return symbols.split(" ")


class Password:
    def generating_password(self):
        num = "0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5"
        symbols = "! @ # $ % ^ & * ( ) _ + - = [ { | \ ; ' / . , : ' } ] ~ ` `"
        ch = Characters(symbols, num)
        capitals = ch.capital_letters()
        smalls = ch.small_letters()
        nums = ch._numbers()
        symbols = ch._symbols()
        characters = [capitals, smalls, nums, symbols]
        password = ""
        len = int(input("Enter the length of password"))
        for length in range(0, len):
            index1 = int(random.uniform(0, 4))
            index2 = int(random.uniform(0, 26))
            character = characters[index1][index2]
            password += str(character)
        return password

def main():
    ps = Password()
    passW = ps.generating_password()
    return passW
