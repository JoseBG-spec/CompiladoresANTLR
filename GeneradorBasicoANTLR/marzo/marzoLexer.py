# Generated from f:\pepot\Documents\8vo Semestre\GeneradorANTLR\CompiladoresANTLR\GeneradorBasicoANTLR\marzo\marzo.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("m\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\17\3\17\3\17\3\20\6\20a\n\20\r\20\16\20b")
        buf.write("\3\21\3\21\3\22\6\22h\n\22\r\22\16\22i\3\22\3\22\2\2\23")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23\3\2\5\3\2\62;\4\2C\\c|\5")
        buf.write("\2\13\f\17\17\"\"\2n\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2")
        buf.write("\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2")
        buf.write("\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31")
        buf.write("\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2")
        buf.write("\2\2\2#\3\2\2\2\3%\3\2\2\2\5\'\3\2\2\2\7)\3\2\2\2\t+\3")
        buf.write("\2\2\2\13-\3\2\2\2\r/\3\2\2\2\17\61\3\2\2\2\21\63\3\2")
        buf.write("\2\2\238\3\2\2\2\25B\3\2\2\2\27O\3\2\2\2\31S\3\2\2\2\33")
        buf.write("Z\3\2\2\2\35\\\3\2\2\2\37`\3\2\2\2!d\3\2\2\2#g\3\2\2\2")
        buf.write("%&\7-\2\2&\4\3\2\2\2\'(\7?\2\2(\6\3\2\2\2)*\7>\2\2*\b")
        buf.write("\3\2\2\2+,\7@\2\2,\n\3\2\2\2-.\7/\2\2.\f\3\2\2\2/\60\7")
        buf.write("\61\2\2\60\16\3\2\2\2\61\62\7,\2\2\62\20\3\2\2\2\63\64")
        buf.write("\7k\2\2\64\65\7h\2\2\65\66\7\"\2\2\66\67\7*\2\2\67\22")
        buf.write("\3\2\2\289\7+\2\29:\7\"\2\2:;\7f\2\2;<\7q\2\2<=\7\"\2")
        buf.write("\2=>\7v\2\2>?\7j\2\2?@\7k\2\2@A\7u\2\2A\24\3\2\2\2BC\7")
        buf.write("g\2\2CD\7n\2\2DE\7u\2\2EF\7g\2\2FG\7\"\2\2GH\7f\2\2HI")
        buf.write("\7q\2\2IJ\7\"\2\2JK\7v\2\2KL\7j\2\2LM\7k\2\2MN\7u\2\2")
        buf.write("N\26\3\2\2\2OP\7k\2\2PQ\7p\2\2QR\7v\2\2R\30\3\2\2\2ST")
        buf.write("\7r\2\2TU\7t\2\2UV\7k\2\2VW\7p\2\2WX\7v\2\2XY\7*\2\2Y")
        buf.write("\32\3\2\2\2Z[\7+\2\2[\34\3\2\2\2\\]\7\61\2\2]^\7\61\2")
        buf.write("\2^\36\3\2\2\2_a\t\2\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2")
        buf.write("bc\3\2\2\2c \3\2\2\2de\t\3\2\2e\"\3\2\2\2fh\t\4\2\2gf")
        buf.write("\3\2\2\2hi\3\2\2\2ig\3\2\2\2ij\3\2\2\2jk\3\2\2\2kl\b\22")
        buf.write("\2\2l$\3\2\2\2\5\2bi\3\b\2\2")
        return buf.getvalue()


class marzoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    Numero = 15
    Letra = 16
    WS = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'='", "'<'", "'>'", "'-'", "'/'", "'*'", "'if ('", "') do this'", 
            "'else do this'", "'int'", "'print('", "')'", "'//'" ]

    symbolicNames = [ "<INVALID>",
            "Numero", "Letra", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "Numero", "Letra", "WS" ]

    grammarFileName = "marzo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


