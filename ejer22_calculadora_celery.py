from celery import Celery

app = Celery('ejer22(calculadora_celery)', broker='redis://localhost:8888', backend='redis://localhost:8888',
        include=['ejer22(calculadora_celery)'])



@app.task
def suma(x, y):
    return x + y


@app.task
def resta(x, y):
    return x - y


@app.task
def mult(x, y):
    return x * y


@app.task
def div(x, y):
    return x / y


@app.task
def pot(x, y):
    return x ** y
