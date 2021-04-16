# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from Buffer import Buffer
from LexicalAnalyzer import LexicalAnalyzer



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Buffer = Buffer()
    Lexical = LexicalAnalyzer()
    token = []
    lexeme = []
    row = []
    column = []

    for i in Buffer.load_buffer():
        t, lex, line, col = Lexical.tokinizer(i)
        token += t
        lexeme += lex
        row += line
        column += col

    print('\nRecognized Tokens: ', token)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
