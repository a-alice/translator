import smc_analyzer_sm
from string import digits
from string import ascii_letters
from smc_analyzer_sm import MainMap

class SMCAnalyzer:

    def __init__(self):
        self._fsm = smc_analyzer_sm.SMAnalyzer_sm(self)
        self.list_types = ['int', 'short', 'long']
        self.buffer = []
        self.is_correct = True

    def incTmp(self, p):
        self.buffer.append(p)

    def clearTmp(self):
        self.buffer.clear()

    def isValidRT(self):
        return (''.join(self.buffer) in self.list_types)

    def isValidFN(self):
        l = len(self.buffer)
        return (l < 17 and l > 0)

    def Unacceptable(self):
        self.is_correct = False

    def Acceptable(self):
        self.is_correct = True

    def check_str(self, str):
        # self._fsm.enterStartState()
        self._fsm.setState(MainMap.Start)
        for char in str:
            if char in ascii_letters:
                self._fsm.Symbol(char)
            elif char in digits:
                self._fsm.Digit(char)
            elif char == ' ':
                self._fsm.WhiteSpace()
            elif char == '(':
                self._fsm.SymbolOpen()
            elif char == ')':
                self._fsm.SymbolClose()
            elif char == ',':
                self._fsm.Comma()
            elif char == ';':
                self._fsm.SymbolFinish()
            else:
                self._fsm.Unknown()

        self._fsm.EOS()

        return self.is_correct





if __name__ == '__main__':
    t = SMCAnalyzer()
    print (t.check_str('long   StX0LEzY8ArWHe();'))