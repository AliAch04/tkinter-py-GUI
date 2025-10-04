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

def rounded_rectangle(canvas, x1, y1, x2, y2, r=25, **kwargs):
    x2_y1_t_r_1 = x2_y1_t_r_2 = x2_y2_b_r_1 = x2_y2_b_r_2 = x1_y2_b_l_1 = x1_y2_b_l_2 = x1_y1_t_l_1 = x1_y1_t_l_2 = None

    if 'target_corners' in kwargs:
        # Extract wanted corners (has to be seperated by '|') example of the input : 'top-left|top-right'
        corners = kwargs['target_corners'].split('|')
        print(f'corners wanted: {corners}')

        # Assign wanted corners to the appropriate variable
        for corner in corners:
            if 'top-right' == corner:
                x2_y1_t_r_1, x2_y1_t_r_2 = (x2-r, y1), (x2, y1+r)
                print(f'corner to be curve: {corner}')
            if 'buttom-right' == corner:
                x2_y2_b_r_1, x2_y2_b_r_2 = (x2-r, y2), (x2, y2-r)
                print(f'corner to be curve: {corner}')
            if 'buttom-left' == corner:
                x1_y2_b_l_1, x1_y2_b_l_2 = (x1+r, y2), (x1, y2-r)
                print(f'corner to be curve: {corner}')
            if 'top-left' == corner:
                x1_y1_t_l_1, x1_y1_t_l_2 = (x1-r, y1), (x1, y1+r)
                print(f'corner to be curve: {corner}')
        
        # Assign the control point duplication to the appropriate variable
        if x2_y1_t_r_1 ==None and  x2_y1_t_r_2 == None:
            x2_y1_t_r_1, x2_y1_t_r_2 = x2, y1
        
        if x2_y2_b_r_1 ==None and  x2_y2_b_r_2 == None:
            x2_y2_b_r_1, x2_y2_b_r_2 = x2, y2

        if x1_y2_b_l_1 ==None and  x1_y2_b_l_2 == None:
            x1_y2_b_l_1, x1_y2_b_l_2 = x1, y2

        if x1_y1_t_l_1 ==None and  x1_y1_t_l_2 == None:
            x1_y1_t_l_1, x1_y1_t_l_2 = x1, y1

        # Delete the added argument
        del kwargs['target_corners']

    else:
        print('No corner selected') 
        # Assign Appropriat variable to achive normal curve for all corners
        x2_y1_t_r_1, x2_y1_t_r_2 = (x2-r, y1), (x2, y1+r)
        x2_y2_b_r_1, x2_y2_b_r_2 = (x2-r, y2), (x2, y2-r)
        x1_y2_b_l_1, x1_y2_b_l_2 = (x1+r, y2), (x1, y2-r)
        x1_y1_t_l_1, x1_y1_t_l_2 = (x1-r, y1), (x1, y1+r)
        
    points = [
        x2, y1,
        x2_y1_t_r_1, x2_y1_t_r_2,
        
        x2, y2,
        x2_y2_b_r_1, x2_y2_b_r_2,

        x1, y2,
        x1_y2_b_l_1, x1_y2_b_l_2,
        
        x1, y1,
        x1_y1_t_l_1, x1_y1_t_l_2,
    ]

    return canvas.create_polygon(points, smooth=True, **kwargs)


def main():
    global root

    # Top Title Label
    canvas_top = tk.Canvas(root, width=200, height=80, highlightthickness=0)
    rounded_rectangle(canvas_top, 0,0,200,75, 25, target_corners='top-left', fill='red', outline='')
    canvas_top.create_text(100, 40, anchor='c', text='Main Title', font=('Arial', 12, 'bold'), fill='white')

    # Main frame
    main_frame = tk.Frame(root)

    # Sub frames
    frame_1 = tk.Frame(main_frame, bg='blue')
    frame_2 = tk.Frame(main_frame, bg='cyan')
    frame_3 = tk.Frame(main_frame, bg='purple')

    

    # Layout
    canvas_top.pack(side='top', pady=20)
    main_frame.pack(side='top', fill=tk.BOTH, expand=True)
    frame_1.pack(side='top', expand=True, fill='both', padx=10, pady=(10,0))
    frame_2.pack(side='top', expand=True, fill='both', padx=10, pady=(10,0))
    frame_3.pack(side='top', expand=True, fill='both', padx=10, pady=(10,10))


    root.mainloop()

if __name__ == '__main__':
    main()