import importlib.metadata


def version():
    version = importlib.metadata.version('whoami_bot')
    print(f'whoami_bot version {version}')


def main():
    version()
