# 📱 Filtre Anti-Spam SMS

> Classification automatique de SMS en **spam** ou **ham** (légitime) grâce au NLP classique et à un modèle de classification binaire avec fonction sigmoïde.

---

## 📋 Table des matières

- [Aperçu](#aperçu)
- [Fonctionnalités](#fonctionnalités)
- [Architecture du projet](#architecture-du-projet)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Pipeline NLP](#pipeline-nlp)
- [Modèle de classification](#modèle-de-classification)
- [Résultats](#résultats)
- [Technologies utilisées](#technologies-utilisées)
- [Contribuer](#contribuer)
- [Licence](#licence)

---

## 🔍 Aperçu

Ce projet implémente un **filtre anti-spam** pour messages SMS en combinant des techniques de traitement du langage naturel (NLP) avec un modèle de **régression logistique** (classification binaire via sigmoïde). L'objectif est de distinguer automatiquement les messages indésirables (spam) des messages légitimes (ham).

Le modèle est entraîné sur le célèbre dataset **SMS Spam Collection** et atteint des performances élevées grâce à un pipeline de prétraitement textuel rigoureux.

---

## ✨ Fonctionnalités

- 🧹 **Prétraitement NLP** : nettoyage, tokenisation, suppression des stop words, stemming/lemmatisation
- 🔢 **Vectorisation** : transformation du texte en vecteurs numériques (TF-IDF ou Bag of Words)
- 📊 **Classification binaire** : modèle avec fonction d'activation sigmoïde
- 📈 **Évaluation** : métriques de performance (accuracy, précision, rappel, F1-score, matrice de confusion)
- 🔮 **Prédiction** : classification de nouveaux SMS en temps réel

---

## 🗂️ Architecture du projet

```
sms-spam-filter/
│
├── app/
│   └── app.py                  # site by streamlit pour test le model
├── data/
│   └── spam.csv                  # Dataset SMS Spam Collection
│
├── notebooks/
│   └── Filter_spams.ipynb         # Analyse exploratoire des données (EDA)
│
├── src/
│   ├── fonctions.py         	  #la fonction │  principale
│  
│
├── models/
│   └── spam_model.pkl       # Modèle entraîné sauvegardé
│   └── vectorizer.py 	     #modele vectorizer
│
│
├── requirements.txt
├── README.md


```

---

## ⚙️ Installation

### Prérequis

- Python 3.8+
- pip

### Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-utilisateur/sms-spam-filter.git
cd sms-spam-filter

# 2. Créer un environnement virtuel
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Télécharger les ressources NLTK (si utilisé)
python -c "import nltk; nltk.download('stopwords'); nltk.download('punkt')"
```

---

## 🚀 Utilisation

### Entraîner le modèle

```bash
python main.py --train
```

### Classifier un nouveau SMS

```bash
python main.py --predict "Congratulations! You've won a FREE prize. Call now!"
```

### Lancer les tests

```bash
pytest tests/
```

---

## 🧠 Pipeline NLP

Le texte brut passe par les étapes suivantes avant d'être soumis au modèle :

```
SMS brut
   │
   ▼
Nettoyage (minuscules, ponctuation, chiffres)
   │
   ▼
Tokenisation
   │
   ▼
Suppression des stop words
   │
   ▼
Stemming / Lemmatisation
   │
   ▼
Vectorisation TF-IDF
   │
   ▼
Vecteur numérique → Modèle
```

---

## 📐 Modèle de classification

Le modèle repose sur une **régression logistique** dont la sortie est calculée via la **fonction sigmoïde** :

$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

- Si `σ(z) ≥ 0.5` → **SPAM**  
- Si `σ(z) < 0.5` → **HAM**

Le modèle est optimisé par descente de gradient en minimisant la **Binary Cross-Entropy Loss**.

---

## 📊 Résultats

| Métrique   | Score  |
|------------|--------|
| Accuracy   | ~98%   |
| Précision  | ~97%   |
| Rappel     | ~96%   |
| F1-Score   | ~96%   |

> *Résultats obtenus sur le dataset SMS Spam Collection avec une division 80/20 train/test.*

---

## 🛠️ Technologies utilisées

| Outil | Usage |
|---|---|
| **Python** | Langage principal |
| **scikit-learn** | Vectorisation TF-IDF, modèle logistique, métriques |
| **NLTK / spaCy** | Prétraitement NLP |
| **pandas / NumPy** | Manipulation des données |
| **Matplotlib / Seaborn** | Visualisations |
| **Jupyter Notebook** | Exploration et prototypage |

---

## 🤝 Contribuer

Les contributions sont les bienvenues ! Pour contribuer :

1. Forkez le projet
2. Créez votre branche (`git checkout -b feature/amelioration`)
3. Committez vos changements (`git commit -m 'Ajout d'une fonctionnalité'`)
4. Poussez la branche (`git push origin feature/amelioration`)
5. Ouvrez une **Pull Request**

---

## 📄 Licence

Ce projet est sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

<p align="center">
  Fait avec ❤️ pour apprendre le NLP et le Machine Learning
</p>
