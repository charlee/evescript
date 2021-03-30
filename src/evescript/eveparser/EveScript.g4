grammar EveScript;

script: statement*
    ;

block: '{' statement* '}'
    | statement
    ;

statement: if_statement
    | action
    ;

if_statement: 'if' '(' expr ')' block ( 'else' block )?
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
    | boolean
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

boolean: 'true'
    | 'false'
    ;

const: STRING
    | NUMBER
    | boolean
    ;

action: KEYWORD '(' params ')'
    ;

params: param (',' param)*
    |
    ;

param: const
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

// skip all line comments
COMMENT: '#' ~[\r\n]* -> skip ;

// skip whitespaces
WS  :   [ \t\n\r]+ -> skip ;

