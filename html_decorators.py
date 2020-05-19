def div(func):
    def wrapper(*args, **kwargs):
        return "<div>{} </div>".format(func(*args, **kwargs))

    return wrapper

def article(func):
    def wrapper(*args, **kwargs):
        return "<article>{} </article>".format(func(*args, **kwargs))

    return wrapper


def p(func):
    def wrapper(*args, **kwargs):
        return "<p>{}</p>".format(func(*args, **kwargs))

    return wrapper

# Here you must apply the decorators, uncomment this later

#@article
#@p
@ div
def saludo(nombre):
    return f'¡Hola {nombre}, ¿Cómo estás?'


def run():
    print(saludo('Jorge'))


if __name__ == '__main__':
    run()

# We want to have three different outputs 👇🏼

# <div>¡Hola Jorge, ¿Cómo estás?'</div>
# <article>¡Hola Jorge, ¿Cómo estás?'</article>
# <p>¡Hola Jorge, ¿Cómo estás?'</p>
