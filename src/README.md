EveScript
==========



## BNF


```bnf
<script> ::= { <trigger> }

<trigger> ::= "on" "(" <event> ")" "{" { condition } "}"

<event> ::= keyword

<condition> ::= "if" "(" <expr> ")" "{" { action } "}"

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
             | bool


<action>   ::= keyword "(" <param> { "," <param> } ")"

<param>    ::= <operand>
```


## Example

if ($currentTime matchCron "0 0 * * *" && $lightSensor > 20) {
    say("Hello, world!")
    play("music.mp3")
}
