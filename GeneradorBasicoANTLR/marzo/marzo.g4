grammar marzo;

program : expression* | statement* | expression*statement*;
expression: 
    expression '+' expression #suma
    | Numero                #numero
    | expression '=' expression #asignacion
    | Letra                 #letra
    | expression '<' expression #menor
    | expression '>' expression #mayor
    | expression '-' expression #resta
    | expression '/' expression #division
    | expression '*' expression #multiplicacion
    ;

statement:
    'if (' expression ') do this' statement #ifnoelse
    | 'if (' expression ') do this' expression #ifnoelseExp
    | 'if (' expression ') do this' statement 'else do this' statement #if
    | 'if (' expression ') do this' statement 'else do this' expression #ifexpression
    | 'int' Letra  #declaracion
    | 'print(' expression ')' #print
    | statement '//'        #endStatement
    | 'int' expression #asignacionExp
    ;

Numero : [0-9]+;

Letra: [a-zA-Z];

WS : [ \t\n\r]+ -> skip ;