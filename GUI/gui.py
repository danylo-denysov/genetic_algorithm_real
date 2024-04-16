from tkinter import *
from tkinter import ttk, messagebox
from main import evolutionary_algorithm
import customtkinter


def submit():
    try:
        selection_type = variable.get()
        if selection_type == "Selection of the best":
            selection_type = 1
        elif selection_type == "Tournament selection":
            selection_type = 2
        elif selection_type == "Roulette selection":
            selection_type = 3
        mutation_type = variable1.get()
        if mutation_type == "Even mutation":
            mutation_type = 1
        elif mutation_type == "Index-swap mutation":
            mutation_type = 2
        elif mutation_type == "Gauss mutation":
            mutation_type = 3
        crossover_type = variable3.get()
        if crossover_type == "Arithmetic crossover":
            crossover_type = 1
        if crossover_type == "Blend (blx) crossover":
            crossover_type = 2
        if crossover_type == "Blend - beta (blx - b) crossover":
            crossover_type = 3
        if crossover_type == "Average crossover":
            crossover_type = 4
        if crossover_type == "Flat crossover":
            crossover_type = 5
        if crossover_type == "Heuristic crossover":
            crossover_type = 6
        if crossover_type == "Linear crossover":
            crossover_type = 7

        minimisation = None
        optm = variable_optm.get()
        if optm == "minimisation":
            minimisation = True
        if optm == "maximisation":
            minimisation = False

        func = choosen_func.get()
        if func == "Default (1)":
            func_type = 1
        if func == "Default (2)":
            func_type = 2
        if func == "Hypersphere":
            func_type = 3
        if func == "Hyperellipsoid":
            func_type = 4
        if func == "Schwefel":
            func_type = 5
        if func == "Ackley":
            func_type = 6
        if func == "Michalewicz":
            func_type = 7
        if func == "Rastrigin":
            func_type = 8
        if func == "Rosenbrock":
            func_type = 9
        if func == "De Jong 3":
            func_type = 10
        if func == "De Jong 5 (2)":
            func_type = 11
        if func == "Martin and Gaddy (2)":
            func_type = 12
        if func == 'Griewank':
            func_type = 13
        if func == "Easom (2)":
            func_type = 14
        if func == "Goldstein and Price (2)":
            func_type = 15
        if func == "Picheny, Goldstein and Price (2)":
            func_type = 16
        if func == "Styblinski and Tang":
            func_type = 17
        if func == "Mc Cormick (2)":
            func_type = 18
        if func == "Rana":
            func_type = 19
        if func == "Egg Holder":
            func_type = 20
        if func == "Keane":
            func_type = 21
        if func == "Schaffer 2 (2)":
            func_type = 22
        if func == "Himmelblau (2)":
            func_type = 23
        if func == "Pits and Holes (2)":
            func_type = 24

        variable_amount = int(entrybox11.get())
        a = float(entrybox.get())
        b = float(entrybox2.get())
        power_number_intervals = int(entrybox3.get())
        individual_amount = int(entrybox4.get())
        individual_selection_amount = int(entrybox5.get())
        epochs_amount = int(entrybox6.get())
        crossover_probability = float(entrybox7.get())
        mutation_probability = float(entrybox8.get())
        inversion_probability = float(entrybox9.get())
        individual_elitism_amount = int(entrybox10.get())

        return variable_amount, a, b, power_number_intervals, individual_amount, individual_selection_amount, \
            individual_elitism_amount, epochs_amount, selection_type, mutation_type, crossover_type, \
            crossover_probability, mutation_probability, inversion_probability, minimisation, func_type
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")


def execute_evolutionary_algorithm():
    try:
        values = submit()
        if values is not None:
            variable_amount, a, b, power_number_intervals, individual_amount, individual_selection_amount, \
                individual_elitism_amount, epochs_amount, selection_type, mutation_type, crossover_type, \
                crossover_probability, mutation_probability, inversion_probability, minimisation, func_type = values
            the_best_individuals, time = evolutionary_algorithm(variable_amount, a, b, power_number_intervals,
                                                                individual_amount, individual_selection_amount,
                                                                individual_elitism_amount, epochs_amount,
                                                                selection_type,
                                                                mutation_type, crossover_type,
                                                                crossover_probability, mutation_probability,
                                                                inversion_probability, minimisation, func_type)
            display_result_window(the_best_individuals, time)
    except ValueError as e:
        messagebox.showerror("Error", f"Invalid input: {str(e)}")
    except TypeError as e:
        messagebox.showerror("Error", f"Error during execution: {str(e)}")


