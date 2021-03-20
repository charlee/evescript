if ($currentTime matchCron "0 0 * * *" && $lightSensor > 20 || $lightSensor < 10) {
    say("Only run on midnight 00:00")
    play("music.mp3")
}

# another condition
if ($currentTime matchCron "* * * * *") {
    say("run every minute")
    say(true)
}