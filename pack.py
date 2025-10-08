import tkinter as tk
import ttkbootstrap as ttk
import random
import time

root = ttk.Window() 
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

def rounded_rectangle(canvas, x1, y1, x2, y2, r=25, **kwargs):
    """
    Draw a rounded rectangle on a tkinter canvas with customizable corner rounding.
    
    Parameters:
    -----------
    canvas : tkinter.Canvas
        The canvas widget to draw on
    x1, y1 : int
        Top-left coordinates of the rectangle
    x2, y2 : int
        Bottom-right coordinates of the rectangle
    r : int, optional
        Radius of the rounded corners (default: 25)
    **kwargs : dict
        Additional arguments passed to canvas.create_polygon()
        Special keyword:
            target_corners (str): Pipe-separated string specifying which corners to round.
                                 Options: 'top-left', 'top-right', 'bottom-left', 'bottom-right',
                                 'all', 'top', 'bottom', 'left', 'right'
                                 Example: 'top-left|top-right' or 'bottom'
    
    Returns:
    --------
    int
        The canvas item ID of the created polygon
    
    Examples:
    ---------
    # Round only top corners
    rounded_rectangle(canvas, 10, 10, 200, 100, r=20, target_corners='top', fill='blue')
    
    # Round specific corners
    rounded_rectangle(canvas, 10, 10, 200, 100, target_corners='top-left|bottom-right')
    
    # Round all corners
    rounded_rectangle(canvas, 10, 10, 200, 100, target_corners='all')
    """
    # Early return if not target_corners
    target_corners = kwargs.pop('target_corners', None)

    if 'outline' not in kwargs and 'fill' in kwargs:
        kwargs['outline'] = kwargs['fill']

    if not target_corners:
        points = [x2, y1, x2, y1, x2, y2, x2, y2, x1, y2, x1, y2, x1, y1, x1, y1]
        return canvas.create_polygon(points, smooth=True, **kwargs)
    
    # Config of each rounded corner
    corners_config = {
        'top-left': (x1, y1+r, x1, y1, x1+r, y1),
        'top-right': (x2-r, y1, x2, y1, x2, y1+r),
        'bottom-right': (x2, y2-r, x2, y2, x2-r, y2),
        'bottom-left': (x1+r, y2, x1, y2, x1, y2-r)
    }
    
    corners_default = {
        'top-left': (x1, y1, x1, y1),
        'top-right': (x2, y1, x2, y1),
        'bottom-right': (x2, y2, x2, y2),
        'bottom-left': (x1, y2, x1, y2)
    }

    # Pre-parser the corners
    corners_set = set(target_corners.split('|'))
    is_all = 'all' in corners_set

    # Precalculate complexes conditions
    edge_map = {
        'top': {'top-left', 'top-right'},
        'bottom': {'bottom-left', 'bottom-right'},
        'left': {'top-left', 'bottom-left'},
        'right': {'top-right', 'bottom-right'}
    }

    # Expand corners_set
    for edge, edge_corners in edge_map.items():
        if edge in corners_set:
            corners_set.update(edge_corners)
    
    points = []
    for corner in ['top-left', 'top-right', 'bottom-right', 'bottom-left']:
        if is_all or corner in corners_set:
            points.extend(corners_config[corner])
        else:
            points.extend(corners_default[corner])
    
    return canvas.create_polygon(points, smooth=True, **kwargs)


