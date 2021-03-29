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

# Or run actions directly
say("Run action directly")