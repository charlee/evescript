grammar EveScript;

script: trigger*
    ;

trigger: 'on' '(' event ')' '{' condition* '}'
    ;

event: KEYWORD
    ;

condition: 'if' '(' expr ')' '{' action* '}'
    ;

expr: term '||' expr
    | term
    ;

term: factor '&&' term
    | factor
    ;

factor: '(' expr ')'
    | '!' factor
    | predicate
    ;

predicate: operand operator operand
    ;

operator: '>'
    | '>='
    | '<'
    | '<='
    | '=='
    | '!='
    | KEYWORD
    ;

operand: VARIABLE
    | const
    ;

const: STRING
    | NUMBER
    | BOOL
    ;

action: KEYWORD '(' param (',' param)* ')'
    ;

param: operand
    ;

KEYWORD: [a-zA-Z_][a-zA-Z_0-9]* ;

STRING :  '"' (ESC | ~["\\])* '"' ;
VARIABLE: '$' KEYWORD ;
NUMBER
    :   '-'? INT '.' INT EXP?   // 1.35, 1.35E-9, 0.3, -4.5
    |   '-'? INT EXP            // 1e10 -3e4
    |   '-'? INT                // -3, 45
    ;
BOOL: 'true'
    | 'false'
    ;

fragment ESC :   '\\' (["\\/bfnrt] | UNICODE) ;
fragment UNICODE : 'u' HEX HEX HEX HEX ;
fragment HEX : [0-9a-fA-F] ;

fragment INT :   '0' | '1'..'9' '0'..'9'* ; // no leading zeros
fragment EXP :   [Ee] [+\-]? INT ; // \- since - means "range" inside [...]
WS  :   [ \t\n\r]+ -> skip ;
