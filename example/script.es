if ($currentTime matchCron "0 0 * * *" && $lightSensor > 20 || $lightSensor < 10) {
    say("Only run on midnight 00:00")
    play("music.mp3")
}

# another condition
if ($currentTime matchCron "* * * * *") {
    say("run every minute")
    say(true)
}

if (true) {
    say("Always true")
}

if (false) {
    say("This action should never run!")
}

# Nested statements
if (true) {
    if (true) {
        say("true & true")
    }

    if (false) {
        say("true & false")
    }
}

# if else statement
if ($lightSensor > 50) {
    say("Too bright!")
    say("Too bright!")
} else if ($lightSensor > 30) {
    say("Good lighting")
} else
    say("Too dark!")

# Or run actions directly
say("Run action directly")