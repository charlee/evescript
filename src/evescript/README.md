EveScript
==========

This document provides some information about how the EveScript language itself is created.

## How to Build the Parser


The parser is written in [ANTLR](https://www.antlr.org/) and can be built with the following commands:

```
$ cd eveparser
$ make
```

The defualt make target will download ANTLR to `__antlr__`, then generate the lexer and parser
using the grammar definition `EveScript.g4`.


## Modify the Language

The full EBNF definition is listed in the [EBNF] section in this document.
Make any necessary changes and make sure the result EBNF sounds.

Then modify `EveScript.g4` based on the modified EBNF, and run `make` to rebuild the lexer and parser.


## EBNF


```bnf
<script> ::= { <statement> }

<statement> ::= "if" "(" <expr> ")" "{" { action } "}"

<expr>   ::= <term> "||" <expr>
          |  <term>

<term>   ::= <factor> "&&" <term>
          |  <factor>

<factor> ::= "(" <expr> ")
          | "!" <factor>
          | <predicate>

<predicate> ::= <operand> <operator> <operand>
             | <boolean>

<operator>  ::= ">"
             |  ">="
             |  "<"
             |  "<="
             |  "=="
             |  "!="
             |  keyword

<operand>   ::= variable
             |  <const>

<boolean>   ::= 'true'
             |  'false'

<const>     ::= string
             |  number
             |  <bool>


<action>   ::= keyword "(" <param> { "," <param> } ")"

<param>    ::= <const>
```


## Script Example

```
if ($currentTime matchCron "0 0 * * *" && $lightSensor > 20) {
    say("Hello, world!")
    play("music.mp3")
}
```