def main():
    global root

    # Style
    style = ttk.Style()
    # Main Frames
    style.configure(
        'TFrame', 
        background="#3f3547", 
    )
    # Sub Frames
    style.configure(
        'Sub.TFrame', 
        background="#564068", 
    )
    # Standard widgets
    style.configure(
        'TRadiobutton', 
        background="#564068", 
        foreground='white'
    )
    style.configure(
        'TScale', 
        background="#564068", 
    )
    


    main_frame_top = ttk.Frame(root)

    # Top Title Label
    canvas_top = tk.Canvas(main_frame_top, width=200, height=80, highlightthickness=0, bg="#3f3547")
    start = time.perf_counter()
    rounded_rectangle(canvas_top, 0,0,200,75, 25, fill="#ED9A41", target_corners ='all' )
    print(f'time execution : {time.perf_counter() - start:.6f}s')

    canvas_top.create_text(100, 40, anchor='c', text='Main Title', font=('Arial', 12, 'bold'), fill='white')


    # Main frame
    main_frame = ttk.Frame(root, style='TFrame')

    # Sub frames
    frame_1 = ttk.Frame(main_frame, style='Sub.TFrame')
    frame_2 = ttk.Frame(main_frame, style='Sub.TFrame')
    frame_3 = ttk.Frame(main_frame, style='Sub.TFrame')


    # 1st section
    # widgets
    title_frame = ttk.Frame(frame_1, style='Sub.TFrame')
    radio_frame = ttk.Frame(frame_1, style='Sub.TFrame')

    # Title
    canvas_title = tk.Canvas(title_frame, width=160, height=30, highlightthickness=0, bg="#3f3547")
    rounded_rectangle(canvas_title, 0,0,160,30, 20, fill="#CF934F", target_corners ='bottom' ,width=0)
    canvas_title.create_text(80, 15, anchor='c', text='1st Section', font=('Arial', 10, 'bold'), fill='white')

    # Radio Buttons
    category_value = tk.StringVar(value='DAY')

    def show_input_radio():
        print(category_value.get())

    radio_1 = ttk.Radiobutton(radio_frame, text='Day', bootstyle="info", variable=category_value, value='DAY', )
    radio_2 = ttk.Radiobutton(radio_frame, text='Week', bootstyle="info", variable=category_value, value='WEEK', )
    radio_3 = ttk.Radiobutton(radio_frame, text='Month', bootstyle="info", variable=category_value, value='MONTH', )
    btn = ttk.Button(radio_frame, text='click', command=show_input_radio, bootstyle="success")

    # Layout 1st Section
    canvas_title.pack(side='top')
    title_frame.pack(side='top', fill='x')

    radio_1.pack(side='left', expand=True, fill='both')
    radio_2.pack(side='left', expand=True, fill='both')
    radio_3.pack(side='left', expand=True, fill='both')
    radio_frame.pack(side='bottom', expand=True, fill='x')
    btn.pack()

    # 2nd section
    # widgets
    title_frame_2 = ttk.Frame(frame_2, style='Sub.TFrame')
    scale_frame = ttk.Frame(frame_2, style='Sub.TFrame')

    # Title
    canvas_title_2 = ttk.Canvas(title_frame_2, width=160, height=30, highlightthickness=0, bg="#3f3547")
    rounded_rectangle(canvas_title_2, 0,0,160,30, 20, fill="#CF934F", target_corners ='bottom' ,width=0)
    canvas_title_2.create_text(80, 15, anchor='c', text='2nd Section', font=('Arial', 10, 'bold'), fill='white')

    # Button
    scale_float_value = tk.DoubleVar(value=10)
    entry_string_value = tk.StringVar(value="10")

    def update_entry_from_scale(event=None):
        float_val = scale_float_value.get()
        int_val = int(float_val) 
        entry_string_value.set(str(int_val))
    
    def update_scale_from_entry(*args):
        #print(f'the key released : {args[0].keysym}')
        # Handle none numerical input 
        try:
            entry_val_str = entry_string_value.get()

            # Handle Empty input
            if not entry_val_str:
                return
            
            new_int_val = int(entry_val_str)
            # Clamped the value to the bounds (0, 100)
            val_clamped = max(0, min(100, new_int_val))

            scale_float_value.set(val_clamped)

            
        
        except ValueError:
            print('Only numerical values')


    def show_input_scale():
        print(entry_string_value.get())

    scale = ttk.Scale(scale_frame, bootstyle="info", from_=0, to=100, variable=scale_float_value )
    entry_scale = ttk.Entry(scale_frame, bootstyle="info", width=5, textvariable=entry_string_value)
    btn_scale = ttk.Button(scale_frame, text='click', command=show_input_scale, bootstyle="success")

    # Bind scale when is in motion (drag it)
    scale.bind('<Motion>', update_entry_from_scale) 

    entry_scale.bind('<Key>', update_scale_from_entry) 
    scale.pack(pady=10, fill='x')

    # Layout 2nd Section
    canvas_title_2.pack(side='top')
    title_frame_2.pack(side='top', fill='x')
    scale.pack(side='left', expand=True, fill='both')
    entry_scale.pack(side='left')
    scale_frame.pack(side='bottom', expand=True, fill='x')
    btn_scale.pack()

    callback_id = entry_string_value.trace_add('write', update_scale_from_entry)
    update_entry_from_scale(None)

    # Layout
    main_frame_top.pack(side='top',fill='both')
    canvas_top.pack(side='top', pady=20)
    main_frame.pack(side='top', fill=tk.BOTH, expand=True)
    frame_1.pack(side='top', expand=True, fill='both', padx=10, pady=(10,0))
    frame_2.pack(side='top', expand=True, fill='both', padx=10, pady=(10,0))
    frame_3.pack(side='top', expand=True, fill='both', padx=10, pady=(10,10))

    print('value is : ', category_value.get())


    root.mainloop()

if __name__ == '__main__':
    main()