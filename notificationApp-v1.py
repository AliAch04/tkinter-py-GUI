import tkinter as tk
from tkinter import ttk

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

        # Main Frame
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Period Section
        period_frame = tk.Frame(main_frame, bg="#0077FF", borderwidth=5)
        period_frame.pack(fill=tk.X, side='top', expand=True)

        # Period title
        period_title_frame = tk.Frame(period_frame, bg=period_frame['bg'])
        period_title_frame.pack(fill=tk.X)

        # Canvas avec fond transparent (couleur du parent)
        canvas_period = tk.Canvas(period_title_frame, width=200, height=70, 
                                highlightthickness=0, bg=period_title_frame['bg'])
        canvas_period.pack(pady=5)

        # Rectangle pour la bordure
        self.create_rounded_rectangle(canvas_period, 0, 0, 200, 70, r=25, 
                             fill='#7b7b6a', outline='')  
        # Rectangle pour le fond
        self.create_rounded_rectangle(canvas_period, 3, 3, 197, 67, r=23, 
                                    fill='#a28a55', outline='')   

        canvas_period.create_text(100, 35, text='Choise Period', 
                                fill='white', font=('Arial', 10, 'bold'), 
                                anchor='center')

        # Period Section Options
        period_radio_frame = tk.Frame(period_frame, bg=period_frame['bg'])
        period_radio_frame.pack(anchor='n', fill=tk.X, expand=True, pady=(20,0))

        period_value = tk.StringVar(value='DAY')

        radio1_period = ttk.Radiobutton(period_radio_frame, text='Day', variable=period_value, value='DAY')
        radio2_period = ttk.Radiobutton(period_radio_frame, text='Week', variable=period_value, value='WEEK')
        radio3_period = ttk.Radiobutton(period_radio_frame, text='Month', variable=period_value, value='MONTH')

        radio1_period.pack(side='left', expand=True)
        radio2_period.pack(side='left', expand=True)
        radio3_period.pack(side='left', expand=True)

        # Density Section
        density_frame = tk.Frame(main_frame, bg="#B1CA8B")
        density_frame.pack(fill=tk.BOTH, expand=True)

        # Density title
        density_title_frame = tk.Frame(density_frame, bg="#6E7761")
        density_title_frame.pack(fill=tk.X)

        # Canvas avec fond transparent (couleur du parent)
        canvas_density = tk.Canvas(density_title_frame, width=200, height=70, 
                                highlightthickness=0, bg=period_title_frame['bg'])
        canvas_density.pack(pady=5)

        # Rectangle pour la bordure
        self.create_rounded_rectangle(canvas_density, 0, 0, 200, 70, r=25, 
                             fill='#7b7b6a', outline='')  
        # Rectangle pour le fond
        self.create_rounded_rectangle(canvas_density, 3, 3, 197, 67, r=23, 
                                    fill='#a28a55', outline='')   

        canvas_density.create_text(100, 35, text='Density', 
                                fill='white', font=('Arial', 10, 'bold'), 
                                anchor='center')
        
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


    