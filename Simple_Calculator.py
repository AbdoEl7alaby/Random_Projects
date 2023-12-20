import tkinter as tk
import math
# Initialize the main window
root = tk.Tk()
root.geometry("400x250")
root.resizable(False, False)
root.title("Simple Calculator")

# Define functions for user interaction
def on_enter(event=None):
    button_calc.invoke()
#-----------------------------------------------------------------------------------------
def get_operator():
    operator = entry2.get()
    if operator == "+":
        get_sum()
    elif operator == "-":
        get_diff()
    elif operator == "x" or operator == "*":
        get_mult()
    elif operator == "/":
        get_div()
    elif operator == "%":
        get_mod()
    elif operator == "^":
        get_pow()
    else:
        result_label.config(text="Invalid input! Please enter valid operator.",font=("Arial",15),fg="red",borderwidth=6,relief='ridge')
#-----------------------------------------------------------------------------------------
def get_sum():
     try:
          num1 = float(entry1.get())
          num2 = float(entry3.get())
          sum = num1 + num2
          if int(sum) == sum:
               result_label.config(text=f"Result: {int(sum)}",font=("Arial",20),fg="green",borderwidth=6,relief='ridge')
          else:
               result_label.config(text=f"Result: {sum}",font=("Arial",20),fg="green",borderwidth=6,relief='ridge')
     except ValueError:
          result_label.config(text="Invalid input! Please enter valid numbers.",font=("Arial",15),fg="red",borderwidth=6,relief='ridge')

def get_diff():
     try:
          num1 = float(entry1.get())
          num2 = float(entry3.get())
          diff = num1 - num2
          if int(diff) == diff:
               result_label.config(text=f"Result: {int(diff)}",font=("Arial",20),fg="green",borderwidth=6,relief='ridge')
          else:
               result_label.config(text=f"Result: {diff}",font=("Arial",20),fg="green",borderwidth=6,relief='ridge')
     except ValueError:
          result_label.config(text="Invalid input! Please enter valid numbers.",font=("Arial",15),fg="red",borderwidth=6,relief='ridge')


def get_mult():
     try:
          num1 = float(entry1.get())
          num2 = float(entry3.get())
          mult = num1 * num2
          if int(mult) == mult:
               result_label.config(text=f"Result: {int(mult)}",font=("Arial",20),fg="green",borderwidth=6,relief='ridge')
          else:
               result_label.config(text=f"Result: {mult}",font=("Arial",20),fg="green",borderwidth=6,relief='ridge')
     except ValueError:
          result_label.config(text="Invalid input! Please enter valid numbers.",font=("Arial",15),fg="red",borderwidth=6,relief='ridge')

def get_div():
     try:
          num1 = float(entry1.get())
          num2 = float(entry3.get())
          div = num1/num2
          if int(div) == div :
               result_label.config(text=f"Result: {int(div)}",font=("Arial",20),fg="green",borderwidth=6,relief='ridge')
          else:
               result_label.config(text=f"Result: {div}",font=("Arial",20),fg="green",borderwidth=6,relief='ridge')
     except ValueError:
          result_label.config(text="Invalid input! Please enter valid numbers.",font=("Arial",15),fg="red",borderwidth=6,relief='ridge')

def get_mod():
     try:
          num1 = float(entry1.get())
          num2 = float(entry3.get())
          mod = num1%num2
          if int(mod) == mod :
               result_label.config(text=f"Result: {int(mod)}",font=("Arial",20),fg="green",borderwidth=6,relief='ridge')
          else:
               result_label.config(text=f"Result: {mod}",font=("Arial",20),fg="green",borderwidth=6,relief='ridge')
     except ValueError:
          result_label.config(text="Invalid input! Please enter valid numbers.",font=("Arial",15),fg="red",borderwidth=6,relief='ridge')

def get_pow():
    try:
        num1 = float(entry1.get())
        num2 = float(entry3.get())
        power = math.pow(num1,num2)
        if int(power) == power:
            result_label.config(text=f"Result: {int(power)}",font=("Arial",20),fg="green",borderwidth=6,relief='ridge')
        else:
            result_label.config(text=f"Result: {power}",font=("Arial",20),fg="green",borderwidth=6,relief='ridge')
    except ValueError:
        result_label.config(text="Invalid input! Please enter valid numbers.",font=("Arial",15),fg="red",borderwidth=6,relief='ridge')

#-----------------------------------------------------------------------------------------
def check_entry(*args):
     if entry1.get() == "" or entry2.get() == "" or entry3.get() == "":
          button_calc.config(state=tk.DISABLED)
     else:
          button_calc.config(state=tk.NORMAL)
          
def clear_fields():
     entry1.delete(0, tk.END)
     entry2.delete(0, tk.END)
     entry3.delete(0, tk.END)
     result_label.config(text="")
#-----------------------------------------------------------------------------------------
# Create labels and entry fields
label = tk.Label(root,text="Sum(+),Subbtract(-),Product(*or x),Divide(/),Mod(%),Power(^)",font=("Arial",10,"bold"))
label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
label1 = tk.Label(root, text="Number 1:")
label1.place(x=130,y=40)
entry1 = tk.Entry(root, width=20)
entry1.place(x=200,y=40)
entry1.bind("<KeyRelease>", check_entry)
entry1.bind("<Return>", on_enter)

label2 = tk.Label(root, text="The operator:")
label2.place(x=118,y=70)
entry2 = tk.Entry(root, width=5)
entry2.place(x=245,y=70)
entry2.bind("<KeyRelease>", check_entry)
entry2.bind("<Return>", on_enter)

label3 = tk.Label(root, text="Number 2:")
label3.place(x=130,y=100)
entry3 = tk.Entry(root, width=20)
entry3.place(x=200,y=100)
entry3.bind("<KeyRelease>", check_entry)
entry3.bind("<Return>", on_enter)
#-----------------------------------------------------------------------------------------
# Create buttons
button_calc = tk.Button(root, text="Calculate", command=get_operator)
button_calc.place(x=130,y=140)
button_calc.config(state=tk.DISABLED)

button_clear = tk.Button(root, text="Clear", command=clear_fields)
button_clear.place(x=220,y=140)
#-----------------------------------------------------------------------------------------
# Create result label
result_label = tk.Label(root, text="")
result_label.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Start the main loop
root.mainloop()
