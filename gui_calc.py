from tkinter import *

root = Tk()
root.title('Calculator')
output = Entry(width=35, borderwidth=5)
output.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def num_click(number):
    current = output.get()
    output.delete(0, END)
    output.insert(0,str(current) + str(number))
def function_click(function):
    current = output.get()
    global first_number
    first_number = current
    output.delete(0, END)
    output.insert(0,str(current) + str(function))
    #print(first_number)
    global function_output
    function_output = function
def off_click():
    quit()
def delete_click():
    output.delete(0,END)
def get_second_number(statement):
    global second_number
    second_number = ''
    is_in_second_number = False
    for i in range(len(str(statement))):
        if is_in_second_number == True:
            second_number += statement[i]
        if (statement[i] == '+') or (statement[i] == '-') or (statement[i] == 'x') or (statement[i] == '/') or (statement[i] == '%'):
            is_in_second_number = True
def equal_click():
    get_second_number(output.get())
    #print(first_number)
    #print(second_number)
    output.delete(0,END)
    if function_output == '+':
        output.insert(0,int(first_number) + int(second_number))
    elif function_output == '-':
        output.insert(0,int(first_number) - int(second_number))
    elif function_output == 'x':
        output.insert(0,int(first_number) * int(second_number))
    elif function_output == '/':
        output.insert(0,int(first_number) / int(second_number))
    elif function_output == '%':
        output.insert(0,int(first_number) % int(second_number))
#c1
c_button = Button(text='C' , bg='black', fg='lightgreen', padx= 25, pady= 15, command= lambda: delete_click()).grid(row= 3, column=0)
seven_button = Button(text='7' , bg='black', fg='lightgreen', padx= 25, pady= 15, command= lambda: num_click(7)).grid(row= 4, column=0)
four_button = Button(text='4' , bg='black', fg='lightgreen', padx= 25, pady= 15, command= lambda: num_click(4)).grid(row= 5, column=0)
one_button = Button(text='1' ,  bg='black', fg='lightgreen', padx= 25, pady= 15 ,command= lambda: num_click(1)).grid(row= 6, column=0)
nothing_button = Button(text=' ' ,  bg='black', fg='lightgreen', padx= 25, pady= 15).grid(row= 7, column=0)
#C2
off_button = Button(text='off' , bg='black', fg='lightgreen', padx= 25, pady= 15, command= lambda: off_click()).grid(row= 3, column=1)
eight_button = Button(text='8' ,  bg='black', fg='lightgreen', padx= 25, pady= 15, command= lambda: num_click(8)).grid(row= 4, column=1)
five_button = Button(text='5' , bg='black', fg='lightgreen', padx= 25, pady= 15, command= lambda: num_click(5)).grid(row= 5, column=1)
two_button = Button(text='2' , bg='black', fg='lightgreen', padx= 25, pady= 15, command= lambda: num_click(2)).grid(row= 6, column=1)
zero_button = Button(text='0' ,  bg='black', fg='lightgreen', padx= 25, pady= 15, command= lambda: num_click(0)).grid(row= 7, column=1)
#C3
percent_button = Button(text='%' , bg='black', fg='lightgreen', padx= 25, pady= 15, command= lambda: function_click('%')).grid(row= 3, column=2)
nine_button = Button(text='9' ,  bg='black', fg='lightgreen', padx= 25, pady= 15,  command= lambda: num_click(9)).grid(row=4, column=2)
six_button = Button(text='6' ,  bg='black', fg='lightgreen', padx= 25, pady= 15,  command= lambda: num_click(6)).grid(row= 5, column=2)
three_button = Button(text='3' ,  bg='black', fg='lightgreen', padx= 25, pady= 15,  command= lambda: num_click(3)).grid(row= 6, column=2)
comma_button = Button(text='.' ,  bg='black', fg='lightgreen', padx= 25, pady= 15, command= lambda: num_click('.')).grid(row= 7, column=2)
#C4
division_button = Button(text='/' ,  bg='black', fg='lightgreen', padx= 25, pady= 15, command= lambda: function_click('/')).grid(row= 3, column=3)
multiplication_button = Button(text='x' ,  bg='black', fg='lightgreen', padx= 25, pady= 15, command= lambda: function_click('x')).grid(row= 4, column=3)
substraction_button = Button(text='-' ,  bg='black', fg='lightgreen', padx= 25, pady= 15, command= lambda: function_click('-')).grid(row= 5, column=3)
addition_button = Button(text='+' , bg='black', fg='lightgreen', padx= 25, pady= 15, command= lambda: function_click('+')).grid(row= 6, column=3)
equals_button = Button(text='=' ,  bg='black', fg='lightgreen', padx= 25, pady= 15, command= lambda: equal_click()).grid(row= 7, column=3)

root.mainloop()
