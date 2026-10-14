grammar Operjun;

prog: stat+ EOF ;

stat: 'if' cond stat ('else' stat)?   # IfStat
    | 'imprime' expr                  # PrintStat
    | expr                            # ExprStat
    ;

cond: expr op=('<'|'>'|'=='|'!=') expr ;

expr: expr op=('*'|'/') expr          # MulDiv
    | expr op=('+'|'-') expr          # AddSub
    | <assoc=right> expr '^' expr     # Potencia
    | INT                             # Int
    | '(' expr ')'                    # Parens
    ;

INT : [0-9]+ ;
WS  : [ \t\r\n]+ -> skip ;