import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

class ModernApp:
    def __init__(self):
        # Configuration du theme
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")
        
        self.root = ctk.CTk()
        self.root.title("Application Moderne")
        self.root.geometry("500x400")
        
        self.create_widgets()
    
    def create_widgets(self):
        # Frame principal
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Titre
        title = ctk.CTkLabel(
            main_frame, 
            text="📱 Mon Application Python",
            font=("Arial", 24, "bold")
        )
        title.pack(pady=30)
        
        # Sous-titre
        subtitle = ctk.CTkLabel(
            main_frame,
            text="Cette application a été créée avec Python et peut être compilée en exécutable !",
            font=("Arial", 14),
            wraplength=400
        )
        subtitle.pack(pady=10)
        
        # Boutons
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.pack(pady=30)
        
        # Bouton action
        action_btn = ctk.CTkButton(
            button_frame,
            text="Action Spéciale",
            command=self.special_action,
            height=40,
            width=150,
            font=("Arial", 14)
        )
        action_btn.pack(pady=10)
        
        # Bouton info
        info_btn = ctk.CTkButton(
            button_frame,
            text="Information",
            command=self.show_info,
            height=35,
            width=120,
            fg_color="gray",
            font=("Arial", 12)
        )
        info_btn.pack(pady=5)
        
        # Bouton quitter
        quit_btn = ctk.CTkButton(
            button_frame,
            text="Quitter",
            command=self.root.quit,
            height=30,
            width=100,
            fg_color="red",
            hover_color="darkred",
            font=("Arial", 12)
        )
        quit_btn.pack(pady=10)
        
        # Status bar
        self.status = ctk.CTkLabel(
            main_frame,
            text="✅ Prêt",
            font=("Arial", 10)
        )
        self.status.pack(side="bottom", pady=10)
    
    def special_action(self):
        self.status.configure(text="🔄 Action en cours...")
        self.root.after(2000, self.action_complete)
    
    def action_complete(self):
        messagebox.showinfo("Succès", "Action spéciale terminée avec succès !")
        self.status.configure(text="✅ Action terminée")
    
    def show_info(self):
        info_text = """
        🔧 Informations sur l'application:
        
        • Créée avec Python 3.x
        • Interface: CustomTkinter
        • Peut être compilée en .exe
        • Fonctionne sans Python installé
        • Code source disponible
        """
        messagebox.showinfo("Information", info_text)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    # Installer customtkinter si nécessaire
    # pip install customtkinter
    app = ModernApp()
    app.run()