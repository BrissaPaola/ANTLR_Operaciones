from antlr4 import InputStream, CommonTokenStream
from OperjunLexer import OperjunLexer
from OperjunParser import OperjunParser
from EvalVisitor import EvalVisitor


def ejecutar(codigo):
    lexer = OperjunLexer(InputStream(codigo))
    tokens = CommonTokenStream(lexer)
    parser = OperjunParser(tokens)
    tree = parser.prog()
    EvalVisitor().visit(tree)


if __name__ == "__main__":
    print("--- Probando Operjun.g4 (Aritmética, Potencias e If/Else) ---")

    print("\nCaso 1: Operaciones combinadas y potencia")
    ejecutar("imprime 2 + 3 * 2 ^ 2")  # Debe imprimir 14

    print("\nCaso 2: Condicional If verdadero con impresión")
    ejecutar("""
    if 5 < 10
        imprime 100
    else
        imprime 200
    """)  # Debe imprimir 100

    print("\nCaso 3: Condicional If falso (ejecuta el else)")
    ejecutar("""
    if 20 == 10
        imprime 50
    else
        imprime 99
    """)  # Debe imprimir 99