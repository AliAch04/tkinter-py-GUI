from tkinter import *

def entry_bindings_demo():
    root = Tk()
    root.title("Entry Bindings and Validation")
    root.geometry("500x400")
    
    # Entry with various bindings
    entry = Entry(root, font=("Arial", 14), width=30)
    entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    
    # Display area for events
    event_display = Text(root, height=15, width=50)
    event_display.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    
    def log_event(event=None):
        event_display.insert(END, f"Event: {event.type} | Key: {event.keysym} | Char: {event.char} | Widget: {event.widget}\n")
        event_display.see(END)
    
    def log_focus(event):
        event_display.insert(END, f"Focus: {event.type} - Widget {'gained' if event.type == '9' else 'lost'} focus\n")
        event_display.see(END)
    
    # Key bindings
    entry.bind("<KeyPress>", log_event)          # Any key press
    entry.bind("<KeyRelease>", log_event)        # Any key release
    entry.bind("<Return>", lambda e: log_event(e) or print("Enter pressed!"))  # Enter key
    entry.bind("<FocusIn>", log_focus)           # Gained focus
    entry.bind("<FocusOut>", log_focus)          # Lost focus
    
    # Mouse bindings
    entry.bind("<Button-1>", lambda e: event_display.insert(END, "Mouse click in entry\n"))
    entry.bind("<Double-Button-1>", lambda e: event_display.insert(END, "Double click in entry\n"))
    
    # Special key combinations
    entry.bind("<Control-c>", lambda e: event_display.insert(END, "Ctrl+C pressed\n"))
    entry.bind("<Control-v>", lambda e: event_display.insert(END, "Ctrl+V pressed\n"))
    entry.bind("<Control-a>", lambda e: event_display.insert(END, "Ctrl+A pressed\n"))
    
    # Validation function
    def validate_input(char):
        if char.isdigit() or char == "":
            return True
        else:
            event_display.insert(END, "Validation: Only digits allowed!\n")
            event_display.see(END)
            return False
    
    # Validated entry (only numbers)
    Label(root, text="Numbers only:").grid(row=2, column=0, sticky="w", pady=5)
    validated_entry = Entry(root, font=("Arial", 14), width=30)
    validated_entry.grid(row=3, column=0, padx=10, pady=5, sticky="ew")
    
    # Register validation command
    vcmd = (root.register(validate_input), '%S')
    validated_entry.config(validate="key", validatecommand=vcmd)
    
    def clear_display():
        event_display.delete(1.0, END)
    
    Button(root, text="Clear Events", command=clear_display).grid(row=4, column=0, pady=10)
    
    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)
    
    root.mainloop()

entry_bindings_demo()