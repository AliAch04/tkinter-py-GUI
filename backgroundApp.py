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
        self.animation_data = {}
        self.new_window_active = False
        self.timer_nw = 2000
        self.delay_nw = 5000
        
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
        
        self.lance_nw_btn = tk.Button(button_frame, text="Lancer Nouveau Fenetre", command= self.launch_window_thread,
                                      bg="#cc3ae2", fg="white", padx=10)
        self.lance_nw_btn.pack(side=tk.LEFT, padx=5)
        
    def log_message(self, msg, is_animation=False, animation_id=None):
        '''Ajouter un message au journal (log_text) - support animation'''
        
        time_stamp = datetime.now().strftime("%H:%M:%S") 

        if is_animation:
            # pas de date pour les messages non thread pour eviter le flickering!
            entry_log = f"{msg}\n" 
        else:
            entry_log = f"[{time_stamp}] {msg}\n" 

        # thread-safe
        if is_animation and animation_id:
            self.root.after(0, self._update_animation_text, entry_log, animation_id)
        else:
            self.root.after(0, self._update_log_text, entry_log)

    
    def _update_log_text(self, log):
        '''MAJ de log_text (Journal d'activité) d'une maniere thread-safe'''
        self.log_text.insert(tk.END, log)
        self.log_text.see(tk.END)
        
        # Limiter la taille du log pour une bonne usage de memoire
        lines = self.log_text.get(1.0, tk.END).split('\n')
        if len(lines) > 1000:  
            self.log_text.delete(1.0, f"{len(lines)-1000}.0")

    def _update_animation_text(self, msg, id_animation):
        '''MAJ speciale pour les messages animation'''
        # Supprimer la dernière ligne (de msg animation)
        if id_animation in self.animation_data:
            # Remplacer le contenu de la ligne existante
            line_start = self.animation_data[id_animation]["line_start"]
            print(f'2 = {self.animation_data}')
            try:
                # Calculer la fin de la ligne actuelle
                line_end = self.log_text.index(f"{line_start} lineend")
                print(f'last_line index : {line_end}')
                # Remplacer le contenu de cette ligne
                self.log_text.delete(line_start, line_end)
                self.log_text.insert(line_start, msg.strip())
                self.log_text.see(tk.END)
                
            except tk.TclError:
                # Si la ligne a été supprimée, recommencer
                self._initialize_animation(msg, id_animation)
        else:
            # Créer une nouvelle ligne d'animation
            self._initialize_animation(msg, id_animation)
            
    def _initialize_animation(self, msg, id_animation):
        '''Initialiser une nouvelle ligne d'animation'''
        curr_end = self.log_text.index(tk.END)
        self.log_text.insert(tk.END, msg)
        self.log_text.see(tk.END)
        self.animation_data[id_animation] = {'line_start': curr_end}
        

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
        pass

    def background_worker_2(self):
        """2ème background qui génère des erreurs chaque 10 secondes"""
        pass

    def display_new_window(self):
        '''Creation d'une nouvelle fenetre avec l'emplacement (en haut à droite)'''
        # Vérifier si la fenetre est deja ouvert
        if hasattr(self, 'new_window') and self.new_window:
            return
        
        # Creation de la nouvelle fenetre
        self.new_window = tk.Toplevel(self.root)
        self.new_window.title("Nouvelle Fenetre")
        self.new_window.geometry("200x80-0+0")

        # Ajout de contenue dans la fenetre
        tk.Label(self.new_window, text='Salame')

        # Gestion de fermeture manuelle (X button de nouveau fenetre)
        def on_manual_close():
            self.new_window_active = False
            self._update_nw_btn()
            self.new_window.destroy()
            self.new_window = None

        self.new_window.protocol('WM_DELETE_WINDOW', on_manual_close)
        
    
    def shut_down_thread(self):
        '''Detruire la fenetre'''
        print('la fenetre va eter detruite inchaAllah')
        self.new_window_active = False
        self.root.after(0, self._update_nw_btn)

        # Vérifier l'existance de la Fenetre 
        if hasattr(self, 'new_window') and self.new_window:
            self.new_window.destroy()
            self.new_window = None
        
        # Decr le compteur de threads
        self.thread_count = max(0, self.thread_count-1) # le max de decr est 0
        self.thread_label.config(text=f'Threads actifs : {self.thread_count}')

    
    def _update_thread_label(self):
        '''MAJ thread counter et afficher le dans thread label'''
        self.thread_count += 1
        self.thread_label.config(text=f'Threads actifs : {self.thread_count}')
    
    def start_threads(self):
        """Démarrer la totalité des threads principaux"""
        pass
    
    def test_thread(self):
        pass

    def _decrement_thread_label(self):
        '''Décrémenter le compteur de threads'''
        pass

    def manual_test(self):
        """Tester manuellement des threads (erreurs)"""
        pass
    
    def demarrer_thread(self):
        """Démarrer un thread de test supplémentaire"""
        pass
    
    def launch_window_thread(self):
        '''Lancer une nouvelle fenetre avec le choix de l'arreter (dans displa_new_window)'''
        # Thread-save 
        self.root.after(0, self.display_new_window)

        self.log_message('Nouveau thread a été bien lancé [New Window]')

        # thread-save
        self.new_window_active = True
        self.root.after(0, self._update_thread_label)
        self.root.after(0, self._update_nw_btn)

        # Planifier la fermeture automatique
        self.root.after(self.timer_nw, self.shut_down_thread)

    def  _update_nw_btn(self):
        '''MAJ le contenue de button (Nouvelle Fenetre)'''
        if self.new_window_active:
            print(f'var of nw is :{self.new_window_active} ARRETE')
            self.lance_nw_btn.config(text='Arreter Nouvelle Fenetre',
                                 bg="#e699f1", fg="white" , command=self.shut_down_thread)
        else :
            print(f'var of nw is :{self.new_window_active} LANCE')
            self.lance_nw_btn.config(text="Lancer Nouveau Fenetre", command=self.launch_window_thread,
                  bg="#cc3ae2", fg="white", padx=10)


    def stop_app(self):
        """Arrêter l'app proprement"""
        self.log_message("\nDemande d'arrêt de l'application...")
        self.running = False
        
        self.stop_animation_count = 0
        self._animate_stop_status()

        # Message de confirmation avant fermeture
        self.log_message("Fermeture dans 2 secondes...\n")
        self.root.after(2000, self.root.destroy)

    def _animate_stop_status(self):
        """Animation des points pour le statut d'arrêt"""
        if self.stop_animation_count < 5: # condition de convergence (5 cycles) 
            base_txt = 'Arrêt en cours'
            curr_pts = '.' * (self.stop_animation_count % 3 + 1)
            anim_txt = f'{base_txt}{curr_pts}'
            
            self.status_label.config(text=anim_txt, fg='red')
            print(anim_txt)  
            
            self.stop_animation_count += 1
            self.root.after(400, self._animate_stop_status)  # 0.4 seconde recursive

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
