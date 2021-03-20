EveScript
==========



## BNF


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

<operator>  ::= ">"
             |  ">="
             |  "<"
             |  "<="
             |  "=="
             |  "!="
             |  keyword

<operand>   ::= variable
             |  <const>

<const>     ::= string
             |  number
             |  bool


<action>   ::= keyword "(" <param> { "," <param> } ")"

<param>    ::= <const>
```


## Example

on (timer) {
    if ($currentTime matchCron "0 0 * * *" && $lightSensor > 20) {
        say("Hello, world!")
        play("music.mp3")
    }
}