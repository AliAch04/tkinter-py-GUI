import tkinter as tk
import random
import time

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

    # Early return if not target_corners
    target_corners = kwargs.pop('target_corners', None)

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

    # Top Title Label
    canvas_top = tk.Canvas(root, width=200, height=80, highlightthickness=0)
    start = time.perf_counter()
    rounded_rectangle(canvas_top, 0,0,200,75, 25, fill='red', target_corners ='right' , outline='')
    print(f'time execution : {time.perf_counter() - start:.6f}s')

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