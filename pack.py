import tkinter as tk
import ttkbootstrap as ttk
from tkinter import ttk as tkttk
import time

root = tk.Tk() 
root.title('Pack testing')
root.geometry('400x600')
root.configure(bg='#3f3547')

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
    main_frame_top = tk.Frame(root, bg='#3f3547')

    # Top Title Label
    canvas_top = tk.Canvas(main_frame_top, width=200, height=80, highlightthickness=0, bg="#3f3547")
    print('canvas top : ', canvas_top.winfo_class())
    start = time.perf_counter()
    rounded_rectangle(canvas_top, 0, 0, 200, 80, 25, fill="#ED9A41", target_corners='all')
    print(f'time execution of "rounded_rectangle": {time.perf_counter() - start:.6f}s')
    canvas_top.create_text(100, 40, anchor='c', text='Main Title', font=('Arial', 12, 'bold'), fill='white')

    # Main frame
    main_frame = tk.Frame(root, bg='#3f3547')

    # Sub frames
    frame_1 = tk.Frame(main_frame, bg='#564068')
    frame_2 = tk.Frame(main_frame, bg='#564068')
    frame_3 = tk.Frame(main_frame, bg='#564068')


    # 1st section
    # widgets
    title_frame = tk.Frame(frame_1, bg='#564068')
    radio_frame = tk.Frame(frame_1, bg='#564068')

    # Title
    canvas_title = tk.Canvas(title_frame, width=160, height=30, highlightthickness=0, bg=title_frame['bg'])
    rounded_rectangle(canvas_title, 0,0,160,30, 25, fill="#CF934F", target_corners ='bottom' ,width=0)
    canvas_title.create_text(80, 15, anchor='c', text='1st Section', font=('Arial', 10, 'bold'), fill='white')

    # Radio Buttons
    category_value = tk.StringVar(value='DAY')

    def update_radio_colors(*args):
        radios = [
            (radio_1, 'DAY'),
            (radio_2, 'WEEK'),
            (radio_3, 'MONTH')
        ]
        
        for radio, value in radios:
            if category_value.get() == value:
                radio.config(selectcolor='#CF934F')
                print(category_value.get())
            else:
                radio.config(selectcolor='white')

    radio_1 = tk.Radiobutton(
        radio_frame, 
        text='Day',  
        variable=category_value, 
        value='DAY', 
        bg='#564068',  
        fg='white', 
        selectcolor='white',  
        activebackground='#3f3547', 
        activeforeground='white',
        highlightthickness=0,
        command=update_radio_colors  
    )

    radio_2 = tk.Radiobutton(
        radio_frame, 
        text='Week',  
        variable=category_value, 
        value='WEEK', 
        bg='#564068', 
        fg='white', 
        selectcolor='white',  
        activebackground='#3f3547', 
        activeforeground='white',
        highlightthickness=0,
        command=update_radio_colors
    )

    radio_3 = tk.Radiobutton(
        radio_frame, 
        text='Month',  
        variable=category_value, 
        value='MONTH', 
        bg='#564068', 
        fg='white', 
        selectcolor='white', 
        activebackground='#3f3547', 
        activeforeground='white',
        highlightthickness=0,
        command=update_radio_colors
    )
    # set the initial value (DAY)
    update_radio_colors()

    # Trace the change of the variable (automatic update)
    #category_value.trace_add('write', update_radio_colors)

    # Layout 1st Section
    canvas_title.pack(side='top')
    title_frame.pack(side='top', fill='x')

    radio_1.pack(side='left', expand=True, fill='both')
    radio_2.pack(side='left', expand=True, fill='both')
    radio_3.pack(side='left', expand=True, fill='both')
    radio_frame.pack(side='bottom', expand=True, fill='x')

    # 2nd section
    # widgets
    title_frame_2 = tk.Frame(frame_2, bg='#564068')
    scale_frame = tk.Frame(frame_2, bg='#564068')

    # Title
    canvas_title_2 = ttk.Canvas(title_frame_2, width=160, height=30, highlightthickness=0, bg=title_frame_2['bg'])
    rounded_rectangle(canvas_title_2, 0,0,160,30, 25, fill="#CF934F", target_corners ='bottom' ,width=0)
    canvas_title_2.create_text(80, 15, anchor='c', text='2nd Section', font=('Arial', 10, 'bold'), fill='white')

    # Variables
    scale_float_value = tk.DoubleVar(value=10)
    entry_string_value = tk.StringVar(value="10")
    is_setting_entry_value = False 

    def update_entry_from_scale(event=None):
        # Reject updating the scale when entry is modifing
        nonlocal is_setting_entry_value 
        if is_setting_entry_value:
            return
        float_val = scale_float_value.get()
        int_val = int(float_val) 
        is_setting_entry_value = True

        entry_string_value.set(str(int_val))
        is_setting_entry_value = False
    
    def update_scale_from_entry(*args):
        #print(f'the key released : {args[0].keysym}')
        nonlocal is_setting_entry_value

        # Handle the infinite loop when .set() is called
        if is_setting_entry_value:
            return
        
        # Handle none numerical input 
        try:
            entry_val_str = entry_string_value.get()

            # Handle Empty input
            if not entry_val_str:
                scale_float_value.set(0)
                return
            
            new_int_val = int(entry_val_str)
            # Clamped the value to the bounds (0, 100)
            val_clamped = max(0, min(100, new_int_val))

            scale_float_value.set(val_clamped)

            # Handle entry input loop error
            if str(val_clamped) != entry_string_value:
                is_setting_entry_value = True
                entry_string_value.set(str(val_clamped))
                is_setting_entry_value = False 

        except ValueError:
            print('Only numerical values')
    
    def update_label(*args):
        log_input.config(text=f'You will be notified {entry_string_value.get()} every {category_value.get()}')

    scale = tk.Scale(scale_frame, from_=0, to=100, orient='horizontal', highlightthickness=0, borderwidth=0, sliderrelief='flat', sliderlength=20, showvalue= False, bg='#CF934F', troughcolor='#3f3547',activebackground='#ED9A41', variable=scale_float_value )
    entry_scale = tk.Entry(scale_frame, 
                           width=5, 
                           textvariable=entry_string_value,
                           bg='#3f3547',           
                           fg='white',
                            insertbackground='white',
                            relief='flat',
                            borderwidth=2,          
                            highlightthickness=1,   
                            highlightbackground='#564068',  
                            highlightcolor='#CF934F',  
                            justify='center' )
    log_input = tk.Label(frame_2, text=f'You will be notified {entry_string_value.get()} every {category_value.get()}', fg='white', bg='#564068')
    
    # Automatique log update when variable changing 
    entry_string_value.trace_add('write', update_label)
    category_value.trace_add('write', update_label)

    # Bind scale when is in motion (drag it)
    scale.bind('<Motion>', update_entry_from_scale) 

    # Bind entry when is typing
    entry_scale.bind('<Key>', update_scale_from_entry) 
    scale.pack(pady=10, fill='x')

    # Layout 2nd Section
    canvas_title_2.pack(side='top')
    title_frame_2.pack(side='top', fill='x')
    scale_frame.pack(side='top', expand=True, fill='x')

    scale.pack(side='left', expand=True, fill='both')
    entry_scale.pack(side='left')
    log_input.pack(side='top', expand=True)

    entry_string_value.trace_add('write', update_scale_from_entry)
    update_entry_from_scale(None)

    # 3rd section
    # widgets
    buttons_frame = tk.Frame(frame_3, bg='#564068')

    def submit_fct(*args):
        pass
    
    # Buttons
    submit = tk.Button(
        buttons_frame,
        activebackground='#ED9A41',
        activeforeground='#cccccc', 
        text='Submit',  
        bg='#CF934F',  
        fg='white', 
        relief='flat',
        overrelief='ridge',
        highlightthickness=0,
        command=submit_fct  
    )

    # Layout 3st Section
    buttons_frame.pack(expand=True, fill='x')

    submit.pack(ipadx=10, ipady=0)


    # Layout
    main_frame_top.pack(side='top',fill='both')
    canvas_top.pack(side='top', pady=20)
    main_frame.pack(side='top', fill=tk.BOTH, expand=True)
    frame_1.pack(side='top', expand=True, fill='both', padx=10, pady=(10,0))
    frame_2.pack(side='top', expand=True, fill='both', padx=10, pady=(10,0))
    frame_3.pack(side='top', expand=True, fill='both', padx=10, pady=(10,10))

    root.mainloop()

if __name__ == '__main__':
    main()