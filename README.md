# churn-prediction-machine-learning
il s'agit d'un système de prédiction du désabonnement client (Churn Prediction) capable d'identifier, AVANT qu'ils ne partent, les clients à risque — avec une précision mesurée à plus de 80% (AUC-ROC).
#  Système Intelligent de Détection de Fissures sur les Murs

**Projet Tutoré de mouchili ibrahim, annee 2025-2026 — Institut Saint-Jérôme — Douala, Cameroun**

---

##  Structure du projet

```
crack_detection/
├── crack_detection.ipynb   ← Notebook complet (entraînement + évaluation)
├── app.py                  ← Application Streamlit
├── requirements.txt        ← Dépendances Python
├── README.md               ← Ce fichier
├── dataset/
│   ├── Positive/           ← Images de murs fissurés (vos images "cracks" + dataset public)
│   └── Negative/           ← Images de murs intacts
└── (après entraînement)
    ├── crack_detector_model.keras
    ├── model_metadata.json
    └── crack_detector.tflite
```

---

##  Guide de démarrage rapide

### Étape 1 — Installation

```bash
pip install -r requirements.txt
```

### Étape 2 — Préparer le dataset

1. Copiez vos images de murs fissurés dans `dataset/Positive/`
2. Téléchargez un dataset public :

**Option recommandée (40 000 images):**
```
https://www.kaggle.com/datasets/arunrk7/surface-crack-detection
```
Après téléchargement :
- Dossier `Positive/` → copier dans `dataset/Positive/`
- Dossier `Negative/` → copier dans `dataset/Negative/`

**Autres datasets :**
- Concrete Crack Images : https://data.mendeley.com/datasets/5y9wdsg2zt/2
- SDNET2018 : https://www.kaggle.com/datasets/aniruddhsharma/structural-defects-network-concrete-crack-images

### Étape 3 — Entraîner le modèle

Ouvrez et exécutez toutes les cellules de `crack_detection.ipynb` dans Jupyter :

```bash
jupyter notebook crack_detection.ipynb
```

Le notebook génère automatiquement `crack_detector_model.keras`.

### Étape 4 — Lancer l'application

```bash
streamlit run app.py
```

L'application s'ouvre sur : http://localhost:8501


---

##  Architecture technique

```
Image entrée (JPG/PNG)
        ↓
   Prétraitement
   (224×224, normalisation)
        ↓
   MobileNetV2
   (Transfer Learning)
        ↓
   Classification ──→ Grad-CAM
   (Fissuré/Intact)   (localisation)
        ↓
   Rapport visuel
   (niveau de risque + carte de chaleur)
```

**Niveaux de risque :**
-  **FAIBLE** (< 30%) — Mur sain
-  **MODÉRÉ** (30–50%) — Légères anomalies
-  **ÉLEVÉ** (50–70%) — Fissures significatives
-  **CRITIQUE** (> 70%) — Intervention urgente

---

## Déploiement Streamlit Cloud (optionnel)

1. Créer un dépôt GitHub avec les fichiers du projet
2. Aller sur https://share.streamlit.io
3. Connecter votre dépôt GitHub
4. Sélectionner `app.py` comme fichier principal
5.  L'application est disponible en ligne !

---

##  Références

- Howard, A. et al. (2017). MobileNets. arXiv:1704.04861
- Selvaraju, R.R. et al. (2017). Grad-CAM. ICCV 2017
- Özgenel, Ç.F. (2018). Concrete Crack Detection Dataset. Mendeley Data
- Cha, Y.J. et al. (2017). Deep Learning-Based Crack Detection. Computer-Aided Civil and Infrastructure Engineering
