from marzo.marzoListener import marzoListener
from marzo.marzoParser import marzoParser

class GenCode(marzoListener):

    def __init__(self):
        self.x = 0
        self.list = []
        self.list2 = []
    
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        print("     .text")
        print("main:")

    def exitNumero(self, ctx: marzoParser.NumeroContext):
        self.x+=1
        self.list.append(self.x)
        self.list2.append(self.x)
        print("li $v" + str(self.x) + ", " + ctx.Numero().getText())
    
    def exitLetra(self, ctx: marzoParser.LetraContext):
        self.x+=1
        self.list.append(self.x)
        self.list2.append(self.x)
        print("lw $v" + str(self.x) + ", " + ctx.Letra().getText())

    def exitSuma(self, ctx:marzoParser.SumaContext):
        print("ADD $v" + str((self.x)) +", " + "$v" + str(self.list2.pop()) + ", " + "$v" + str(self.list2.pop()))
        self.list.append(self.x)
        self.list2.append(self.x)

    def exitResta(self, ctx: marzoParser.RestaContext):
        print("REST $v" + str((self.x)) +", " + "$v" + str(self.list2.pop()) + ", " + "$v" + str(self.list2.pop()))
        self.list.append(self.x)
        self.list2.append(self.x)

    def exitMultiplicacion(self, ctx: marzoParser.MultiplicacionContext):
        print("MULT $v" + str((self.x)) +", " + "$v" + str(self.list2.pop()) + ", " + "$v" + str(self.list2.pop()))
        

    def exitDivision(self, ctx: marzoParser.DivisionContext):
        print("DIV $v" + str((self.x)) +", " + "$v" + str(self.list2.pop()) + ", " + "$v" + str(self.list2.pop()))
    
    #def exitAsignacion(self, ctx:marzoParser.AsignacionContext):
        #print("li $v" + str((self.x)) +", " + "$v" + str(self.list2.pop()) + ", " + "$v" + str(self.list2.pop()))

    def exitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        self.x+=1
        self.list.append(self.x)
        self.list2.append(self.x)
        print("sw $v" + str(self.x) + ", " + ctx.Letra().getText())

    def exitMayor(self, ctx:marzoParser.MayorContext):
        print("stgreater $v" + str((self.x)) +", " + "$v" + str(self.list2.pop(1)) + ", " + "$v" + str(self.list2.pop()))

    def exitMenor(self, ctx:marzoParser.MenorContext):
        print("sllower $v" + str((self.x)) +", " + "$v" + str(self.list2.pop(1)) + ", " + "$v" + str(self.list2.pop()))
    
    def exitPrint(self, ctx:marzoParser.PrintContext):
        print("syscall")
        print("______")

    def exitIf(self, ctx:marzoParser.IfContext):
        print("bequals $v" + str(self.list.pop(0)) +", $v" + str(self.list.pop(0)) + ", .main")

    def exitIfnoelse(self, ctx: marzoParser.IfnoelseContext):
        print("bequals $v" + str(self.list.pop(0)) +", $v" + str(self.list.pop(0)))
    
    def exitEndStatement(self, ctx: marzoParser.EndStatementContext):
        print("-----------------------------------------")

    def exitIfexpression(self, ctx: marzoParser.IfexpressionContext):
        print("bequals $v" + str(self.list.pop(0)) +", $v" + str(self.list.pop(0)) + ", .main")
    
    def exitIfnoelseExp(self, ctx: marzoParser.IfnoelseExpContext):
        print("bequals $v" + str(self.list.pop(0)) +", $v" + str(self.list.pop(0)))
    

