from OperjunVisitor import OperjunVisitor


class EvalVisitor(OperjunVisitor):

    def visitProg(self, ctx):
        resultado = None
        for s in ctx.stat():
            resultado = self.visit(s)
        return resultado

    def visitIfStat(self, ctx):
        condicion = self.visit(ctx.cond())
        if condicion:
            return self.visit(ctx.stat(0))
        elif ctx.stat(1) is not None:
            return self.visit(ctx.stat(1))
        return None

    def visitPrintStat(self, ctx):
        valor = self.visit(ctx.expr())
        print(valor)
        return valor

    def visitExprStat(self, ctx):
        return self.visit(ctx.expr())

    def visitCond(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        op = ctx.op.text

        if op == '<':
            return izq < der
        elif op == '>':
            return izq > der
        elif op == '==':
            return izq == der
        elif op == '!=':
            return izq != der
        return False

    def visitMulDiv(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        if ctx.op.text == '*':
            return izq * der
        else:
            return int(izq / der) if der != 0 else 0

    def visitAddSub(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        if ctx.op.text == '+':
            return izq + der
        else:
            return izq - der

    def visitPotencia(self, ctx):
        izq = self.visit(ctx.expr(0))
        der = self.visit(ctx.expr(1))
        return izq**der

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitParens(self, ctx):
        return self.visit(ctx.expr())