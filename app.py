from flask import Flask, request, flash, session, render_template
from forex_python.converter import CurrencyCodes, CurrencyRates

app = Flask(__name__)
# we will start a venv (python3 -m venv venv)
# we need to install the libraries (pip3 install [lib])

# we will need to handle a route when submitting the amount 
# write a python code to get the currency



@app.route('/')
def homepage():

    return render_template("index.html")

@app.route('/convert')
def convert_from_currency():
    """get the Currency from and make sure it's Correct."""
    c = CurrencyRates()
    c.get_rates("")
    # we need to get the value of the user's input on what they are converting from
    from_curr = request.args["from-currency"]
    # and now where they are going to in which we will also make sure the correct code is used.
    to_curr = request.args["to-currency"]
    amount = float(request.args["amount"])
    results = c.convert(from_curr, to_curr, amount)
    # make a condintional to confirm the proper codes are use, so there shouldnt be any Numbers at from_currency
    # if from_curr.isnumeric() == True:
    #     flash("Please use a proper Currency code")
    #trying to make sure the code will actually match the list of currency codes and we will convert them to uppercase so they will match
    # elif from_curr.upper() != CurrencyCodes():
    #     flash("Incorrect Currency code")
    # need to find something to place here that allows the user to continue once the right currency code was inserted
    # else:
    #     text = text.replace("from-currency")



    return render_template("results.html", results=results)

def convert_to_currency():
    """Get the currency to and make sure its correct."""
    c = CurrencyRates()
    c.get_rates("")
    to_curr = request.args["to-currency"]
        # setting the right conditions on the other currency code
    if to_curr.isnumeric() == True:
        flash("Please use proper Currency Code")
    elif to_curr.upper() != CurrencyCodes():
        flash("Incorrect Currency code")
    else:
         text = text.replace("to-currency")

    return text("to-currency", text = text)

def convert_currencies():
    """complete the conversion from and to"""
    # so we want to take the the two currencies(from and to) and the amount to get the converted amount

    currency = CurrencyRates()
    Currency_Codes = CurrencyCodes()

    amount = request.args("amount")

    from_curr = convert_from_currency().upper()
    to_curr = convert_to_currency().upper()

    c = CurrencyRates()
    c.get_rates("")
    result = currency.convert(from_curr, to_curr, amount)

    return result(result = result) 
# i still need to finish with the proper test unit, I need to "refractor" the code so make a class on a seperate python file (i assume) and find out how to get it to work. Defnetly need to better manage the lessons so that I am not struggling as much as I am. What would be the proper first steps? How do I see the progress of the code so that im not trying giberish and assume it would work. Is my logic even in the right place?