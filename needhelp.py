
from jinja2 import Environment, PackageLoader

def load_template():

    env = Environment(loader=PackageLoader('needhelp', 'templates'),
                      lstrip_blocks=True,
                      trim_blocks=True)

    return env.get_template('needhelp.html')


def main(user_data):
    template = load_template()
    accounts = ["long life saver", "working", "utilities", "personal"]
    template_data = {"accounts": accounts}
    webpage = template.render(template_data)

    with open("needhelp.html", "w") as f:
        f.write(webpage)



if __name__ == "__main__":
    main("dud")
    
