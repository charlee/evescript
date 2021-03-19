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
    | 'true'
    | 'false'
    ;

action: KEYWORD '(' param (',' param)* ')'
    ;

param: operand
    ;

KEYWORD: [a-zA-Z_][a-zA-Z_0-9]* ;

STRING :  '"' (ESC | ~["\\])* '"' ;
VARIABLE: '$' KEYWORD ;
NUMBER
    :   '-'? INT '.' INT        // 1.35, 0.3, -4.5
    |   '-'? INT                // -3, 45
    ;

fragment ESC :   '\\' (["\\/bfnrt] | UNICODE) ;
fragment UNICODE : 'u' HEX HEX HEX HEX ;
fragment HEX : [0-9a-fA-F] ;

fragment INT :   '0' | '1'..'9' '0'..'9'* ; // no leading zeros
WS  :   [ \t\n\r]+ -> skip ;
