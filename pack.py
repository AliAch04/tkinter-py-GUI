import tkinter as tk
import random

root = tk.Tk()
root.title('Pack testing')
root.geometry('400x600')

clicked = False

def click():
    global root, clicked

    if not clicked:
        x = random.randint(0,1050)
        y = random.randint(0,100)
        root.geometry(f'600x400+{x}+{y}')
        print(f'Random num is : ({x}, {y})')
        clicked = True
    else:
        x = random.randint(0,450)
        y = random.randint(0,100)
        root.geometry(f'400x600+{x}+{y}')
        print(f'Random num is : ({x}, {y})')
        clicked = False


def main():
    # Widgets
    global root
    # Frame - top
    
    label1 = tk.Label(root, text='lable1', bg='red')
    label2 = tk.Label(root, text='lable2', bg='blue')
    label3 = tk.Label(root, text='lable3', bg='green')
    label4 = tk.Label(root, text='lable4', bg='cyan')
    button = tk.Button(root, text='Button', command=click)

    # Layout
    label1.pack(side='top', expand=True, fill='both')
    label2.pack(side='top', expand=True, fill='both')
    label3.pack(side='left', expand=True, fill='both')
    button.pack(side='left', expand=True, fill='both')
    label4.pack(side='top', expand=True, fill='both')

    root.mainloop()

if __name__ == '__main__':
    main()