import json
from compiler import EveScriptCompiler


script = '''

on (timer) {

    if ($currentTime matchCron "0 0 * * *" && $lightSensor > 20 || $lightSensor < 10) {
        say("Hello, world!")
        play("music.mp3", "ogg")
        play2("music.mp3")
    }

    if ($currentTime matchCron "1 0 * * *") {
        say("test")
    }

}


on(timer) {
}

'''

compiler = EveScriptCompiler()
ast = compiler.compile(script)
print(json.dumps(ast, indent=2))