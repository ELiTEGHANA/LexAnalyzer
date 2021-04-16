import re
class LexicalAnalyzer:
    line_num = 1

    def tokinizer(self, code):
        rules = [
            ('NUMBER', r'num'),
            ('OUTPUT', r'output'),
            ('READ', r'read'),
            ('STRING', r'str'),
            ('CHARACTER', r'char'),
            ('ADDITION', r'\+'),
            ('SUBTRACTION', r'-'),
            ('DIVISION', r'\/'),
            ('MULTIPLICATION', r'\*'),
            ('LESS_THAN', r'<'),
            ('GREATER_THAN', r'>'),
            ('OR', r'\|'),
            ('AND', r'\|\|'),
            ('EQUAL', r'=='),
            ('MODULO', r'%'),
            ('INTEGER_CONSTANT', r'\d(\d)*'),
            ('FLOAT_CONSTANT', r'\d(\d)*\.\d(\d)*'),
            ('IDENTIFIERS', r'[a-zA-Z]\w*'),
            # ('STRING', r'[a-zA-Z]\w*'),
            ('LEFT_BRACKET', r'\('),
            ('RIGHT_BRACKET', r'\)'),
            ('NEWLINE', r'\n'),
            ('COMMA', r','),
            ('SEMI_COL', r';'),
            ('QUOTATION', r'\"'),
        ]
        token_join = '|'.join('(?P<%s>%s)' % x for x in rules)
        line_start = 0

        token = []
        lexeme = []
        row = []
        column = []

        for m in re.finditer(token_join, code):
            token_type = m.lastgroup
            token_lexeme = m.group(token_type)

            if token_type == 'NEWLINE':
                line_start = m.end()
                self.line_num += 1

            else:
                col = m.start() - line_start
                column.append(col)
                token.append(token_type)
                lexeme.append(token_lexeme)
                row.append(self.line_num)

                print('Token = {0}, Lexeme = \'{1}\', Row = {2}, Column = {3}'.format(token_type, token_lexeme, self.line_num, col))

        return token,lexeme,row,column








