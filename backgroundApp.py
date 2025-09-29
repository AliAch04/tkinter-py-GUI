import threading
import time
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import random

class BackgroundApp:
    def __init__(self, root):
        self.root = root
        self.running = True
        self.error_count = 0
        
        # Configuration de l'interface
        self.setup_gui()
        
        # Démarrer les threads
        #self.start_threads()
    
    def setup_gui(self):
        """Configure l'interface graphique"""
        self.root.title("Application Background + Tkinter")
        self.root.geometry("400x300")
        
        # Frame principal
        main_frame = tk.Frame(self.root, 
                              padx=20, 
                              pady=20, 
                              highlightthickness=2,
                              highlightbackground="#B8AC72",
                              highlightcolor="#FFE76E")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Titre
        title_label = tk.Label(main_frame, text="Application en Arrière-plan", 
                              font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Statut
        self.status_label = tk.Label(main_frame, text="🟢 Application en cours d'exécution", 
                                    font=("Arial", 12), fg="green")
        self.status_label.pack(pady=5)
        
        # Compteur d'erreurs
        self.error_label = tk.Label(main_frame, text="Erreurs affichées: 0", 
                                   font=("Arial", 10))
        self.error_label.pack(pady=5)
        
        # Log des activités
        log_frame = tk.Frame(main_frame, 
                             highlightthickness=2,  # border thickness
                             highlightbackground="#ff8a8a",  # Border color (not focused),
                             highlightcolor="#fc4c4c")
        
        log_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        tk.Label(log_frame, text="Journal d'activité:", font=("Arial", 10, "bold")).pack(anchor="w")
        
        self.log_text = tk.Text(log_frame, height=8, width=50)
        scrollbar = tk.Scrollbar(log_frame, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=scrollbar.set)
        
        self.log_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Boutons de contrôle
        button_frame = tk.Frame(main_frame,
                                highlightthickness=1,
                                highlightbackground="#5a5c60")
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="Test Manuel", command=self.manual_test,
                 bg="lightblue").pack(side=tk.LEFT, padx=5, ipadx=5)
        
        tk.Button(button_frame, text="Arrêter", command=self.stop_app,
                 bg="lightcoral").pack(side=tk.LEFT, padx=5)
    
    def start_threads(self):
        pass
    
    def manual_test(self):
        print('Teste manualle activé! ')
    
    def stop_app(self):
        print('Application a été arretée proprement!')

def main():
    root = tk.Tk()
    app = BackgroundApp(root)
    
    # Gestion de la fermeture propre
    def on_closing():
        app.stop_app()
    
    # Quand on click sur la botton 'X' dans title bar de root (window) 
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()