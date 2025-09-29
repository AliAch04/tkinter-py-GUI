import threading
import time
from datetime import datetime

class BackgroundApp:
    def __init__(self):
        self.running = True
        self.thread = threading.Thread(target=self.worker)
    
    def worker(self):
        while self.running:
            # Votre logique métier
            with open("/tmp/background_app.log", "a") as f:
                f.write(f"Tâche exécutée à {datetime.now()}\n")
            time.sleep(60)
    
    def start(self):
        self.thread.start()
        print("Application démarrée en arrière-plan...")
    
    def stop(self):
        self.running = False
        self.thread.join()

if __name__ == "__main__":
    app = BackgroundApp()
    app.start()
    
    # Pour arrêter proprement avec Ctrl+C
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        app.stop()
        print("Application arrêtée")