def say(text):
    print(f'SAY: {text}')


def play(filename):
    print(f'PLAY: {filename}')


def test():
    print('test')
    pass


ACTIONS = {
    'say': say,
    'play': play,
    'test': test,
}
