# Lab 1 — Setup Colab e librerie scientifiche di base

### UF-16 · ML & AI · Modulo 1 · Hands-on Lab

> **Livello:** Beginner &nbsp;·&nbsp; **Durata:** ~75 min &nbsp;·&nbsp; **Ambiente:** Google Colab (browser) &nbsp;·&nbsp; **Linguaggio:** Python 3

---

## Obiettivi del lab

Al termine di questo laboratorio sarai in grado di:

1. Aprire e usare un notebook su **Google Colab** senza installare nulla in locale.
2. Manipolare array numerici con **NumPy** (creazione, slicing, operazioni vettorializzate).
3. Usare **SciPy** per statistiche e funzioni scientifiche di base.
4. Visualizzare dati con **matplotlib** (line plot, scatter, istogramma, subplot).
5. Lavorare con dataset tabellari usando **pandas** (DataFrame, query, group-by).

Tutti gli esercizi sono **autonomi**: puoi farli nell'ordine indicato o saltare a quello che ti interessa.

---

## Come usare questo lab

1. Vai su **[https://colab.research.google.com](https://colab.research.google.com)** e fai login con il tuo account Google.
2. Crea un **nuovo notebook**: `File → Nuovo blocco note`.
3. Rinominalo `Lab1_<TuoNome>.ipynb` cliccando sul titolo in alto a sinistra.
4. Per ogni esercizio sotto, **leggi la consegna, copia il codice di partenza in una cella** (se presente), poi **risolvi i task**.
5. Esegui ogni cella con `Shift + Invio`. La cella si esegue e la successiva diventa attiva.
6. Quando hai finito: `File → Salva una copia in Drive` (oppure scarica il `.ipynb`).

> **Suggerimento:** apri questo documento e Colab affiancati. In Colab le celle di testo (Markdown) ti aiutano a documentare ciò che stai facendo — usale per scrivere note tue.

---

## Indice degli esercizi

| # | Titolo | Durata | Difficoltà |
|----|-----------------------------------------------|---------|------------|
| 0 | Setup: primo Hello World su Colab | 10 min | |
| 1 | NumPy — array e operazioni vettorializzate | 15 min | |
| 2 | SciPy — statistiche e funzioni scientifiche | 15 min | |
| 3 | matplotlib — visualizzazione dati | 15 min | |
| 4 | pandas — DataFrame e analisi tabellare | 20 min | |

---

# Step 0 — Setup: cos'è Colab e come si usa

## Cos'è Google Colab

**Google Colaboratory** (Colab) è un servizio gratuito di Google che esegue **Jupyter Notebook nel cloud**.
Non devi installare Python, né le librerie: tutto è già pronto in una macchina virtuale temporanea ospitata da Google.

**Vantaggi:**
- Zero setup — basta un browser e un account Google.
- Le librerie scientifiche (NumPy, SciPy, pandas, matplotlib, scikit-learn…) sono **già installate**.
- Accesso gratuito a GPU/TPU per chi serve (modulo successivi).
- Notebook salvati direttamente su Google Drive, condivisibili come un Google Doc.

**Limiti da conoscere:**
- La macchina si **spegne dopo un periodo di inattività** (~90 min). I file `/content/` vengono persi.
- I dati persistenti vanno salvati su Drive o scaricati.
- Le sessioni gratuite hanno tempo massimo di ~12 ore.

 **Reference ufficiale:** [Welcome to Colab](https://colab.research.google.com/notebooks/welcome.ipynb) · [Colab FAQ](https://research.google.com/colaboratory/faq.html)

## 0.1 — Hello World

**Consegna:** crea una nuova cella di codice e incolla:

```python
print("Hello ML & AI World!")

import sys
print("Python version:", sys.version)
```

Esegui con `Shift + Invio`.

** Checkpoint:** vedi la stringa stampata e la versione di Python (3.10+).

## 0.2 — Verifica le librerie pre-installate

**Consegna:** in una nuova cella esegui:

```python
import numpy as np
import scipy
import matplotlib
import pandas as pd
import sklearn

print("numpy :", np.__version__)
print("scipy :", scipy.__version__)
print("matplotlib :", matplotlib.__version__)
print("pandas :", pd.__version__)
print("sklearn :", sklearn.__version__)
```

** Checkpoint:** nessun errore di import e vedi le versioni stampate.

## 0.3 — Le celle Markdown

In Colab puoi inserire celle di **testo** (Markdown) per documentare il tuo lavoro: `Inserisci → Cella di testo`.

**Consegna:** aggiungi una cella di testo sopra le tue celle di codice con il titolo `# Lab 1 — Il mio notebook` e una breve descrizione di cosa farai.

 **Lezione chiave:** un buon notebook alterna **codice eseguibile** e **narrazione**. Non è uno script: è un documento.

 **Approfondimento:** [Markdown guide in Colab](https://colab.research.google.com/notebooks/markdown_guide.ipynb)

---

# Esercizio 1 — NumPy: array e operazioni vettorializzate

## Perché NumPy

NumPy è la **base di tutto lo stack scientifico Python**. Offre l'`ndarray`, un array multidimensionale molto più veloce delle liste Python per operazioni numeriche.

> **Tip:** scikit-learn, pandas, matplotlib usano NumPy "sotto il cofano". Saper manipolare un `ndarray` è propedeutico a qualunque task ML.

 **Reference:**
- [NumPy quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy absolute beginners guide](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Cheat sheet NumPy (DataCamp)](https://www.datacamp.com/cheat-sheet/numpy-cheat-sheet-data-analysis-in-python)

## 1.1 — Creare il primo array

**Codice di partenza:**

```python
import numpy as np

# Da lista Python a ndarray
a = np.array([1, 2, 3, 4, 5])

print("a =", a)
print("shape:", a.shape)
print("dtype:", a.dtype)
print("ndim :", a.ndim)
```

**Il tuo compito:**
1. Crea un secondo array `b` di **10 elementi tutti uguali a zero**. (Suggerimento: `np.zeros`).
2. Crea un array `c` con **i numeri da 0 a 19** usando `np.arange`.
3. Crea un array `d` con **5 numeri equispaziati tra 0 e 1** usando `np.linspace`.
4. Stampa shape e dtype di ognuno.

** Checkpoint:**
- `b.shape` deve essere `(10,)` e `b.dtype` `float64`.
- `c[5]` deve essere `5`.
- `d[0]` deve essere `0.0`, `d[-1]` deve essere `1.0`.

## 1.2 — Operazioni vettorializzate

**Concetto chiave:** con NumPy si opera **su tutto l'array senza loop**. Questa è la "magia" della vettorializzazione.

**Codice di partenza:**

```python
prezzi = np.array([10.0, 15.5, 7.2, 22.0, 9.9])

# IVA al 22%
prezzi_con_iva = prezzi * 1.22
print(prezzi_con_iva)
```

**Il tuo compito:**
1. Calcola la **somma**, la **media** e la **deviazione standard** dei prezzi. (Suggerimento: `np.sum`, `np.mean`, `np.std`).
2. Trova il prezzo **massimo** e il prezzo **minimo**.
3. Trasforma `prezzi` da euro a dollari (assumi cambio 1 € = 1.08 $).
4. Crea un nuovo array `sconto_30` che applica uno **sconto del 30%** a tutti i prezzi.

** Checkpoint:** la somma deve essere `64.6`. La media deve essere `12.92`.

## 1.3 — Slicing e indicizzazione

**Codice di partenza:**

```python
arr = np.arange(20) # [0, 1, 2, ..., 19]
print(arr[5:10]) # elementi dal 5° al 9°
print(arr[arr > 10]) # boolean indexing
```

**Il tuo compito:**
1. Estrai i **primi 5 elementi** di `arr`.
2. Estrai gli **ultimi 5 elementi** (suggerimento: indici negativi).
3. Estrai solo gli elementi **pari** (suggerimento: `arr % 2 == 0`).
4. Crea una **matrice 4×5** con `arr.reshape(4, 5)` e stampa la **seconda riga** e la **terza colonna**.

** Checkpoint:** la matrice ha shape `(4, 5)`. La seconda riga è `[5, 6, 7, 8, 9]`.

 **Approfondimento:** [NumPy indexing official docs](https://numpy.org/doc/stable/user/basics.indexing.html)

 **Lezione chiave:** se ti trovi a scrivere un `for` su un array NumPy, fermati. Quasi sempre esiste un'operazione vettorializzata equivalente, 10-100 volte più veloce.

---

# Esercizio 2 — SciPy: statistiche e funzioni scientifiche

## Perché SciPy

SciPy è costruito **sopra NumPy** e aggiunge funzioni scientifiche avanzate: statistica, ottimizzazione, integrazione, algebra lineare, segnali. In ML lo usiamo soprattutto per **`scipy.stats`** (distribuzioni, test).

 **Reference:**
- [SciPy user guide](https://docs.scipy.org/doc/scipy/tutorial/index.html)
- [scipy.stats reference](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Cheat sheet SciPy (DataCamp)](https://www.datacamp.com/cheat-sheet/scipy-cheat-sheet-linear-algebra-in-python)

## 2.1 — Statistiche descrittive

**Codice di partenza:**

```python
import numpy as np
from scipy import stats

# Generiamo 1000 valori da una distribuzione normale (media 0, dev std 1)
np.random.seed(42)
dati = np.random.normal(loc=0, scale=1, size=1000)

descr = stats.describe(dati)
print(descr)
```

**Il tuo compito:**
1. Estrai dalla variabile `descr` i campi `nobs`, `mean`, `variance`, `skewness`, `kurtosis` e stampali in modo leggibile.
2. Calcola **mediana**, **moda** e **range interquartile (IQR)**. (Suggerimenti: `np.median`, `stats.mode`, `stats.iqr`).
3. Verifica se la media è "vicina" a 0 (entro ±0.1) e stampa un messaggio appropriato.

** Checkpoint:** `nobs` deve essere `1000`. Media ≈ `0.019`, varianza ≈ `0.98`.

## 2.2 — Distribuzioni di probabilità

**Concetto chiave:** SciPy ti dà accesso a **decine di distribuzioni** (normale, uniforme, esponenziale, binomiale…) con la stessa API: `.pdf()`, `.cdf()`, `.ppf()`, `.rvs()`.

**Codice di partenza:**

```python
from scipy import stats
import numpy as np

# Distribuzione normale standard N(0, 1)
x = 1.96
prob = stats.norm.cdf(x) # P(X <= 1.96)
print(f"P(X <= {x}) =", prob)
```

**Il tuo compito:**
1. Calcola la **probabilità** che un valore di una `N(0, 1)` cada tra `-1` e `+1`. (Suggerimento: `cdf(1) - cdf(-1)`).
2. Trova il **valore critico** per cui `P(X <= x) = 0.975` (suggerimento: `stats.norm.ppf(0.975)`).
3. Genera **500 campioni** da una distribuzione esponenziale con `scale=2` (suggerimento: `stats.expon.rvs(scale=2, size=500)`).
4. Stampa media e dev std dei campioni generati.

** Checkpoint:** la prob al punto 1 deve essere ≈ `0.6827` (regola del 68%). Il valore critico al punto 2 deve essere ≈ `1.96`.

## 2.3 — Test statistico semplice (t-test)

**Scenario:** abbiamo due gruppi di clienti e i loro punteggi di soddisfazione. Vogliamo capire se la differenza tra i due gruppi è statisticamente significativa.

**Codice di partenza:**

```python
import numpy as np
from scipy import stats

np.random.seed(0)
gruppo_A = np.random.normal(loc=7.0, scale=1.5, size=50)
gruppo_B = np.random.normal(loc=7.8, scale=1.5, size=50)

t_stat, p_value = stats.ttest_ind(gruppo_A, gruppo_B)
print(f"t-statistic = {t_stat:.3f}")
print(f"p-value = {p_value:.4f}")
```

**Il tuo compito:**
1. Esegui il codice e interpreta il `p_value`: se è `< 0.05` la differenza è **statisticamente significativa**.
2. Cambia la `loc` del `gruppo_B` portandola a `7.05` (molto vicina ad A) e rilancia. Cosa succede al p-value?
3. Stampa una frase in italiano del tipo: `"La differenza è significativa (p=...)"` oppure `"La differenza NON è significativa (p=...)"`.

 **Lezione chiave:** SciPy ti permette di fare statistica seria con poche righe di codice. Ma ricorda: un p-value basso non significa "ho ragione", significa "se non ci fosse differenza, sarebbe raro osservare questo".

 **Approfondimento:** [Welch's t-test (Wikipedia)](https://en.wikipedia.org/wiki/Welch%27s_t-test) · [scipy.stats.ttest_ind docs](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html)

---

# Esercizio 3 — matplotlib: visualizzare dati

## Perché matplotlib

`matplotlib` è la libreria **fondante** per visualizzare dati in Python. È usata sotto il cofano da pandas, seaborn e altre librerie più "moderne". Sapere matplotlib di base è obbligatorio.

 **Reference:**
- [matplotlib pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html)
- [Gallery di esempi](https://matplotlib.org/stable/gallery/index.html)
- [Cheat sheet matplotlib (DataCamp)](https://www.datacamp.com/cheat-sheet/matplotlib-cheat-sheet-plotting-in-python)

## 3.1 — Il tuo primo line plot

**Codice di partenza:**

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.title("La mia prima sinusoide")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()
```

**Il tuo compito:**
1. Aggiungi sullo **stesso grafico** la curva `cos(x)`.
2. Aggiungi una **legenda** che distingua le due curve (suggerimento: `label=...` + `plt.legend()`).
3. Cambia colori e stili di linea (es. `color='red', linestyle='--'`).

** Checkpoint:** vedi due curve, una per sin e una per cos, con legenda visibile.

## 3.2 — Scatter plot con colori per classe

**Scenario:** vogliamo visualizzare 100 punti casuali appartenenti a 3 classi diverse.

**Codice di partenza:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
x = np.random.randn(100)
y = np.random.randn(100)
classi = np.random.randint(0, 3, 100) # 0, 1, 2

plt.figure(figsize=(7, 6))
plt.scatter(x, y, c=classi, cmap='viridis', s=60, alpha=0.7)
plt.title("Punti colorati per classe")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.colorbar(label="classe")
plt.show()
```

**Il tuo compito:**
1. Esegui il codice e verifica che i punti siano colorati in 3 gruppi.
2. Cambia la `cmap` in `'plasma'`, `'coolwarm'`, `'Set1'`. Quale ti piace di più?
3. Aggiungi una griglia con `plt.grid(True, alpha=0.3)`.

** Checkpoint:** vedi 100 punti colorati e la barra dei colori a destra.

## 3.3 — Istogramma di una distribuzione

**Codice di partenza:**

```python
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
dati = np.random.normal(loc=170, scale=10, size=1000) # altezza in cm

plt.figure(figsize=(8, 4))
plt.hist(dati, bins=30, color='steelblue', edgecolor='white')
plt.title("Distribuzione delle altezze (n=1000)")
plt.xlabel("Altezza (cm)")
plt.ylabel("Frequenza")
plt.axvline(np.mean(dati), color='red', linestyle='--', label=f"media = {np.mean(dati):.1f}")
plt.legend()
plt.show()
```

**Il tuo compito:**
1. Cambia il numero di `bins` a `10`, `50`, `100`. Come cambia l'aspetto?
2. Aggiungi una **seconda linea verticale** per la mediana (in verde tratteggiato).
3. (Bonus) Sovrapponi una curva di densità teorica della distribuzione normale.

** Checkpoint:** la media stampata in legenda è ≈ `170.4`.

## 3.4 — Subplot: più grafici in una figura

**Codice di partenza:**

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)

fig, axes = plt.subplots(2, 2, figsize=(10, 7))

axes[0, 0].plot(x, np.sin(x)); axes[0, 0].set_title("sin")
axes[0, 1].plot(x, np.cos(x)); axes[0, 1].set_title("cos")
axes[1, 0].plot(x, np.tan(x)); axes[1, 0].set_title("tan"); axes[1, 0].set_ylim(-5, 5)
axes[1, 1].plot(x, np.exp(-x)); axes[1, 1].set_title("exp(-x)")

fig.suptitle("Quattro funzioni in una figura", fontsize=14)
plt.tight_layout()
plt.show()
```

**Il tuo compito:**
1. Esegui e osserva la struttura 2×2.
2. Sostituisci una delle funzioni con `x**2` o `np.log(x + 1)`.
3. Aggiungi una griglia (`.grid(True)`) a tutti i subplot.

 **Lezione chiave:** la **leggibilità** del grafico è più importante della complessità. Un grafico chiaro vince sempre su uno "fancy".

 **Approfondimento:** [Anatomy of a matplotlib figure](https://matplotlib.org/stable/gallery/showcase/anatomy.html)

---

# Esercizio 4 — pandas: DataFrame e analisi tabellare

## Perché pandas

`pandas` è lo strumento standard per **manipolare dati tabellari** in Python. Pensa a un foglio Excel programmabile: leggi file CSV/Excel, fai query SQL-like, raggruppi, pulisci, esporti.

 **Reference:**
- [pandas getting started](https://pandas.pydata.org/docs/getting_started/index.html)
- [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Cheat sheet pandas (ufficiale, PDF)](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)

## 4.1 — Creare un DataFrame

**Codice di partenza:**

```python
import pandas as pd

dati = {
 "nome": ["Alice", "Bob", "Carla", "Davide", "Elena", "Fabio"],
 "eta": [25, 32, 41, 29, 35, 50],
 "citta": ["Milano", "Roma", "Milano", "Napoli", "Roma", "Milano"],
 "stipendio": [32000, 45000, 52000, 38000, 47000, 60000],
}
df = pd.DataFrame(dati)
print(df)
print()
print(df.dtypes)
print()
print(df.describe())
```

**Il tuo compito:**
1. Stampa la **forma** del DataFrame con `df.shape`.
2. Stampa solo le **prime 3 righe** con `df.head(3)`.
3. Stampa i **nomi delle colonne** con `df.columns.tolist()`.
4. Stampa **media** e **mediana** dello stipendio.

** Checkpoint:** `df.shape` deve essere `(6, 4)`. Media stipendio = `45666.67`.

## 4.2 — Selezione e filtri

**Codice di partenza:**

```python
# Seleziona una colonna
print(df["nome"])

# Seleziona più colonne
print(df[["nome", "stipendio"]])

# Filtra righe con condizione
print(df[df["stipendio"] > 40000])
```

**Il tuo compito:**
1. Estrai tutte le persone che **abitano a Milano**.
2. Estrai chi ha **età tra 30 e 40** anni (suggerimento: `(df["eta"] >= 30) & (df["eta"] <= 40)`).
3. Estrai chi guadagna **più della media** (usa `df["stipendio"].mean()`).
4. Estrai **nome e città** delle persone più giovani di 35.

** Checkpoint:** il filtro Milano restituisce 3 righe.

## 4.3 — Group-by e aggregazioni

**Concetto chiave:** `group-by` è il pattern più potente di pandas. Equivale al `GROUP BY` di SQL: raggruppa righe per una colonna e calcola statistiche per gruppo.

**Codice di partenza:**

```python
# Stipendio medio per città
medie = df.groupby("citta")["stipendio"].mean()
print(medie)
```

**Il tuo compito:**
1. Calcola lo **stipendio massimo** per città.
2. Calcola il **numero di persone** per città (suggerimento: `.size()` o `.count()`).
3. Per ogni città, calcola **insieme** media e dev std dello stipendio (suggerimento: `.agg(["mean", "std"])`).
4. (Bonus) Ordina le città dalla media stipendio più alta alla più bassa.

** Checkpoint:** la città con stipendio medio più alto è **Milano** (≈ `48000`).

## 4.4 — Aggiungere colonne e modificare dati

**Codice di partenza:**

```python
# Aggiungi una colonna calcolata
df["stipendio_netto"] = df["stipendio"] * 0.70

# Categoria di età
df["fascia_eta"] = pd.cut(
 df["eta"],
 bins=[0, 30, 40, 100],
 labels=["giovane", "medio", "senior"]
)

print(df)
```

**Il tuo compito:**
1. Aggiungi una colonna `bonus` pari al **10% dello stipendio**.
2. Aggiungi una colonna `iniziale` che contiene la **prima lettera del nome** (suggerimento: `df["nome"].str[0]`).
3. Conta quante persone ci sono per ogni `fascia_eta` (suggerimento: `df["fascia_eta"].value_counts()`).

## 4.5 — Caricare un CSV reale (bonus opzionale)

Carichiamo un dataset pubblico classico — i **Titanic survivors** — direttamente da URL.

**Codice di partenza:**

```python
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic = pd.read_csv(url)

print(titanic.shape)
print(titanic.head())
print(titanic.info())
```

**Il tuo compito:**
1. Quante **righe** ha il dataset?
2. Quante persone sono **sopravvissute** (colonna `Survived`)?
3. Qual è la **percentuale di sopravvivenza** complessiva?
4. Calcola la **percentuale di sopravvivenza per classe di biglietto** (`Pclass`). Cosa noti?
5. (Bonus) Stesso calcolo ma per **sesso** (`Sex`). Cosa noti?

** Checkpoint:** il dataset ha `891` righe. La sopravvivenza media è ≈ `38.4%`. Le donne sopravvivono molto più degli uomini.

 **Lezione chiave:** in un progetto ML reale, **il 70% del lavoro è in pandas**: caricare, pulire, esplorare, trasformare. Padroneggiarlo è un investimento ad alto ROI.

 **Approfondimento:** [Kaggle Titanic competition](https://www.kaggle.com/c/titanic) — il caso d'uso classico per imparare il workflow ML end-to-end.

---

# Riepilogo

Dopo questo lab dovresti saper rispondere a queste domande:

| # | Domanda | Risposta in una riga |
|----|----------------------------------------------------------------------|--------------------------------------------------------|
| 1 | A cosa serve Colab? | Esegue notebook Python nel cloud senza setup locale. |
| 2 | Qual è la differenza tra una lista Python e un `ndarray` NumPy? | L'`ndarray` è omogeneo, vettorializzato e molto più veloce. |
| 3 | Cosa fa `scipy.stats.ttest_ind`? | Confronta le medie di due campioni indipendenti. |
| 4 | A cosa serve `plt.subplots`? | Creare più grafici nella stessa figura. |
| 5 | A cosa serve `groupby` in pandas? | Raggruppare righe e calcolare aggregati per gruppo. |

---

## Comandi di riferimento rapido

```python
# === NumPy ===
np.array([1, 2, 3]) # crea array da lista
np.arange(10) # 0..9
np.linspace(0, 1, 5) # 5 valori equispaziati tra 0 e 1
arr.reshape(2, 3) # cambia forma
arr.mean(), arr.std(), arr.sum()

# === SciPy ===
from scipy import stats
stats.describe(dati)
stats.norm.cdf(1.96)
stats.ttest_ind(a, b)

# === matplotlib ===
import matplotlib.pyplot as plt
plt.plot(x, y); plt.show()
plt.scatter(x, y, c=labels)
plt.hist(dati, bins=30)
fig, axes = plt.subplots(2, 2)

# === pandas ===
import pandas as pd
df = pd.read_csv("file.csv")
df.head(); df.info(); df.describe()
df[df["col"] > 10]
df.groupby("categoria")["valore"].mean()
df["nuova"] = df["a"] + df["b"]
```

---

## Risorse e link utili

| Argomento | Link |
|---------------|---------------------------------------------------------------------------------------------------|
| Colab tour | [Welcome to Colab](https://colab.research.google.com/notebooks/welcome.ipynb) |
| Colab FAQ | [Colab FAQ](https://research.google.com/colaboratory/faq.html) |
| NumPy guide | [Absolute beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) |
| NumPy quickstart | [Quickstart](https://numpy.org/doc/stable/user/quickstart.html) |
| SciPy tutorial | [SciPy user guide](https://docs.scipy.org/doc/scipy/tutorial/index.html) |
| scipy.stats | [API reference](https://docs.scipy.org/doc/scipy/reference/stats.html) |
| matplotlib pyplot | [Pyplot tutorial](https://matplotlib.org/stable/tutorials/pyplot.html) |
| matplotlib gallery | [Examples](https://matplotlib.org/stable/gallery/index.html) |
| pandas 10-min | [10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) |
| pandas cheat sheet | [PDF ufficiale](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) |
| Jupyter docs | [Jupyter Notebook docs](https://jupyter-notebook.readthedocs.io/en/stable/) |
| Kaggle Titanic | [Tutorial competition](https://www.kaggle.com/c/titanic) |

---

## Cosa consegnare

Salva il tuo notebook con il nome `Lab1_<Cognome>_<Nome>.ipynb` e caricalo nello spazio condiviso del corso.

> **Buon lavoro!** Se ti blocchi, alza la mano oppure scrivi nel canale del corso. Il file di **demo del formatore** (`Lab1_demo_instructor.ipynb`) è disponibile dopo il lab come riferimento.
