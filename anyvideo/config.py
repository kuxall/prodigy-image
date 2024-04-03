import toml

values = toml.load("anyvideo/config.toml")

if __name__ == '__main__':
    print(values['anyvideo']['data_in'])
