from marzo.marzoListener import marzoListener
from marzo.marzoParser import marzoParser

class GenCode(marzoListener):

    def __init__(self):
        self.var = 0
        self.queue = []
        self.stack = []
    
    def enterProgram(self, ctx:marzoParser.ProgramContext):
        print(".text")

    def exitNumero(self, ctx: marzoParser.NumeroContext):
        self.var+=1
        self.queue.append(self.var)
        self.stack.append(self.var)
        print("li $v" + str(self.var) + ", " + ctx.Numero().getText())
    
    def exitLetra(self, ctx: marzoParser.LetraContext):
        self.var+=1
        self.queue.append(self.var)
        self.stack.append(self.var)
        print("lw $v" + str(self.var) + ", " + ctx.Letra().getText())

    def exitSuma(self, ctx:marzoParser.SumaContext):
        print("ADD $v" + str((self.var)) +", " + "$v" + str(self.stack.pop()) + ", " + "$v" + str(self.stack.pop()))

    def exitResta(self, ctx: marzoParser.RestaContext):
        print("REST $v" + str((self.var)) +", " + "$v" + str(self.stack.pop()) + ", " + "$v" + str(self.stack.pop()))

    def exitMultiplicacion(self, ctx: marzoParser.MultiplicacionContext):
        print("MULT $v" + str((self.var)) +", " + "$v" + str(self.stack.pop()) + ", " + "$v" + str(self.stack.pop()))

    def exitDivision(self, ctx: marzoParser.DivisionContext):
        print("DIV $v" + str((self.var)) +", " + "$v" + str(self.stack.pop()) + ", " + "$v" + str(self.stack.pop()))
    
    def exitAsignacion(self, ctx:marzoParser.AsignacionContext):
        print("li $v" + str((self.var)) +", " + "$v" + str(self.stack.pop()) + ", " + "$v" + str(self.stack.pop()))

    def exitDeclaracion(self, ctx:marzoParser.DeclaracionContext):
        self.var+=1
        self.queue.append(self.var)
        self.stack.append(self.var)
        print("sw $v" + str(self.var) + ", " + ctx.Letra().getText())

    def exitMayor(self, ctx:marzoParser.MayorContext):
        print("stgreater $v" + str((self.var)) +", " + "$v" + str(self.stack.pop(1)) + ", " + "$v" + str(self.stack.pop()))

    def exitMenor(self, ctx:marzoParser.MenorContext):
        print("sllower $v" + str((self.var)) +", " + "$v" + str(self.stack.pop(1)) + ", " + "$v" + str(self.stack.pop()))
    
    def exitPrint(self, ctx:marzoParser.PrintContext):
        print("syscall")
        print("______")

    def exitIf(self, ctx:marzoParser.IfContext):
        print("bequals $v" + str(self.queue.pop(0)) +", $v" + str(self.queue.pop(0)) + ", ELSE")

    def exitIfnoelse(self, ctx: marzoParser.IfnoelseContext):
        print("bequals $v" + str(self.queue.pop(0)) +", $v" + str(self.queue.pop(0)))
    
    def exitEndStatement(self, ctx: marzoParser.EndStatementContext):
        print("-----------------------------------------")
    

