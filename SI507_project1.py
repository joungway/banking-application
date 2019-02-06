# Import statements necessary
from lab3_code import *
from flask import Flask

# Set up application
app = Flask(__name__)

# Routes

@app.route('/')
def home(): # Route function names can be anything unique
    return 'Welcome to the banking application!' # Route functions can return plain old text, or text in correctly formatted HTML (or the return values of many special functions we haven't looked at yet)

# Something else to note is that the functions don't get INVOKED the way you may be used to. Running the application and *going to a URL that matches the path in the @app.route() business IS what runs that function!

#@app.route('/bank/<name>')
@app.route('/bank/<name>')
def welcome_bank(name):
    # Note how the word in < > carats / angle-brackets is the SAME as the input to the function - that means the URL is what sends the input along
    ins_bank=Bank(name, Yuan, 0)
    return 'Welcom to {}!'.format(ins_bank.name)

@app.route('/dollar/<value>')
def showdollar(value): # Check this out -- what's going on here? A useful pattern to think about.
    ins_dollar=Dollar(int(value))
    #Dollar(int(amt))
    return "{} {}".format(ins_dollar.value,"Dollar" + "s" * (ins_dollar.value > 1))

@app.route('/yuan/<value>')
def showyuan(value): # Check this out -- what's going on here? A useful pattern to think about.
    ins_yuan=Yuan(int(value))
    return "{} Yuan".format(ins_yuan.value)

@app.route('/pound/<value>')
def showpound(value): # Check this out -- what's going on here? A useful pattern to think about.
    ins_pound=Pound(int(value))
    return "{} {}".format(ins_pound.value,"Pound" + "s" * (ins_pound.value > 1))

@app.route('/bank/<name>/<currency>/<value>')
def message(name, currency, value):
    if currency =="dollar":
        ins_message=Bank(name,currency,int(value))
        return 'Welcome to the {} bank! {}'.format(ins_message.name,ins_message.__str__())
    elif currency == "pound":
        ins_information =  Bank(name, currency, int(value))
        return 'Welcome to the {} bank! {}'.format(ins_information.name, ins_information.__str__())
    elif currency == "yuan":
        ins_information = Bank(name, currency, int(value))
        return 'Welcome to the {} bank! {}'.format(ins_information.name, ins_information.__str__())


if __name__ == '__main__':
    app.run()
