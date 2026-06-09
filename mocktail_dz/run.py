#!/usr/bin/env python3
"""
╔══════════════════════════════════════╗
║   MOCKTAIL DZ – Lanceur du site web  ║
╚══════════════════════════════════════╝
Exécutez ce script avec : python run.py
"""
import subprocess
import sys
import os

def main():
    print("🍹 Mocktail DZ – Démarrage du serveur web...")
    print("=" * 45)

    # Install Django if needed
    try:
        import django
        print(f"✅ Django {django.__version__} détecté")
    except ImportError:
        print("📦 Installation de Django...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "django"])
        print("✅ Django installé avec succès")

    # Move to project directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)
    print("\n🌐 Site disponible sur : http://127.0.0.1:8000")
    print("   Appuyez sur CTRL+C pour arrêter le serveur\n")
    print("=" * 45)

    # Run server
    subprocess.run([sys.executable, "manage.py", "runserver"])

if __name__ == "__main__":
    main()
