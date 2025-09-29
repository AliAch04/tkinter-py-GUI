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
        self.thread_count = 0
        self.active_threads = [] 
        
        # Configuration de l'interface
        self.setup_gui()
        
        # Démarrer les threads
        self.start_threads()
    
    def setup_gui(self):
        """Configure l'interface graphique"""
        self.root.title("Application Background + Tkinter")
        self.root.geometry("650x550") 
        
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
        self.status_label = tk.Label(main_frame, text="Application en cours d'exécution", 
                                    font=("Arial", 12), fg="green")
        self.status_label.pack(pady=5)

        # Compteur de threads 
        self.thread_label = tk.Label(main_frame, text="Threads en cours : 0", 
                                    font=("Arial", 11))
        self.thread_label.pack(pady=5)
        
        # Compteur d'erreurs
        self.error_label = tk.Label(main_frame, text="Erreurs affichées: 0", 
                                   font=("Arial", 10))
        self.error_label.pack(pady=5)
        
        # Log des activités
        log_frame = tk.Frame(main_frame, 
                             highlightthickness=2,
                             highlightbackground="#ff8a8a",
                             highlightcolor="#fc4c4c")
        log_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        tk.Label(log_frame, text="📝 Journal d'activité:", font=("Arial", 10, "bold")).pack(anchor="w")
        
        self.log_text = tk.Text(log_frame, 
                               wrap='word', 
                               height=12,           
                               width=60,            
                               font=("Consolas", 9), 
                               bg="#f8f9fa",        
                               relief="solid",      
                               bd=1)
        
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
                 bg="#4CAF50", fg="white", padx=10).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Démarrer Thread Test", command=self.demarrer_thread,
                 bg="#2196F3", fg="white", padx=10).pack(side=tk.LEFT, padx=5)
        
        tk.Button(button_frame, text="Arrêter", command=self.stop_app,
                 bg="#f44336", fg="white", padx=10).pack(side=tk.LEFT, padx=5)
        
        
    def log_message(self, msg, wait=False):
        '''Ajouter un message au journal (log_text)'''
        if not wait:
            time_stamp = datetime.now().strftime("%H:%M:%S")  
            entry_log = f"[{time_stamp}] {msg}\n" 

            # thread-safe
            self.root.after(0, self._update_log_text, entry_log, wait)
        else:
            # thread-safe
            self.root.after(0, self._update_log_text, entry_log, wait)

    
    def _update_log_text(self, log, wait=False):
        '''MAJ de log_text (Journal d'activité) d'une maniere thread-safe'''
        if not wait:
            self.log_text.insert(tk.END, log)
            self.log_text.see(tk.END)
        else:
            self.log_text.insert(tk.END, "placeholder")
            self.log_text.delete(self.log_text.index("end-1c line start"), tk.END)
            self.log_text.insert(tk.END, log)
            self.log_text.see(tk.END)
        
        # Limiter la taille du log pour une bonne usage de memoire
        lines = self.log_text.get(1.0, tk.END).split('\n')
        if len(lines) > 1000:  
            self.log_text.delete(1.0, f"{len(lines)-1000}.0")

    def show_error_message(self, thread_name="Général"):
        '''Afficher une erreur aléatoire dans boite de dialogue'''
        # Messages d'erreur plus descriptifs avec le préfixe de thread
        errors = [
            f"{thread_name}: Erreur de connexion réseau",
            f"{thread_name}: Mémoire insuffisante pour l'opération",
            f"{thread_name}: Fichier de configuration non trouvé", 
            f"{thread_name}: Timeout de la base de données",
            f"{thread_name}: Permission refusée sur le fichier",
            f"{thread_name}: Syntaxe invalide dans la requête"
        ]

        err_choix = random.choice(errors)
        self.error_count += 1

        self.root.after(0, self._display_error_message, err_choix, thread_name)

    def _display_error_message(self, err_msg, thread_name):
        '''Afficher la messagebox et mettre à jour l'interface'''
        messagebox.showerror('Erreur Système', err_msg)
        self._update_error_display(err_msg, thread_name)
    
    def _update_error_display(self, err_msg, thread_name):
        '''Afficher et MAJ les erreurs d'une maniere thread-safe'''

        # MAJ et afficher le compteur
        self.error_label.config(text=f"Erreurs affichées: {self.error_count}")

        log_entry = f"Erreur n°{self.error_count:03d} ({thread_name}): {err_msg}\n"
        self.log_text.insert(tk.END, log_entry)
        self.log_text.see(tk.END)

    def background_worker_1(self):
        """1er background qui génère des erreurs chaque 5 secondes"""
        thread_id = "Thread-1"
        self.log_message(f"{thread_id} démarré - active chaque 5s")
        
        self.root.after(0, self._update_thread_label)

        while self.running:
            try: 
                self.show_error_message(thread_id)

                for _ in range(50): 
                    if not self.running:
                        return  
                    time.sleep(0.1)

            except Exception as e:
                self.log_message(f'{thread_id}: Exception - {e}')
                time.sleep(5)

    def background_worker_2(self):
        """2ème background qui génère des erreurs chaque 10 secondes"""
        thread_id = "Thread-2"
        
        # Délai de 6 sconds
        time.sleep(6) 

        self.log_message(f"{thread_id} démarré - active chaque 10s")
        self.root.after(0, self._update_thread_label)

        while self.running:
            try:  
                self.show_error_message(thread_id)

                for _ in range(100):  
                    if not self.running:
                        return  
                    time.sleep(0.1)

            except Exception as e:
                self.log_message(f'{thread_id}: Exception - {e}')
                time.sleep(10)
    
    def _update_thread_label(self):
        '''MAJ thread counter et afficher le dans thread label'''
        self.thread_count += 1
        self.thread_label.config(text=f'Threads actifs : {self.thread_count}')
    
    def start_threads(self):
        """Démarrer la totalité des threads principaux"""
        # Journalisation du démarrage
        self.log_message("🚀 Démarrage des threads principaux...")
        
        # Création des threads
        self.background_thread_1 = threading.Thread(target=self.background_worker_1, daemon=True)
        self.background_thread_2 = threading.Thread(target=self.background_worker_2, daemon=True)

        # Démarrage des threads
        self.background_thread_1.start()
        self.background_thread_2.start()

        self.log_message("Tous les threads principaux démarrés\n")
    
    def test_thread(self):
        '''Fonction pour les threads Test supplémentaires'''
        thread_id = f"Test-{threading.current_thread().name}"

        # Délai aléatoire entre 1s et 3s avec animation
        delay = random.randint(1, 10)
        msg_demarrage = str(thread_id) + "en cours de démarrage"
        for i in range(delay):
            if msg_demarrage != str(thread_id) + "en cours de démarrage...":
                msg_demarrage += '.'
                self.log_message(msg_demarrage, True)
            else:
                msg_demarrage = str(thread_id) + "en cours de démarrage"
                self.log_message(msg_demarrage, True)
            time.sleep(0.5)

        self.log_message(f"{thread_id} démarré")
        self.root.after(0, self._update_thread_label)

        # Simulation de travail en 3 cycles
        try:
            for i in range(3):  
                if not self.running:
                    break
                self.log_message(f"🔧 {thread_id} - Cycle de travail {i+1}/3")
                time.sleep(2)
        except Exception as e:
            self.log_message(f"💥 {thread_id}: Erreur - {e}")
        finally:
            self.log_message(f"🏁 {thread_id} terminé\n")
            # Decrementer le cmpt quand le thread se termine
            self.root.after(0, self._decrement_thread_label)

    def _decrement_thread_label(self):
        '''Décrémenter le compteur de threads'''
        self.thread_count = max(0, self.thread_count - 1) # sans if
        self.thread_label.config(text=f'Threads actifs : {self.thread_count}')

    def manual_test(self):
        """Tester manuellement des threads (erreurs)"""
        self.log_message("Déclenchement de test manuel...")
        self.show_error_message("Test-Manuel")
    
    def demarrer_thread(self):
        """Démarrer un thread de test supplémentaire"""
        thread = threading.Thread(target=self.test_thread, daemon=True, name=f"Thread-{time.time()}")
        thread.start()
        self.log_message("Lancement d'un thread de test supplémentaire\n")
    
    def stop_app(self):
        """Arrêter l'app proprement"""
        self.log_message("\nDemande d'arrêt de l'application...")
        self.running = False
        self.status_label.config(text='Arrêt en cours...', fg='red')

        # AMÉLIORATION: Message de confirmation avant fermeture
        self.log_message("Fermeture dans 2 secondes...\n")
        self.root.after(2000, self.root.destroy)

def main():
    root = tk.Tk()
    app = BackgroundApp(root)
    
    # Gestion de la fermeture propre
    def on_closing():
        app.stop_app()
    
    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()