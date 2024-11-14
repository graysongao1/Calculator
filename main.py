import tkinter as tk

calculation = ''

def add_to_calculation(symbol):
    #makes the variable accessible outside of the function + makes it a string
    global calculation
    calculation += str(symbol)

    #deletes all content in text_result field + inserts the calculation (1.0 is where we insert/delete the string)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)

#Note - we cannot use eval() because it ALSO evaluates python code, so theoretically someone can inject code into your program
def evaluate_calculation(): 
    global calculation
    #try and except - if there is an error (division by 0), code goes into except. Otherwise, it just runs try
    try:
        #evaluates calcuation, clears the current text, and inserts caluclation
        calculation = str(eval(calculation))
        text_result.delete(1.0, 'end')
        text_result.insert(1.0, calculation)
    except:
        #clears the text and inserts Error
        clear_field()
        text_result.insert(1.0, 'Error')

def clear_field():
    global calculation
    calculation = ''
    text_result.delete(1.0, 'end')

#tk.Tk() - opens tkinter interface
root = tk.Tk()

#window size
root.geometry = ('300x275')

#creating a user text input that spans all 5 columns of the 5x5 grid that .grid() makes
text_result = tk.Text(root, height=2, width=16, font=('Arial', 24))
text_result.grid(columnspan=5)

#NUMBERS

#creates a button that types 1 when it is pressed.
#The lambda function is needed here to make sure add_to_calc only runs when the button is pressed.
btn_1 = tk.Button(root, text='1', command=lambda: add_to_calculation(1), width=5, font=('Arial', 14))

#inserts the 1 button on the 2nd row and 1st column (first row is for the text)
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text='2', command=lambda: add_to_calculation(2), width=5, font=('Arial', 14)) 
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text='3', command=lambda: add_to_calculation(3), width=5, font=('Arial', 14)) 
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text='4', command=lambda: add_to_calculation(4), width=5, font=('Arial', 14)) 
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text='5', command=lambda: add_to_calculation(5), width=5, font=('Arial', 14)) 
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text='6', command=lambda: add_to_calculation(6), width=5, font=('Arial', 14)) 
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text='7', command=lambda: add_to_calculation(7), width=5, font=('Arial', 14)) 
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text='8', command=lambda: add_to_calculation(8), width=5, font=('Arial', 14)) 
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text='9', command=lambda: add_to_calculation(9), width=5, font=('Arial', 14)) 
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text='0', command=lambda: add_to_calculation(0), width=5, font=('Arial', 14)) 
btn_0.grid(row=5, column=2)

#FUNCTIONS

btn_plus = tk.Button(root, text='+', command=lambda: add_to_calculation('+'), width=5, font=('Arial', 14)) 
btn_plus.grid(row=2, column=4)

btn_minus = tk.Button(root, text='-', command=lambda: add_to_calculation('-'), width=5, font=('Arial', 14)) 
btn_minus.grid(row=3, column=4)

btn_times = tk.Button(root, text='*', command=lambda: add_to_calculation('*'), width=5, font=('Arial', 14)) 
btn_times.grid(row=4, column=4)

btn_divide = tk.Button(root, text='/', command=lambda: add_to_calculation('/'), width=5, font=('Arial', 14)) 
btn_divide.grid(row=5, column=4)

#we don't need lambda funcion for these - we are not calling a function, we are passing one since there are no parameters

btn_equals = tk.Button(root, text='=', command=evaluate_calculation, width=5, font=('Arial', 14)) 
btn_equals.grid(row=6, column=1, columnspan=2)

btn_clear = tk.Button(root, text='C', command=clear_field, width=5, font=('Arial', 14)) 
btn_clear.grid(row=6, column=3, columnspan=2)

#PARENTHESES

btn_open = tk.Button(root, text='(', command=lambda: add_to_calculation('('), width=5, font=('Arial', 14))
btn_open.grid(row=5, column=1)

btn_close = tk.Button(root, text=')', command=lambda: add_to_calculation(')'), width=5, font=('Arial', 14))
btn_close.grid(row=5, column=3)

#root.mainloop() - keeps interface open + responsive to user inputs
root.mainloop()