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
        self.root.geometry("600x500")
        
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
        
    def log_message(self, msg):
        '''Ajouter un message au journal (log_text)'''
        time_stamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
        entry_log = self.log_text.insert(tk.END, f' {time_stamp} , {msg} ')

    def show_error_message(self):
        '''Afficher un erreur aléatoire dans boite de dialog'''
        errors = ['erreur1', 'erreur2', 'erreur3', 'erreur4', 'erreur5', 'erreur6']

        err_choise = random.choice(errors)
        self.error_count += 1

        # Afficher le msg en boite dialog
        messagebox.showerror('Erreur Système', err_choise)

        # MAJ et afficher le conteur
        self.error_label.config(text=f"Erreurs affichées: {self.error_count}")

        # Affirmer dans le journal
        self.log_text.insert(tk.END, f'Erreur : "{err_choise}" ')
        self.log_text.see(tk.END)


        
    def background_worker_1(self):
        """1er background qui génére des erreurs chaque 5 seconds"""
        self.log_message('Thread d\'erreur démarré')

        while self.running == True:
            # ajouter try/except 
            self.show_error_message()

            for i in range(50):
                if not self.running:
                    break
                time.sleep(0.1)

    def background_worker_2(self):
        """2er background qui génére des erreurs chaque 10 seconds"""
        self.log_message('Thread d\'erreur démarré')

        while self.running == True:
            # ajouter try/except 
            self.show_error_message()

            for i in range(100):
                if not self.running:
                    break
                time.sleep(0.1)
    
    def start_threads(self):
        """Démarrer la totalités des threads"""
        # Creation des threads
        self.background_thread_1 = threading.Thread(target=self.background_worker_1, daemon=True)
        self.background_thread_2 = threading.Thread(target=self.background_worker_2, daemon=True)

        # Demarrage des threads
        self.background_thread_1.start()
        self.background_thread_2.start()

        self.log_message('Tous les threads demarrés')


    
    def manual_test(self):
        """Tester manuellement des threats (erreurs)"""
        self.show_error_message()
        self.log_message(" -- Test manuel déclenché!")
    
    def stop_app(self):
        """Arreter l'app proprement"""
        self.running = False
        self.status_label.config(text='Application en cours de fermeture...', fg='red')

        self.root.after(1500, self.root.destroy)
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