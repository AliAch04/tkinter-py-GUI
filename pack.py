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
    points =[]
    
    if 'target_corners' in kwargs:
        # Extract wanted corners (has to be seperated by '|') example of the input : 'top-left|top-right'
        corners = kwargs['target_corners'].split('|')
        print(f'corners wanted: {corners}')

        # Config of each rounded corner
        corners_config = {
            'top-left' : [x1+r, y1, x1, y1+r],
            'top-right' : [x2-r, y1, x2, y1+r],
            'bottom-right': [x2-r, y2, x2, y2-r],
            'bottom-left' : [x1+r, y2, x1, y2-r]
        }

        # Default corners
        corners_default = {
            'top-left' : [x1, y1, x1, y1],
            'top-right' : [x2, y1, x2, y1],
            'bottom-right': [x2, y2, x2, y2],
            'bottom-left' : [x1, y2, x1, y2]
        }

        # Assign with correct ordre
        for corner in ['top-left', 'top-right', 'bottom-right', 'bottom-left']:
            if corner in corners:
                points.extend(corners_config[corner])
            else:
                points.extend(corners_default[corner])
        
        print(f'points = {points}')
        
        del kwargs['target_corners']
    else:
        print('No corner Select - Normal rectangle') 
        points.extend(
            [
            x2, y1,
            x2, y1,

            x2, y2,
            x2, y2,

            x1, y2,
            x1, y2,

            x1, y1,
            x1, y1]
        )
        
    return canvas.create_polygon(points, smooth=True, **kwargs)


def main():
    global root

    # Top Title Label
    canvas_top = tk.Canvas(root, width=200, height=80, highlightthickness=0)
    rounded_rectangle(canvas_top, 0,0,200,75, 25, fill='red', target_corners ='top-left|bottom-right' , outline='')
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