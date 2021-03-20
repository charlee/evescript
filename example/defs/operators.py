from croniter import croniter


def matchCron(t, cron):
    return croniter.match(cron, t)


OPERATORS = {
    'matchCron': matchCron,
}
