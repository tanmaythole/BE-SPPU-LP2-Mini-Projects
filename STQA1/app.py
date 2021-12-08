from flask import Flask, render_template, request

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'defaultkey'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        loanType = request.form['loanType']
        amount = request.form['amount']
        tenure = request.form['tenure']
        if loanType=="emi":
            intrestRate = request.form['interestRate']
            emi = calculate_emi(amount, intrestRate, tenure)
            return render_template('index.html', status="result", amount=emi, loanType=loanType)

        elif loanType=="fixedDeposit":
            intrestRate = request.form['interestRate']
            maturityValue = calculate_fd(amount, intrestRate, tenure)
            return render_template('index.html', status="result", amount=maturityValue, loanType=loanType)
            # return

    return render_template('index.html')



# calculate emi
def calculate_emi(principal, rate, time):
    principal = int(principal)
    rate = float(rate)
    time = int(time)

    rate = rate / (12 * 100) # one month interest
    time = time * 12 # one month period
    emi = (principal * rate * ((1+rate) ** time)) / ((1+rate) ** time - 1)
    
    emi = round(emi, 2)
    return emi



# calculate fd
def calculate_fd(principal, rate, time):
    principal = int(principal)
    rate = float(rate)
    time = int(time)
    
    maturityValue = principal * ((1 + rate/100) ** time)
    maturityValue = round(maturityValue, 2)
    return maturityValue


if __name__ == '__main__':
    app.run(debug=True)