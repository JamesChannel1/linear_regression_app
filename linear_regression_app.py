import tkinter as tk  
import numpy as np  
from sklearn.linear_model import LinearRegression  
import matplotlib.pyplot as plt  


def on_button_click():
    x_str = x_axis_entry.get()
    y_str = y_axis_entry.get()

    try:
        X = np.array(list(map(float, x_str.split(',')))).reshape(-1, 1)
        y = np.array(list(map(float, y_str.split(','))))

        model = LinearRegression()
        model.fit(X, y)
        y_pred = model.predict(X)
        intercept_value = model.intercept_
        coefficient_value = model.coef_


        # new UI window
        new_window = tk.Toplevel(root)
        new_window.title("Values")

        # intercept and coefficient values outputted as labels
        intercept_label = tk.Label(new_window, text=f"Intercept: {intercept_value}")
        intercept_label.pack()

        coefficient_label = tk.Label(new_window, text=f"Coefficient: {coefficient_value}")
        coefficient_label.pack()

        # plotting graph
        plt.scatter(X, y, color='blue', label='Actual Data')
        plt.plot(X, y_pred, color='red', label='Regression Line')
        plt.xlabel('X (Feature)')
        plt.ylabel('y (Target)')
        plt.title('Linear Regression')
        plt.legend()
        plt.show()

    except ValueError:
        print('Invalid input. Please enter comma-separated numeric values.')


root = tk.Tk()
root.title("Linear Regression App")
root.geometry("300x200")

label_x = tk.Label(root, text="Enter X values (comma-separated):")
label_x.pack()

x_axis_entry = tk.Entry(root)
x_axis_entry.pack()

label_y = tk.Label(root, text="Enter Y values (comma-separated):")
label_y.pack()

y_axis_entry = tk.Entry(root)
y_axis_entry.pack()

button = tk.Button(root, text="Perform Regression", command=on_button_click)
button.pack()

root.mainloop()

