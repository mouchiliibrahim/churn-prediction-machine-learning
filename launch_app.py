#!/usr/bin/env python
"""
Script de lancement automatique pour l'application Streamlit Churn Prediction
"""

import subprocess
import sys
import os

def main():
    print("=" * 60)
    print("  🚀 CHURN PREDICTION DASHBOARD")
    print("  Lancement automatique de Streamlit")
    print("=" * 60)

    # Chemin vers l'environnement ML
    ml_python = r"C:\Users\Pc\.conda\envs\ML\python.exe"
    app_path = r"c:\Users\Pc\Desktop\ML\tp1 optimisation\streamlit_app.py"

    # Vérifier si l'environnement existe
    if not os.path.exists(ml_python):
        print("❌ Erreur : Environnement ML non trouvé à", ml_python)
        print("Vérifiez que conda est installé et l'environnement 'ML' existe.")
        return

    # Vérifier si le fichier app existe
    if not os.path.exists(app_path):
        print("❌ Erreur : Fichier streamlit_app.py non trouvé à", app_path)
        return

    print(f"✅ Environnement Python : {ml_python}")
    print(f"✅ Application : {app_path}")

    # Vérifier et installer streamlit si nécessaire
    print("\n🔍 Vérification de Streamlit...")
    try:
        result = subprocess.run([ml_python, "-c", "import streamlit; print('Version:', streamlit.__version__)"],
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            print("✅ Streamlit trouvé :", result.stdout.strip())
        else:
            print("⚠️  Streamlit non trouvé, installation...")
            subprocess.run([ml_python, "-m", "pip", "install", "streamlit"], check=True)
            print("✅ Streamlit installé avec succès")
    except subprocess.TimeoutExpired:
        print("⚠️  Timeout lors de la vérification, tentative d'installation...")
        subprocess.run([ml_python, "-m", "pip", "install", "streamlit"])
    except Exception as e:
        print(f"❌ Erreur lors de la vérification : {e}")
        return

    print("\n🚀 Lancement de l'application Streamlit...")
    print("L'application va s'ouvrir dans votre navigateur par défaut.")
    print("Pour arrêter : Ctrl+C dans ce terminal")
    print("-" * 60)

    try:
        # Lancer streamlit
        subprocess.run([ml_python, "-m", "streamlit", "run", app_path])
    except KeyboardInterrupt:
        print("\n\n🛑 Application arrêtée par l'utilisateur")
    except Exception as e:
        print(f"\n❌ Erreur lors du lancement : {e}")

if __name__ == "__main__":
    main()