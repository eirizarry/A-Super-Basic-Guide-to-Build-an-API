#!flask/bin/python
from flask import Flask, request, jsonify #We import these to work in a webframe, use the GET method, and display our results in json.

app = Flask(__name__) #The first argument, which creates an instance of the Flask class. It is the name of the application's module. For a single module, use '__name__'.

@app.route('/api/v1/tasks') #This is the app decorator which tells Flask what URL should trigger the function.
def get_tasks(): #Here, the function is named and generates URLs, returning the message we want to display in the user's browser.
    operation = request.args.get('operation') #This lets the user set the parameters of the URL by choosing a mathematical operation and the two numbers he wants to manipulate.
    numberOne= request.args.get('numberOne')
    numberTwo = request.args.get('numberTwo')
    convertedNumberOne = int(numberOne) #We created these values because the URL parameter is stored as a String. If we want to do any mathematical calculations, we cannot do it in words--it must be numbers. We must convert the string into a number value by using int().
    convertedNumberTwo = int(numberTwo)
    if (operation == 'multiply'): #Conditional statements, which perform binary operations based on user input.
        result = (convertedNumberOne * convertedNumberTwo)

    elif (operation == 'divide'):
        result = (convertedNumberOne / convertedNumberTwo)

    elif (operation == 'subtract'):
        result = (convertedNumberOne - convertedNumberTwo)

    elif (operation == 'add'):
        result = (convertedNumberOne + convertedNumberTwo)

    else: #Displays if user input does not meet other conditions.
        result = 'not a valid operation'

    tasks = [ #Results are displayed in json; key = value. For example, 'Operation': is the key name, given the value of operation, which was defined earlier.
        {
            'Operation': operation,
            'number one': numberOne,
            'number two': numberTwo,
            'result': result
        }
    ]
    return jsonify({'Calculation': tasks}) #User will see 'Calculation', followed by the json set for tasks.

if __name__ == '__main__': #Python assigns the name "__main__" to the script when it is executed. Therefore, __name__ is equal to "__main__". If this condition is satfisfied, the app.run() method will be executed.
    app.run(debug=True) #Use debug and set the parameter to True. If there is an error, the web page will print out possible Python errors by helping us trace it.
