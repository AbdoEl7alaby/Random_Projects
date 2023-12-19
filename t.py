import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Simple Calculator")

# Define functions for user interaction
def on_enter(event=None):
    button_calc.invoke()

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
          else:
               result_label.config(text="Invalid input! Please enter valid operator.")

def get_sum():
     try:
          num1 = float(entry1.get())
          num2 = float(entry3.get())
          sum = num1 + num2
          if int(sum) == sum:
               result_label.config(text=f"Result: {int(sum)}")
          else:
               result_label.config(text=f"Result: {sum}")
     except ValueError:
          result_label.config(text="Invalid input! Please enter valid numbers.")

def get_diff():
     try:
          num1 = float(entry1.get())
          num2 = float(entry3.get())
          diff = num1 - num2
          if int(diff) == diff:
               result_label.config(text=f"Result: {int(diff)}")
          else:
               result_label.config(text=f"Result: {diff}")
     except ValueError:
          result_label.config(text="Invalid input! Please enter valid numbers.")


def get_mult():
     try:
          num1 = float(entry1.get())
          num2 = float(entry3.get())
          mult = num1 * num2
          if int(mult) == mult:
               result_label.config(text=f"Result: {int(mult)}")
          else:
               result_label.config(text=f"Result: {mult}")
     except ValueError:
          result_label.config(text="Invalid input! Please enter valid numbers.")

def get_div():
     try:
          num1 = float(entry1.get())
          num2 = float(entry3.get())
          div = num1/num2
          if int(div) == div :
               result_label.config(text=f"Result: {int(div)}")
          else:
               result_label.config(text=f"Result: {div}")
     except ValueError:
          result_label.config(text="Invalid input! Please enter valid numbers.")

def get_mod():
     try:
          num1 = float(entry1.get())
          num2 = float(entry3.get())
          mod = num1%num2
          if int(mod) == mod :
               result_label.config(text=f"Result: {int(mod)}")
          else:
               result_label.config(text=f"Result: {mod}")
     except ValueError:
          result_label.config(text="Invalid input! Please enter valid numbers.")

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

# Create labels and entry fields
label1 = tk.Label(root, text="Number 1:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root, width=20)
entry1.grid(row=0, column=1)
entry1.bind("<KeyRelease>", check_entry)
entry1.bind("<Return>", on_enter)

label2 = tk.Label(root, text="The operator:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root, width=5)
entry2.grid(row=1, column=1)
entry2.bind("<KeyRelease>", check_entry)
entry2.bind("<Return>", on_enter)

label3 = tk.Label(root, text="Number 2:")
label3.grid(row=3, column=0)
entry3 = tk.Entry(root, width=20)
entry3.grid(row=3, column=1)
entry3.bind("<KeyRelease>", check_entry)
entry3.bind("<Return>", on_enter)

# Create buttons
button_calc = tk.Button(root, text="Calculate", command=get_operator)
button_calc.grid(row=4, column=0)
button_calc.config(state=tk.DISABLED)

button_clear = tk.Button(root, text="Clear", command=clear_fields)
button_clear.grid(row=4, column=1)

# Create result label
result_label = tk.Label(root, text="")
result_label.grid(row=5, columnspan=2)

# Start the main loop
root.mainloop()
