# Lab 2 — Prima applicazione ML: il dataset Iris con scikit-learn

### UF-16 · ML & AI · Modulo 1 · Hands-on Lab

> **Livello:** Beginner &nbsp;·&nbsp; **Durata:** ~90 min &nbsp;·&nbsp; **Ambiente:** Google Colab (browser) &nbsp;·&nbsp; **Linguaggio:** Python 3

---

## Obiettivi del lab

Al termine di questo laboratorio sarai in grado di:

1. Riconoscere l'**API uniforme** di `scikit-learn`: `Estimator`, `fit`, `predict`, `score`.
2. Caricare ed esplorare il dataset **Iris** (un classico della letteratura ML).
3. Realizzare un workflow **end-to-end** di classificazione supervised:
 load → split → train → predict → evaluate.
4. Capire la differenza tra **train set** e **test set** e perché lo split è essenziale.
5. Costruire e valutare un classificatore **k-Nearest Neighbors**.
6. Sperimentare con gli **iperparametri** (`k`) e leggere una **confusion matrix**.

> **Prerequisito:** aver completato il **Lab 1** (Colab + NumPy + matplotlib + pandas di base).

---

## Come usare questo lab

1. Apri **[Google Colab](https://colab.research.google.com)** e fai login.
2. Crea un nuovo notebook e rinominalo `Lab2_<TuoNome>.ipynb`.
3. Procedi esercizio per esercizio: ogni sotto-task ha **starter code → consegna → checkpoint → lezione chiave**.
4. Esegui le celle con `Shift + Invio`.
5. Alla fine: `File → Salva una copia in Drive` e consegna il notebook nello spazio condiviso.

> **Buona pratica:** documenta i tuoi esperimenti in celle Markdown. Un notebook non è uno script: è un **diario di analisi**.

---

## Indice degli esercizi

| # | Titolo | Durata | Difficoltà |
|-------|------------------------------------------------------------|---------|------------|
| 1 | **Hello World su scikit-learn** — API e primo Estimator | 20 min | |
| 2.1 | Caricare ed esplorare il dataset Iris | 10 min | |
| 2.2 | Visualizzare i dati (scatter, pair plot) | 10 min | |
| 2.3 | Train/test split: dividere correttamente i dati | 10 min | |
| 2.4 | Addestrare un classificatore k-NN | 10 min | |
| 2.5 | Fare predizioni su nuovi fiori | 10 min | |
| 2.6 | Valutare il modello: accuracy e confusion matrix | 10 min | |
| 2.7 | Sperimentare con il parametro `k` | 10 min | |

---

# Esercizio 1 — Hello World su scikit-learn

## Cos'è scikit-learn

**scikit-learn** è la libreria di riferimento per il Machine Learning "classico" in Python:
classificazione, regressione, clustering, riduzione della dimensionalità, model selection.

Tutta la libreria è costruita attorno a un'idea molto semplice — **l'API Estimator**:

```python
model = AlgoritmoQualsiasi(parametro=...) # 1. istanzia
model.fit(X_train, y_train) # 2. addestra
y_pred = model.predict(X_new) # 3. predici
score = model.score(X_test, y_test) # 4. valuta
```

Imparato uno, imparati tutti.

 **Reference:**
- [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html)
- [Getting started tutorial](https://scikit-learn.org/stable/getting_started.html)
- [API reference](https://scikit-learn.org/stable/api/index.html)
- [Cheat sheet ufficiale: choosing an estimator](https://scikit-learn.org/stable/tutorial/machine_learning_map.html)

## Task 1.1 — Verifica che scikit-learn sia disponibile

**Consegna:** in una nuova cella esegui:

```python
import sklearn
print("scikit-learn version:", sklearn.__version__)

# Lista alcuni moduli importanti
from sklearn import datasets, model_selection, neighbors, metrics
print("Moduli importati correttamente ")
```

** Checkpoint:** vedi la versione di scikit-learn stampata (≥ 1.0) e nessun errore di import.

## Task 1.2 — Il tuo primo Estimator

**Concetto chiave:** ogni algoritmo in scikit-learn è una classe. La istanzi creando un oggetto.

**Codice di partenza:**

```python
from sklearn.neighbors import KNeighborsClassifier

# Crea l'Estimator (non lo addestra ancora!)
knn = KNeighborsClassifier(n_neighbors=3)

print(knn)
print("Parametri:", knn.get_params())
```

**Il tuo compito:**
1. Crea altri due Estimator: un `LogisticRegression` e un `DecisionTreeClassifier` (li importi da `sklearn.linear_model` e `sklearn.tree`).
2. Stampa i loro parametri di default con `.get_params()`.
3. Quale Estimator ha **più iperparametri**?

** Checkpoint:** vedi i parametri di tre Estimator diversi. Stessa API, configurazioni diverse.

## Task 1.3 — Un dataset giocattolo per capire `fit` e `predict`

**Scenario:** abbiamo 6 frutti con due caratteristiche (peso in grammi e diametro in cm). Vogliamo classificare se è una mela (0) o un'arancia (1).

**Codice di partenza:**

```python
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# Training set: 6 frutti
X_train = np.array([
 [150, 7], # mela
 [170, 7.5], # mela
 [140, 6.8], # mela
 [200, 8.5], # arancia
 [220, 9], # arancia
 [180, 8], # arancia
])
y_train = np.array([0, 0, 0, 1, 1, 1]) # 0=mela, 1=arancia

# Crea, addestra, predici
clf = KNeighborsClassifier(n_neighbors=3)
clf.fit(X_train, y_train)

# Un nuovo frutto: 160g, 7.2cm di diametro — mela o arancia?
nuovo = np.array([[160, 7.2]])
predizione = clf.predict(nuovo)
print("Predizione:", predizione, "(0=mela, 1=arancia)")
```

**Il tuo compito:**
1. Esegui il codice e verifica che la predizione sia coerente con il buon senso.
2. Prova con un frutto da `[210, 8.7]`. Che frutto è?
3. Prova con `[180, 7.5]` (caso ambiguo, "in mezzo"). Come decide il modello?
4. Cambia `n_neighbors` da 3 a 1 e poi a 5. Le predizioni cambiano?

** Checkpoint:** il primo frutto è una mela (0), il secondo un'arancia (1).

 **Lezione chiave:** scikit-learn applica **lo stesso pattern** a qualunque algoritmo. Quello che cambia tra modelli è il loro funzionamento interno, non l'API che usi.

 **Approfondimento:** [Estimator API design](https://scikit-learn.org/stable/developers/develop.html) — perché tutti gli Estimator hanno la stessa interfaccia.

---

# Esercizio 2 — Classificazione di fiori Iris

Useremo il **dataset Iris**, un classico della statistica e del ML.

- **150 fiori** appartenenti a **3 specie**: *setosa*, *versicolor*, *virginica*.
- **4 misure (feature)** per ciascun fiore: lunghezza e larghezza di sepalo e petalo (in cm).
- **Task:** dato un nuovo fiore, prevedere a quale specie appartiene → **classificazione a 3 classi**.

> **Curiosità storica:** il dataset fu pubblicato dal biologo Edgar Anderson nel 1935 e reso famoso da Ronald Fisher nel 1936 in uno dei lavori fondativi della statistica multivariata. È usato in tutti i corsi di ML perché è **piccolo, ben separato e interpretabile**.

 **Reference:**
- [Iris dataset description (UCI)](https://archive.ics.uci.edu/dataset/53/iris)
- [`sklearn.datasets.load_iris`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)
- [Wikipedia: Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set)

---

## Task 2.1 — Caricare ed esplorare il dataset

**Codice di partenza:**

```python
from sklearn.datasets import load_iris

iris = load_iris()

# load_iris() restituisce un Bunch (un dizionario evoluto)
print("Chiavi disponibili:", list(iris.keys()))
print()
print("Feature names :", iris.feature_names)
print("Target names :", iris.target_names)
print("Shape di data :", iris.data.shape)
print("Shape di target:", iris.target.shape)
```

**Il tuo compito:**
1. Stampa le **prime 5 righe** di `iris.data` (suggerimento: `iris.data[:5]`).
2. Stampa le **prime 10 etichette** di `iris.target`. Quanti valori distinti vedi?
3. Quanti fiori ci sono **per ciascuna classe**? (Suggerimento: `np.unique(iris.target, return_counts=True)`).
4. (Opzionale) Stampa la descrizione completa con `print(iris.DESCR[:1000])`.

** Checkpoint:**
- `iris.data.shape` deve essere `(150, 4)`.
- Ci sono **50 fiori per ciascuna delle 3 classi** (perfettamente bilanciato!).

## Task 2.2 — Visualizzare i dati con un pair plot

**Concetto chiave:** prima di modellare, **guarda i dati**. Un grafico vale 1000 numeri.

Useremo `pandas` per costruire un DataFrame comodo da plottare, e `seaborn` (già installato in Colab) per il pair plot.

**Codice di partenza:**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Costruisci un DataFrame con feature + colonna specie (leggibile)
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["species"] = [iris.target_names[t] for t in iris.target]

print(df.head())
print()
print(df["species"].value_counts())

# Pair plot: tutte le coppie di feature, colorate per specie
sns.pairplot(df, hue="species", height=2.0)
plt.suptitle("Iris — pair plot delle 4 feature", y=1.02)
plt.show()
```

**Il tuo compito:**
1. Esegui e osserva il pair plot. Quale specie è **più facile da separare** dalle altre?
2. Quali due feature sembrano **più discriminative** tra le tre classi? (Suggerimento: petali o sepali?)
3. Fai uno scatter plot semplice di **`petal length`** vs **`petal width`** colorato per specie usando solo `matplotlib`.

** Checkpoint:** `setosa` è linearmente separabile dalle altre due; `versicolor` e `virginica` si sovrappongono leggermente.

 **Lezione chiave:** se le classi sono ben separate nello spazio delle feature, anche un algoritmo semplice (come k-NN) funzionerà molto bene. Se sono mescolate, ti servirà un modello più potente o feature migliori.

 **Approfondimento:** [Seaborn pairplot docs](https://seaborn.pydata.org/generated/seaborn.pairplot.html)

## Task 2.3 — Train/test split

**Concetto chiave:** **MAI** valutare un modello sui dati con cui è stato addestrato.
Riserviamo una parte dei dati (~25%) come **test set**, "in cassaforte", per misurare quanto il modello generalizza a dati mai visti.

**Codice di partenza:**

```python
from sklearn.model_selection import train_test_split

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
 X, y,
 test_size=0.25,
 random_state=0,
 stratify=y, # mantiene le proporzioni delle classi nei due split
)

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)
```

**Il tuo compito:**
1. Quanti fiori finiscono nel **train** e quanti nel **test**?
2. Verifica che le **proporzioni delle classi** nel train e nel test siano simili (`np.unique(..., return_counts=True)`).
3. Rilancia lo split **senza** `random_state`. Le dimensioni cambiano? E i numeri specifici?
4. Cosa succede se metti `test_size=0.5`? E `test_size=0.1`?

** Checkpoint:**
- `X_train.shape == (112, 4)` e `X_test.shape == (38, 4)`.
- Le tre classi sono ~38 in train e ~12 in test (stratificate).

> **Errori frequenti da evitare:**
> - **Mai** usare il test set per scegliere il modello o gli iperparametri.
> - **Mai** "sbirciare" il test set durante lo sviluppo.
> - **Sempre** fissare `random_state` per esperimenti riproducibili.

 **Approfondimento:** [`train_test_split` docs](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) · [Cross-validation: evaluating estimator performance](https://scikit-learn.org/stable/modules/cross_validation.html)

## Task 2.4 — Addestrare un classificatore k-NN

**Concetto chiave:** **k-Nearest Neighbors** è uno dei classificatori più semplici. Non costruisce un modello esplicito: memorizza il training set e, per predire un punto nuovo, cerca i `k` punti più vicini e restituisce la classe di maggioranza.

**Codice di partenza:**

```python
from sklearn.neighbors import KNeighborsClassifier

# 1. Istanzia
knn = KNeighborsClassifier(n_neighbors=1)

# 2. Addestra
knn.fit(X_train, y_train)

print("Modello addestrato:", knn)
print("Numero di vicini :", knn.n_neighbors)
print("Classi apprese :", knn.classes_)
```

**Il tuo compito:**
1. Esegui il codice e verifica che `knn.classes_` sia `[0, 1, 2]`.
2. Per k-NN il `fit` è quasi istantaneo. Perché? (Pensa: cosa fa veramente l'algoritmo nel `fit`?)
3. Calcola l'accuracy **sul training set** con `knn.score(X_train, y_train)`. È un risultato affidabile? Perché no?
4. Crea un secondo modello `knn5 = KNeighborsClassifier(n_neighbors=5)`, addestralo e confronta lo score sul training.

** Checkpoint:** lo score sul training con `n_neighbors=1` è esattamente **1.0** (100%). Sai dire perché?

 **Lezione chiave:** con `k=1`, ogni punto del training è il "primo vicino di sé stesso", quindi l'accuracy sul training è sempre perfetta. Ma questo dice **zero** sulla generalizzazione. Per quello serve il test set.

 **Approfondimento:** [`KNeighborsClassifier` docs](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) · [Nearest Neighbors user guide](https://scikit-learn.org/stable/modules/neighbors.html)

## Task 2.5 — Fare predizioni su nuovi fiori

**Codice di partenza:**

```python
import numpy as np

# Un nuovo fiore — misure (sepal length, sepal width, petal length, petal width) in cm
fiore_nuovo = np.array([[5.0, 2.9, 1.0, 0.2]])

prediction = knn.predict(fiore_nuovo)
species = iris.target_names[prediction]

print(f"Misure: {fiore_nuovo[0]}")
print(f"Classe predetta: {prediction[0]} → {species[0]}")
```

**Il tuo compito:**
1. Predici la specie per questi tre fiori:
 - `[5.1, 3.5, 1.4, 0.2]`
 - `[6.7, 3.0, 5.2, 2.3]`
 - `[5.7, 2.8, 4.1, 1.3]`
2. Stampa anche le **probabilità** predette con `knn.predict_proba(...)`. Cosa rappresentano?
3. Cosa succede se passi un array 1D invece che 2D, tipo `knn.predict([5.0, 2.9, 1.0, 0.2])`? Prova e leggi l'errore.

** Checkpoint:**
- Il primo fiore è classificato come **setosa**, il secondo come **virginica**, il terzo come **versicolor**.
- `predict_proba` ritorna 3 colonne (una per classe) che sommano a 1.

> **Errore tipico:** scikit-learn **richiede sempre un array 2D** come input di `predict` — shape `(n_samples, n_features)`. Anche per un solo fiore: `[[...]]` (doppie parentesi).

 **Approfondimento:** [Predict vs predict_proba](https://scikit-learn.org/stable/glossary.html#term-predict_proba)

## Task 2.6 — Valutare il modello

**Concetto chiave:** ora usiamo il **test set** che avevamo messo da parte.
L'**accuracy** è la frazione di predizioni corrette: `accuracy = corrette / totali`.

**Codice di partenza:**

```python
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Predizione su tutto il test set
y_pred = knn.predict(X_test)

# Accuracy in tre modi equivalenti
print("Accuracy (manuale):", np.mean(y_pred == y_test))
print("Accuracy (sklearn):", accuracy_score(y_test, y_pred))
print("Accuracy (score) :", knn.score(X_test, y_test))
```

**Il tuo compito:**
1. Calcola e stampa la **confusion matrix** con `confusion_matrix(y_test, y_pred)`.
2. Stampa il **classification report** con `classification_report(y_test, y_pred, target_names=iris.target_names)`. Quali sono le metriche precision, recall, f1?
3. Visualizza la confusion matrix con questa cella:

```python
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

disp = ConfusionMatrixDisplay.from_estimator(
 knn, X_test, y_test,
 display_labels=iris.target_names,
 cmap="Blues",
)
plt.title("Confusion Matrix — k-NN (k=1)")
plt.show()
```

4. Su quale coppia di classi (se esiste) il modello sbaglia di più? È sorprendente alla luce di ciò che hai visto nel pair plot?

** Checkpoint:** l'accuracy sul test è tipicamente tra **0.95 e 1.00** (con `random_state=0` e `n_neighbors=1`).

 **Lezione chiave:** l'**accuracy** è una sintesi utile, ma la **confusion matrix** ti dice **dove** sbaglia il modello. In problemi reali (sbilanciati o ad alto rischio) questo è spesso più importante del numero singolo.

 **Approfondimento:** [Classification metrics guide](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics) · [Confusion matrix docs](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)

## Task 2.7 — Sperimentare con il parametro `k`

**Concetto chiave:** `k` è un **iperparametro**. Non viene appreso dai dati: lo sceglie chi modella. Valori diversi danno modelli diversi.

**Codice di partenza:**

```python
import matplotlib.pyplot as plt

k_values = range(1, 31)
train_scores = []
test_scores = []

for k in k_values:
 model = KNeighborsClassifier(n_neighbors=k)
 model.fit(X_train, y_train)
 train_scores.append(model.score(X_train, y_train))
 test_scores.append(model.score(X_test, y_test))

plt.figure(figsize=(9, 5))
plt.plot(k_values, train_scores, "o-", label="Training accuracy")
plt.plot(k_values, test_scores, "s-", label="Test accuracy")
plt.xlabel("Numero di vicini (k)")
plt.ylabel("Accuracy")
plt.title("Effetto di k sul k-NN sull'Iris")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

best_k = k_values[int(np.argmax(test_scores))]
print(f"Miglior k sul test: {best_k} (accuracy = {max(test_scores):.4f})")
```

**Il tuo compito:**
1. Esegui e osserva la curva: come cambia l'accuracy di training all'aumentare di `k`?
2. Come cambia l'accuracy di test?
3. Qual è il valore di `k` che produce le **migliori prestazioni sul test**?
4. Riflessione: **sceglieresti `k` guardando il test set?** Perché potrebbe essere una pratica scorretta?

** Checkpoint:**
- L'accuracy di training a `k=1` è 1.0 e diminuisce gradualmente con `k` crescente.
- L'accuracy di test ha un comportamento meno monotono, con un picco intorno a `k=3-10`.

 **Lezione chiave (importante!):**
- `k=1` → **overfitting**: il modello memorizza il training, generalizza meno.
- `k` molto grande → **underfitting**: il modello fa una media su troppi vicini, perde dettaglio.
- C'è sempre un **trade-off bias-varianza** da bilanciare.
- **Scegliere `k` sul test set è scorretto:** invaliderebbe la valutazione finale. Il modo corretto è la **cross-validation** sul training set (vedremo nei moduli successivi).

 **Approfondimento:** [Underfitting vs overfitting (esempio sklearn)](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html) · [Cross-validation: GridSearchCV](https://scikit-learn.org/stable/modules/grid_search.html)

---

# Riepilogo

In questo lab abbiamo costruito il nostro **primo modello ML completo**, end-to-end.

| Step | scikit-learn API | Cosa abbiamo imparato |
|--------------------------|-------------------------------------------------|---------------------------------------------|
| Carica i dati | `load_iris()` | Dataset come matrice X (150×4) e label y |
| Esplora | `pandas` + `seaborn.pairplot` | Classi ben separate sui petali |
| Splitta | `train_test_split(stratify=y)` | Test set come misura onesta di generalizzazione |
| Addestra | `KNeighborsClassifier().fit(X_train, y_train)` | API uniforme di scikit-learn |
| Predici | `model.predict(X_new)` | Input sempre 2D |
| Valuta | `accuracy_score`, `confusion_matrix` | Numero singolo + dove sbaglia |
| Tuning iperparametri | Loop su `k` + grafico train/test | Trade-off bias/varianza |

---

## Comandi di riferimento rapido

```python
# === scikit-learn workflow completo ===
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1) Load
iris = load_iris()
X, y = iris.data, iris.target

# 2) Split
X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size=0.25, random_state=0, stratify=y
)

# 3) Train
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train, y_train)

# 4) Predict
y_pred = model.predict(X_test)

# 5) Evaluate
print(accuracy_score(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=iris.target_names))
```

---

## Risorse e link utili

| Argomento | Link |
|--------------------------------------|-------------------------------------------------------------------------------------------------------|
| scikit-learn user guide | [User guide](https://scikit-learn.org/stable/user_guide.html) |
| Getting started | [Getting started](https://scikit-learn.org/stable/getting_started.html) |
| Choosing the right estimator | [ML map](https://scikit-learn.org/stable/tutorial/machine_learning_map.html) |
| Iris dataset (UCI) | [Iris @ UCI](https://archive.ics.uci.edu/dataset/53/iris) |
| `load_iris` API | [load_iris docs](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html) |
| Train/test split | [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) |
| KNeighborsClassifier | [KNN docs](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) |
| Nearest Neighbors guide | [User guide §1.6](https://scikit-learn.org/stable/modules/neighbors.html) |
| Classification metrics | [Metrics guide](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics) |
| Confusion matrix display | [ConfusionMatrixDisplay](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.ConfusionMatrixDisplay.html) |
| Cross-validation | [User guide §3.1](https://scikit-learn.org/stable/modules/cross_validation.html) |
| Overfitting vs underfitting | [Example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html) |
| Seaborn pairplot | [pairplot docs](https://seaborn.pydata.org/generated/seaborn.pairplot.html) |
| Kaggle: Iris EDA & ML | [Kaggle Iris](https://www.kaggle.com/datasets/uciml/iris) |

---

## Cosa consegnare

Salva il tuo notebook con il nome `Lab2_<Cognome>_<Nome>.ipynb` e caricalo nello spazio condiviso del corso.

**Domande di riflessione finale** (rispondi in una cella Markdown alla fine del notebook):

1. Qual è il **k migliore** che hai trovato? Perché secondo te?
2. Se ti chiedessi di **valutare onestamente** il modello con il k che hai scelto, cosa faresti di diverso?
3. Quale tra le tre specie è la **più difficile** da classificare, e perché?

> **Buon lavoro!** Il file di **demo del formatore** (`Lab2_demo_instructor.ipynb`) è disponibile dopo il lab come riferimento.
