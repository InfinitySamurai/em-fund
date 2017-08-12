from jinja2 import Environment, PackageLoader

def load_template():

    env = Environment(loader=PackageLoader('indanger', 'templates'),
                      lstrip_blocks=True,
                      trim_blocks=True)

    return env.get_template('indanger.html')

def main():
    template = load_template()
    webpage = template.render()

    with open("indanger.html", "w") as f:
        f.write(webpage)



if __name__ == "__main__":
    main()