def display_result_window(the_best_individuals, time):
    new_window = Toplevel()
    new_window.geometry("300x300")
    new_window.config(background="#3b3c3d")
    new_window.title("Result")
    individuals = list(the_best_individuals.values())
    our_individual = individuals[-1]
    label1 = Label(new_window, background="#3b3c3d", fg="white", text="The result: ")
    label1.pack()
    for i in our_individual.chromosome_values:
        label = Label(new_window, background="#3b3c3d", fg="white", text=str(i))
        label.pack()
    label2 = Label(new_window, background="#3b3c3d", fg="white",
                   text="Fitness function: " + str(our_individual.fitness_function_value))
    label2.pack()
    label3 = Label(new_window, background="#3b3c3d", fg="white",
                   text="Time: " + str(time) + " s")
    label3.pack()
    new_window.mainloop()


window = customtkinter.CTk()
window.geometry("500x700")
window.title("Evolutionary Algorithms")
window.config(background="#3b3c3d")
# icon = PhotoImage(file='kwadrat.png')
# window.iconphoto(True, icon)

# Ustawienie stylu dla list rozwijanych
style = ttk.Style()
style.configure('TCombobox', padding=2, relief="flat", borderwidth=5, highlightthickness=0)
style.map('TCombobox', fieldbackground=[('readonly', '#2b2b2a')])

# Ustawienie stylu dla pól Entry
style.configure('TEntry', padding=2, relief="flat", borderwidth=5, highlightthickness=0)
style.map('TEntry', fieldbackground=[('readonly', '#2b2b2a')])


def create_entry_label_pair(description, row):
    label = Label(
        window,
        text=description,
        font=('Calibri', 14),
        bg="#3b3c3d",
        fg='#f6f7df',
    )
    label.grid(row=row, column=0, pady=5, padx=10, sticky=E)

    entry = Entry(
        window,
        font=('Calibri', 12, 'bold'),
        bg="#2b2b2a",
        fg='#f6f7df',
    )
    entry.grid(row=row, column=1, pady=5, padx=10, sticky=W)

    return entry


row_counter = 0
entrybox0 = create_entry_label_pair("choose function:", row_counter)
funcs = ["Default (1)", "Default (2)", "Hypersphere", "Hyperellipsoid", "Schwefel", "Ackley", "Michalewicz",
         "Rastrigin", "Rosenbrock", "De Jong 3", "De Jong 5 (2)", "Martin and Gaddy (2)", 'Griewank', "Easom (2)",
         "Goldstein and Price (2)", "Picheny, Goldstein and Price (2)", "Styblinski and Tang", "Mc Cormick (2)", "Rana",
         "Egg Holder", "Keane", "Schaffer 2 (2)", "Himmelblau (2)", "Pits and Holes (2)"]
choosen_func = StringVar(window)
choosen_func.set(funcs[0])
option_menu_funcs = OptionMenu(window, choosen_func, *funcs)
option_menu_funcs.config(
    font=('Calibri', 12),
    bg="#2b2b2a",
    fg='#f6f7df',
    activebackground="#2b2b2a",
    activeforeground='#f6f7df',
    width=17,
    bd=0,
    highlightthickness=0
)
option_menu_funcs.grid(row=row_counter, column=1, pady=5, padx=10, sticky=W)
row_counter += 1
entrybox11 = create_entry_label_pair("amount of variables:", row_counter)
entrybox11.insert(0, "2")
row_counter += 1
entrybox = create_entry_label_pair("start of the range:", row_counter)
entrybox.insert(0, "-5")
row_counter += 1
entrybox2 = create_entry_label_pair("end of the range:", row_counter)
entrybox2.insert(0, "5")
row_counter += 1
entrybox3 = create_entry_label_pair("precision:", row_counter)
entrybox3.insert(0, "12")
row_counter += 1
entrybox4 = create_entry_label_pair("amount of individuals:", row_counter)
entrybox4.insert(0, "1000")
row_counter += 1
entrybox5 = create_entry_label_pair("amount of best individuals:", row_counter)
entrybox5.insert(0, "200")
row_counter += 1
entrybox10 = create_entry_label_pair("elite individuals amount:", row_counter)
entrybox10.insert(0, "2")
row_counter += 1
entrybox6 = create_entry_label_pair("amount of epochs:", row_counter)
entrybox6.insert(0, "100")
row_counter += 1
entrybox7 = create_entry_label_pair("crossing probability:", row_counter)
entrybox7.insert(0, "0.7")
row_counter += 1
entrybox8 = create_entry_label_pair("mutation probability:", row_counter)
entrybox8.insert(0, "0.3")
row_counter += 1
entrybox9 = create_entry_label_pair("inversion probability:", row_counter)
entrybox9.insert(0, "0.1")
row_counter += 1

