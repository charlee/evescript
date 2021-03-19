def say(text):
    print(f'SAY: {text}')


def play(filename):
    print(f'PLAY: {filename}')


ACTIONS = {
    'say': say,
    'play': play,
}
