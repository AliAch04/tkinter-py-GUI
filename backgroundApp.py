import threading
import time
import os
from datetime import datetime

class BackgroundApp:
    def __init__(self):
        self.running = True
        self.thread = threading.Thread(target=self.worker)
        # Utiliser le dossier temp de Windows ou le dossier courant
        self.log_file = "background_app.log"
    
    def worker(self):
        while self.running:
            try:
                with open(self.log_file, "a", encoding='utf-8') as f:
                    f.write(f"Tâche exécutée à {datetime.now()}\n")
                print(f"✓ Tâche enregistrée dans {self.log_file}")
                time.sleep(10)  # 10 secondes pour les tests
            except Exception as e:
                print(f"Erreur: {e}")
                time.sleep(30)
    
    def start(self):
        self.thread.start()
        print("Application démarrée! Appuyez sur Ctrl+C pour arrêter.")
    
    def stop(self):
        self.running = False
        self.thread.join()

if __name__ == "__main__":
    app = BackgroundApp()
    app.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        app.stop()
        print("Application arrêtée.")