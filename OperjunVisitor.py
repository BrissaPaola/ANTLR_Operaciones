# Generated from Operjun.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .OperjunParser import OperjunParser
else:
    from OperjunParser import OperjunParser

# This class defines a complete generic visitor for a parse tree produced by OperjunParser.

class OperjunVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by OperjunParser#prog.
    def visitProg(self, ctx:OperjunParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OperjunParser#IfStat.
    def visitIfStat(self, ctx:OperjunParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OperjunParser#PrintStat.
    def visitPrintStat(self, ctx:OperjunParser.PrintStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OperjunParser#ExprStat.
    def visitExprStat(self, ctx:OperjunParser.ExprStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OperjunParser#cond.
    def visitCond(self, ctx:OperjunParser.CondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OperjunParser#MulDiv.
    def visitMulDiv(self, ctx:OperjunParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OperjunParser#AddSub.
    def visitAddSub(self, ctx:OperjunParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OperjunParser#Parens.
    def visitParens(self, ctx:OperjunParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OperjunParser#Potencia.
    def visitPotencia(self, ctx:OperjunParser.PotenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by OperjunParser#Int.
    def visitInt(self, ctx:OperjunParser.IntContext):
        return self.visitChildren(ctx)



del OperjunParser