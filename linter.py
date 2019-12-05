class Linter:
    def __init__(self):
        self.stack = []
        self.opening_brace = {')': '(', ']': '[', '}': '{'}
        
    def lint(self, text):
        for i in range(len(text)):
            if text[i] in ['(', '[', '{']:
                self.stack.append(text[i])
            elif text[i] in [')', ']', '}']:
                if self.stack[-1] == self.opening_brace[text[i]]:
                    self.stack.pop()
                else:
                    print("Error: incorrect closing brace '{0}' at index {1}".format(text[i], i))
        if self.stack != []:
            print("Error: opening brace '{0}' does not have a closing brace".format(self.stack[-1]))
                
if __name__ == '__main__':
    linter = Linter()
    linter.lint('(var x = { y: [1, 2, 3,]} )')