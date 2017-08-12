from jinja2 import Environment, PackageLoader

def load_template():

    env = Environment(loader=PackageLoader('indanger', 'templates'),
                      lstrip_blocks=True,
                      trim_blocks=True)

    return env.get_template('indanger.html')

def get_page_info():
    return "fake"

def main():
    template = load_template()
    page_info = get_page_info()
    webpage = template.render()

    with open("indanger.html", "w") as f:
        f.write(webpage)



if __name__ == "__main__":
    main()
