from tkinter import *
from tkinter import filedialog, messagebox

def text_widget_demo():
    root = Tk()
    root.title("Text Widget Demo")
    root.geometry("600x500")
    
    # Create Text widget with Scrollbar
    frame = Frame(root)
    frame.pack(fill=BOTH, side=BOTTOM,expand=True, padx=10, pady=10)
    
    text_widget = Text(frame, wrap=WORD, width=55, font=("Arial", 12), undo=True)
    scrollbar = Scrollbar(frame, orient=VERTICAL, command=text_widget.yview)
    text_widget.config(yscrollcommand=scrollbar.set)
    
    text_widget.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(fill=Y, side=RIGHT)
    
    # Text widget methods
    def get_text():
        content = text_widget.get(1.0, END)  # 1.0 = line 1, character 0
        print(f"Text content:\n{content.strip()}")
    
    def insert_text():
        text_widget.insert(END, "\nInserted text at end!")
    
    def delete_text():
        text_widget.delete(1.0, END)  # Clear all text
    
    def search_text():
        search_term = "python"
        text_widget.tag_remove("highlight", 1.0, END)
        if search_term:
            start_pos = "1.0"
            while True:
                start_pos = text_widget.search(search_term, start_pos, stopindex=END)
                if not start_pos:
                    break
                end_pos = f"{start_pos}+{len(search_term)}c"
                text_widget.tag_add("highlight", start_pos, end_pos)
                start_pos = end_pos
            text_widget.tag_config("highlight", background="yellow")
    
    # Button frame
    btn_frame = Frame(root)
    btn_frame.pack(fill=Y, side=TOP, padx=10, pady=5)
    
    Button(btn_frame, text="Get Text", command=get_text).pack(side=LEFT, padx=5)
    Button(btn_frame, text="Insert Text", command=insert_text).pack(side=LEFT, padx=5)
    Button(btn_frame, text="Clear", command=delete_text).pack(side=LEFT, padx=5)
    Button(btn_frame, text="Search 'python'", command=search_text).pack(side=LEFT, padx=5)
    
    # Insert sample text
    sample_text = """Welcome to the Text Widget Demo!

This is a multi-line text editor widget.
You can:
• Type multiple lines of text
• Copy, cut, and paste text
• Search and highlight text
• Undo and redo actions

Try typing some text and using the buttons above!"""
    text_widget.insert(1.0, sample_text)
    
    root.mainloop()

def radiobutton_demo():
    root = Tk()
    root.title("Radiobutton Demo")
    root.geometry("400x350")
    
    # Radio button variables
    choice_var = StringVar(value="option1")  # Default selection
    
    Label(root, text="Select your favorite programming language:", 
          font=("Arial", 12, "bold")).pack(pady=10)
    
    # Radio buttons
    languages = [
        ("Python", "python"),
        ("JavaScript", "javascript"),
        ("Java", "java"),
        ("C++", "cpp"),
        ("Go", "go")
    ]
    
    for i, (text, value) in enumerate(languages):
        Radiobutton(root, text=text, variable=choice_var, 
                   value=value, font=("Arial", 11)).pack(anchor="w", padx=30, pady=5)
    
    def show_selection():
        messagebox.showinfo("Selection", f"You selected: {choice_var.get()}")
    
    Button(root, text="Confirm Selection", command=show_selection,
          font=("Arial", 12)).pack(pady=20)
    
    # Multiple radio groups
    frame = LabelFrame(root, text="Experience Level", font=("Arial", 10, "bold"))
    frame.pack(padx=20, pady=10, fill=X)
    
    exp_var = StringVar(value="beginner")
    
    levels = ["Beginner", "Intermediate", "Advanced", "Expert"]
    for level in levels:
        Radiobutton(frame, text=level, variable=exp_var, 
                   value=level.lower(), font=("Arial", 10)).pack(anchor="w", padx=10, pady=2)
    
    def show_all_selections():
        result = f"Language: {choice_var.get()}\nExperience: {exp_var.get()}"
        messagebox.showinfo("All Selections", result)
    
    Button(root, text="Show All Selections", command=show_all_selections,
          font=("Arial", 12)).pack(pady=10)
    
    root.mainloop()

