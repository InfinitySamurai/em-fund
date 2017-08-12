
from jinja2 import Environment, PackageLoader

def load_template():

    env = Environment(loader=PackageLoader('friendindanger', 'templates'),
                      lstrip_blocks=True,
                      trim_blocks=True)

    return env.get_template('friendindanger.html')



if __name__ == "__main__":
    template = load_template()