label_description10 = Label(
    window,
    text="selection type:",
    font=('Calibri', 14),
    bg="#3b3c3d",
    fg='#f6f7df',
)
label_description10.grid(row=row_counter, column=0, pady=5, padx=10, sticky=E)
options = ["Selection of the best", "Tournament selection", "Roulette selection"]
variable = StringVar(window)
variable.set(options[0])
option_menu = OptionMenu(window, variable, *options)
option_menu.config(
    font=('Calibri', 12),
    bg="#2b2b2a",
    fg='#f6f7df',
    activebackground="#2b2b2a",
    activeforeground='#f6f7df',
    width=17,
    bd=0,
    highlightthickness=0
)
option_menu.grid(row=row_counter, column=1, pady=5, padx=10, sticky=W)

row_counter += 1
label_description12 = Label(
    window,
    text="crossing type:",
    font=('Calibri', 14),
    bg="#3b3c3d",
    fg='#f6f7df',
)
label_description12.grid(row=row_counter, column=0, pady=5, padx=10, sticky=E)
options = ["Arithmetic crossover", "Blend (blx) crossover", "Blend - beta (blx - b) crossover", "Average crossover",
           "Flat crossover", "Heuristic crossover", "Linear crossover"]
variable3 = StringVar(window)
variable3.set(options[0])
option_menu = OptionMenu(window, variable3, *options)
option_menu.config(
    font=('Calibri', 12),
    bg="#2b2b2a",
    fg='#f6f7df',
    activebackground="#2b2b2a",
    activeforeground='#f6f7df',
    width=17,
    bd=0,
    highlightthickness=0
)
option_menu.grid(row=row_counter, column=1, pady=5, padx=10, sticky=W)

row_counter += 1
label_description11 = Label(
    window,
    text="mutation type:",
    font=('Calibri', 14),
    bg="#3b3c3d",
    fg='#f6f7df',
)
label_description11.grid(row=row_counter, column=0, pady=5, padx=10, sticky=E)
options1 = ["Even mutation", "Index-swap mutation", "Gauss mutation"]
variable1 = StringVar(window)
variable1.set(options1[0])
option_menu1 = OptionMenu(window, variable1, *options1)
option_menu1.config(
    font=('Calibri', 12),
    bg="#2b2b2a",
    fg='#f6f7df',
    activebackground="#2b2b2a",
    activeforeground='#f6f7df',
    width=17,
    bd=0,
    highlightthickness=0
)
option_menu1.grid(row=row_counter, column=1, pady=5, padx=10, sticky=W)

row_counter += 1
variable_optm = StringVar(window)
variable_optm.set("minimisation")
r1 = Radiobutton(window, text="Minimisation", value="minimisation", font=('Calibri', 12), bg="#3b3c3d", fg='#f6f7df',
                 selectcolor="#3b3c3d", activeforeground="#f6f7df",
                 activebackground="#3b3c3d", variable=variable_optm)
r1.grid(row=row_counter, column=0, pady=(10, 0), sticky=E)
r2 = Radiobutton(window, text="Maximisation", value="maximisation", font=('Calibri', 12), bg="#3b3c3d", fg='#f6f7df',
                 selectcolor="#3b3c3d", activeforeground="#f6f7df",
                 activebackground="#3b3c3d", variable=variable_optm)
r2.grid(row=row_counter, column=1, pady=(10, 0), sticky=W)

row_counter += 1
submit_button = Button(window,
                       text="Submit",
                       font=('Calibri', 10),
                       command=execute_evolutionary_algorithm,
                       width=20,
                       bg="#2b2b2a",
                       fg='#f6f7df',
                       activebackground="#2b2b2a",
                       activeforeground='#f6f7df'
                       )
submit_button.place(relx=0.5, rely=0.93, anchor="center")

x_offset = (window.winfo_screenwidth() - window.winfo_reqwidth()) // 2
y_offset = (window.winfo_screenheight() - window.winfo_reqheight()) // 2
window.geometry("+{}+{}".format(x_offset, y_offset))
window.eval('tk::PlaceWindow . center')
window.mainloop()