def listbox_demo():
    root = Tk()
    root.title("Listbox Demo")
    root.geometry("500x400")
    
    # Create listbox with scrollbar
    frame = Frame(root)
    frame.pack(fill=BOTH, expand=True, padx=20, pady=10)
    
    listbox = Listbox(frame, font=("Arial", 12), selectmode=EXTENDED)
    scrollbar = Scrollbar(frame, orient=VERTICAL, command=listbox.yview)
    listbox.config(yscrollcommand=scrollbar.set)
    
    listbox.pack(side=LEFT, fill=BOTH, expand=True)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    # Add sample items
    items = ["Apple", "Banana", "Orange", "Grapes", "Mango", 
             "Pineapple", "Strawberry", "Watermelon", "Kiwi", "Peach"]
    
    for item in items:
        listbox.insert(END, item)
    
    # Listbox operations
    def add_item():
        new_item = f"Item {listbox.size() + 1}"
        listbox.insert(END, new_item)
    
    def delete_selected():
        selected = listbox.curselection()
        for index in selected[::-1]:  # Reverse to maintain indices
            listbox.delete(index)
    
    def get_selected():
        selected = listbox.curselection()
        if selected:
            items = [listbox.get(i) for i in selected]
            messagebox.showinfo("Selected Items", "\n".join(items))
        else:
            messagebox.showwarning("No Selection", "Please select an item first!")
    
    def clear_all():
        listbox.delete(0, END)
    
    def sort_items():
        items = list(listbox.get(0, END))
        items.sort()
        listbox.delete(0, END)
        for item in items:
            listbox.insert(END, item)
    
    # Buttons
    btn_frame = Frame(root)
    btn_frame.pack(fill=X, padx=20, pady=10)
    
    Button(btn_frame, text="Add Item", command=add_item).pack(side=LEFT, padx=5)
    Button(btn_frame, text="Delete Selected", command=delete_selected).pack(side=LEFT, padx=5)
    Button(btn_frame, text="Get Selected", command=get_selected).pack(side=LEFT, padx=5)
    Button(btn_frame, text="Clear All", command=clear_all).pack(side=LEFT, padx=5)
    Button(btn_frame, text="Sort", command=sort_items).pack(side=LEFT, padx=5)
    
    # Double-click to select
    def on_double_click(event):
        selection = listbox.curselection()
        if selection:
            item = listbox.get(selection[0])
            print(f"Double-clicked: {item}")
    
    listbox.bind("<Double-Button-1>", on_double_click)
    
    root.mainloop()


from tkinter import ttk

def combobox_demo():
    root = Tk()
    root.title("Combobox Demo")
    root.geometry("500x400")
    
    # Basic Combobox
    Label(root, text="Basic Combobox:", font=("Arial", 12, "bold")).pack(pady=10)
    
    values = ["Python", "JavaScript", "Java", "C++", "C#", "Go", "Rust", "Swift", "Kotlin"]
    combo1 = ttk.Combobox(root, values=values, font=("Arial", 12))
    combo1.pack(pady=5)
    combo1.set("Select a language")  # Default text
    
    # Readonly Combobox
    Label(root, text="Readonly Combobox:", font=("Arial", 12, "bold")).pack(pady=10)
    
    combo2 = ttk.Combobox(root, values=values, state="readonly", font=("Arial", 12))
    combo2.pack(pady=5)
    combo2.set("Python")  # Default selection
    
    # Combobox with postcommand
    def update_values():
        new_values = [f"Item {i}" for i in range(1, 6)]
        combo3['values'] = new_values
    
    Label(root, text="Dynamic Combobox:", font=("Arial", 12, "bold")).pack(pady=10)
    
    combo3 = ttk.Combobox(root, postcommand=update_values, font=("Arial", 12))
    combo3.pack(pady=5)
    
    # Get selection
    def show_selection():
        selections = f"""
        Basic: {combo1.get()}
        Readonly: {combo2.get()}
        Dynamic: {combo3.get()}
        """
        messagebox.showinfo("Selections", selections)
    
    Button(root, text="Show Selections", command=show_selection,
          font=("Arial", 12)).pack(pady=20)
    
    # Bind events
    def on_select(event):
        widget = event.widget
        print(f"Selected: {widget.get()}")
    
    combo1.bind("<<ComboboxSelected>>", on_select)
    combo2.bind("<<ComboboxSelected>>", on_select)
    
    root.mainloop()

def progressbar_demo():
    root = Tk()
    root.title("Progressbar Demo")
    root.geometry("500x300")
    
    # Progressbars
    Label(root, text="Determinate Progressbar:", font=("Arial", 12, "bold")).pack(pady=10)
    
    progress1 = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='determinate')
    progress1.pack(pady=5)
    
    Label(root, text="Indeterminate Progressbar:", font=("Arial", 12, "bold")).pack(pady=10)
    
    progress2 = ttk.Progressbar(root, orient=HORIZONTAL, length=300, mode='indeterminate')
    progress2.pack(pady=5)
    
    # Progressbar operations
    def start_determinate():
        progress1['maximum'] = 100
        progress1['value'] = 0
        for i in range(101):
            progress1['value'] = i
            root.update()
            root.after(50)  # 50ms delay
    
    def start_indeterminate():
        progress2.start(10)  # 10ms interval
    
    def stop_indeterminate():
        progress2.stop()
    
    def reset_all():
        progress1['value'] = 0
        progress2.stop()
    
    # Buttons
    btn_frame = Frame(root)
    btn_frame.pack(pady=20)
    
    Button(btn_frame, text="Start Determinate", command=start_determinate).pack(side=LEFT, padx=5)
    Button(btn_frame, text="Start Indeterminate", command=start_indeterminate).pack(side=LEFT, padx=5)
    Button(btn_frame, text="Stop Indeterminate", command=stop_indeterminate).pack(side=LEFT, padx=5)
    Button(btn_frame, text="Reset All", command=reset_all).pack(side=LEFT, padx=5)
    
    # Variable progressbar
    Label(root, text="Variable Progressbar:", font=("Arial", 12, "bold")).pack(pady=10)
    
    progress_var = DoubleVar()
    progress3 = ttk.Progressbar(root, orient=HORIZONTAL, length=300, 
                               mode='determinate', variable=progress_var)
    progress3.pack(pady=5)
    
    scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, 
                 variable=progress_var, showvalue=True)
    scale.pack(pady=10)
    
    root.mainloop()

progressbar_demo()

#combobox_demo()

#listbox_demo()

#radiobutton_demo()

#text_widget_demo()

