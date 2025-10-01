import tkinter as tk

class NotificationApp:
    def __init__(self, root):
        self.root = root

        self.start_gui()

    def start_gui(self):
        self.root.title('Notification App v1')
        self.root.geometry('750x600')

        # Rounded edge courner
        canvas = tk.Canvas(self.root, width=300, height=100, highlightthickness=0)
        canvas.pack()
        self.create_rounded_rectangle(canvas, 10, 10, 290, 90, r=25, fill='#556677')
        canvas.create_text(150, 50, text="Pray Time", fill='white', font=('Arial', 12))
    
    def create_rounded_rectangle(self, canvas, x1, y1, x2, y2, r=20, **kwargs):
        points = [
            x1 +r, y1,
            x2 -r, y1,
            x2, y1,

            x2, y1 +r,
            x2, y2- r,
            x2, y2,

            x2 -r, y2,
            x1 +r, y2,
            x1, y2,

            x1, y2 -r,
            x1, y1 +r,
            x1, y1,
        ]

        return canvas.create_polygon(points, **kwargs, smooth=True)
    

def main():
    root = tk.Tk()
    app = NotificationApp(root)

    def on_delete():
        print('delete window')
        root.destroy()

    root.protocol('WM_DELETE_WINDOW', on_delete)

    root.mainloop()

if __name__ == '__main__':
    main()


    