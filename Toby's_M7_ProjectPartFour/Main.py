import tkinter as tk

from tkinter import ttk
from tkinter import messagebox


# Function to handle the button click event

def add_to_cart():

    item = item_entry.get()

    quantity = int(quantity_entry.get())

    category = category_var.get()

    price = price_entry.get()

    if item and quantity > 1000:  # Put in place to stop quantity from exceding the maximum
        messagebox.showinfo("Maximum", "The maximum has been reached")
    else:

        cart_listbox.insert(
            tk.END, f"{quantity} x {price} x {item} ({category})")

    item_entry.delete(0, tk.END)

    quantity_entry.delete(0, tk.END)

    price_entry.delete(0, tk.END)

    update_total()
    update_totalprice()


def clear_cart():

    cart_listbox.delete(0, tk.END)

    update_total()
    update_totalprice()


def update_total():  # Used to Count the total of a item

    total_items = sum(int(entry.split(' x ')[0])
                      for entry in cart_listbox.get(0, tk.END))

    total_label.config(text=f'Total Items: {total_items}')

    progress['value'] = total_items


def update_totalprice():  # Used to get the total price of the item

    total_price = sum(float(entry.split(' x ')[0]) * float(entry.split('x')[1])
                      for entry in cart_listbox.get(0, tk.END))

    total_price_label.config(text=f'Total Price:$ {total_price}')


def about():

    tk.messagebox.showinfo("About", "Toby Grocery Store Application v1.0")


# Create the main application window
root = tk.Tk()
root.geometry('740x740')

root.title('Nash & Nibbles Inventory List')

# Create a menubar

menubar = tk.Menu(root)

root.config(menu=menubar)


# Create a File menu and add items

file_menu = tk.Menu(menubar, tearoff=0)

file_menu.add_command(label="New", command=clear_cart)

file_menu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=file_menu)


# Create a Help menu and add items

help_menu = tk.Menu(menubar, tearoff=0)

help_menu.add_command(label="About", command=about)

menubar.add_cascade(label="Help", menu=help_menu)


# Create a frame to hold the widgets with padding

content = ttk.Frame(root, padding=(10, 10, 10, 10))

content.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))


# Configure grid columns and rows to be resizable

root.columnconfigure(0, weight=1)

root.rowconfigure(0, weight=1)

root.rowconfigure(0, weight=1)

content.columnconfigure(0, weight=1)

content.columnconfigure(1, weight=1)

content.columnconfigure(2, weight=1)

content.columnconfigure(3, weight=1)

# Create a label for the item entry

item_label = ttk.Label(content, text="Enter Item:")

item_label.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)


# Create an entry widget for item input

item_entry = ttk.Entry(content, width=20)

item_entry.grid(column=1, row=0, padx=5, pady=5, sticky=(tk.W, tk.E))

# Label For Price
price_label = ttk.Label(content, text="Enter Price:")

price_label.grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)

# Entry widget for price
price_entry = ttk.Entry(content, width=20)

price_entry.grid(column=1, row=1, padx=5, pady=5, sticky=(tk.W, tk.E))


# Create a label for the quantity entry

quantity_label = ttk.Label(content, text="Quantity:")

quantity_label.grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)


# Create an entry widget for quantity input

quantity_entry = ttk.Entry(content, width=20)

quantity_entry.grid(column=1, row=2, padx=5, pady=5, sticky=(tk.W, tk.E))


# Create radio buttons for selecting item category

category_var = tk.StringVar(value="Fruits")

category_label = ttk.Label(content, text="Category:")

category_label.grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)


fruits_radio = ttk.Radiobutton(
    content, text="Fruits", variable=category_var, value="Fruits")

fruits_radio.grid(column=1, row=3, padx=5, pady=5, sticky=tk.W)


vegetables_radio = ttk.Radiobutton(
    content, text="Vegetables", variable=category_var, value="Vegetables")

vegetables_radio.grid(column=1, row=4, padx=5, pady=5, sticky=tk.W)

produce_radio = ttk.Radiobutton(
    content, text="Produce", variable=category_var, value="Produce")

produce_radio.grid(column=1, row=5, padx=5, pady=5, sticky=tk.W)


dairy_radio = ttk.Radiobutton(
    content, text="Dairy", variable=category_var, value="Dairy")

dairy_radio.grid(column=1, row=6, padx=6, pady=5, sticky=tk.W)

# Create a button to add the item to the cart

add_button = ttk.Button(content, text="Add to Cart", command=add_to_cart)

add_button.grid(column=2, row=0, rowspan=2, padx=5,
                pady=5, sticky=(tk.N, tk.S, tk.E, tk.W))


# Create a button to clear the cart

clear_button = ttk.Button(content, text="Clear Cart", command=clear_cart)

clear_button.grid(column=2, row=5, padx=5, pady=5,
                  sticky=(tk.N, tk.S, tk.E, tk.W))


# Create a listbox to display items in the cart

cart_label = ttk.Label(content, text="Cart:")

cart_label.grid(column=0, row=8, padx=5, pady=5, sticky=tk.W)


cart_listbox = tk.Listbox(content, height=10)

cart_listbox.grid(column=0, row=9, columnspan=3,
                  padx=5, pady=5, sticky=(tk.W, tk.E))


# Create a label to display the total number of items

total_label = ttk.Label(content, text="Total Items: 0")

total_label.grid(column=0, row=10, columnspan=2, padx=5, pady=5, sticky=tk.W)


total_price_label = ttk.Label(content, text="Total Price:$ 0")

total_price_label.grid(column=0, row=11, columnspan=2,
                       padx=5, pady=5, sticky=tk.W)

# Create a progress bar to visually represent the total number of items

progress = ttk.Progressbar(
    content, orient='horizontal', length=200, mode='determinate', maximum=1000)

progress.grid(column=2, row=10, padx=5, pady=5, sticky=(tk.W, tk.E))

about = ttk.Button(content, text="About", command=about)

about.grid(column=2, row=12, rowspan=2, padx=5,
           pady=5, sticky=(tk.N, tk.S, tk.E, tk.W))


# Start the Tkinter event loop

root.mainloop()
