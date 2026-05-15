# Lab 3 — Prima applicazione ML: regressione con il dataset Boston Housing

### UF-16 · ML & AI · Modulo 1 · Hands-on Lab

> **Livello:** Beginner &nbsp;·&nbsp; **Durata:** ~90 min &nbsp;·&nbsp; **Ambiente:** Google Colab (browser) &nbsp;·&nbsp; **Linguaggio:** Python 3

---

## Obiettivi del lab

Al termine di questo laboratorio sarai in grado di:

1. Distinguere la **regressione** dalla classificazione: prevedere un valore continuo invece di una categoria.
2. Riconoscere l'**API uniforme** di `scikit-learn` applicata alla regressione: `Estimator`, `fit`, `predict`, `score`.
3. Caricare ed esplorare il dataset **Boston Housing** (un classico del ML su dati reali).
4. Realizzare un workflow **end-to-end** di regressione supervised:
 load → split → train → predict → evaluate.
5. Capire la differenza tra **train set** e **test set** e i principali punti di attenzione.
6. Valutare un modello di regressione con le metriche appropriate: **MAE**, **MSE**, **RMSE**, **R²**.
7. Sperimentare con diversi modelli e **iperparametri**, confrontando i risultati.

> **Prerequisito:** aver completato il **Lab 2** (classificazione con k-NN su Iris).

---

## Come usare questo lab

1. Apri **[Google Colab](https://colab.research.google.com)** e fai login.
2. Crea un nuovo notebook e rinominalo `Lab3_<TuoNome>.ipynb`.
3. Procedi esercizio per esercizio: ogni sotto-task ha **starter code → consegna → checkpoint → lezione chiave**.
4. Esegui le celle con `Shift + Invio`.
5. Alla fine: `File → Salva una copia in Drive` e consegna il notebook nello spazio condiviso.

> **Buona pratica:** documenta i tuoi esperimenti in celle Markdown. Un notebook non è uno script: è un **diario di analisi**.

---

## Indice degli esercizi

| # | Titolo | Durata | Difficoltà |
|-------|---------------------------------------------------------------------|---------|------------|
| 1 | **Hello World su regressione** — API e primo Estimator | 20 min | |
| 2.1 | Caricare ed esplorare il dataset Boston Housing | 10 min | |
| 2.2 | Visualizzare i dati (distribuzioni, correlazioni, scatter) | 10 min | |
| 2.3 | Train/test split: dividere correttamente i dati | 10 min | |
| 2.4 | Addestrare un modello di regressione lineare | 10 min | |
| 2.5 | Fare predizioni e analizzare i residui | 10 min | |
| 2.6 | Valutare il modello: MAE, MSE, RMSE, R² | 10 min | |
| 2.7 | Sperimentare con iperparametri e confrontare modelli | 10 min | |

---

# Esercizio 1 — Hello World su regressione

## Classificazione vs Regressione

Nel Lab 2 abbiamo **classificato** fiori in categorie discrete (setosa / versicolor / virginica).
La **regressione** risolve un problema diverso: prevedere un **valore numerico continuo**.

| Problema | Output del modello | Esempio |
|-----------------------|--------------------------|----------------------------------|
| Classificazione | Categoria (classe) | "Questo fiore è una setosa" |
| **Regressione** | **Numero reale** | "Questa casa vale 24.5 (k$)" |

L'API di scikit-learn è **identica** — cambia solo l'Estimator che usi:

```python
model = LinearRegression() # 1. istanzia
model.fit(X_train, y_train) # 2. addestra
y_pred = model.predict(X_new) # 3. predici (ora y è un numero, non una classe)
score = model.score(X_test, y_test) # 4. valuta (R² per la regressione)
```

 **Reference:**
- [scikit-learn: supervised learning](https://scikit-learn.org/stable/supervised_learning.html)
- [`LinearRegression` docs](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [Choosing the right estimator](https://scikit-learn.org/stable/tutorial/machine_learning_map.html)

## Task 1.1 — Verifica le librerie

**Consegna:** in una nuova cella esegui:

```python
import sklearn, numpy as np, pandas as pd, matplotlib.pyplot as plt
print("scikit-learn:", sklearn.__version__)

from sklearn import datasets, model_selection, linear_model, metrics
print("Moduli importati correttamente ")
```

** Checkpoint:** versione scikit-learn ≥ 1.0 e nessun errore di import.

## Task 1.2 — Il tuo primo Estimator di regressione

**Codice di partenza:**

```python
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor

for model in [LinearRegression(), DecisionTreeRegressor(), KNeighborsRegressor()]:
 print(type(model).__name__, "→", model.get_params())
 print()
```

**Il tuo compito:**
1. Esegui il codice. Quale modello ha più iperparametri?
2. Nota che esistono versioni *Regressor* degli stessi algoritmi che in Lab 2 usavi come *Classifier*. Cosa cambia nell'output?

** Checkpoint:** vedi i parametri di tre Estimator diversi. Stessa API, task diverso.

## Task 1.3 — Un dataset giocattolo per capire `fit` e `predict`

**Scenario:** abbiamo 6 appartamenti con superficie (m²) e numero di stanze. Vogliamo prevedere il prezzo (k€).

**Codice di partenza:**

```python
import numpy as np
from sklearn.linear_model import LinearRegression

X_train = np.array([[50, 2], [80, 3], [100, 4], [60, 2], [120, 5], [90, 3]])
y_train = np.array([150, 220, 290, 170, 350, 250]) # prezzi in k€

reg = LinearRegression()
reg.fit(X_train, y_train)

nuovo = np.array([[75, 3]])
print("Prezzo stimato:", reg.predict(nuovo), "k€")
print("Coefficienti :", reg.coef_)
print("Intercetta :", reg.intercept_)
```

**Il tuo compito:**
1. Esegui e verifica che la stima sia ragionevole (tra 150 e 350 k€).
2. Prova con `[110, 4]` e `[45, 1]`. I risultati hanno senso?
3. Cosa rappresentano `coef_` e `intercept_`? (Pensa all'equazione `y = mx + b`.)

** Checkpoint:** la stima per `[75, 3]` è circa 210–230 k€.

 **Lezione chiave:** la regressione lineare trova i **coefficienti** che minimizzano l'errore quadratico medio tra valori reali e predetti. L'output è sempre un numero, non una classe.

 **Approfondimento:** [Linear Models user guide](https://scikit-learn.org/stable/modules/linear_model.html)

---

# Esercizio 2 — Regressione sul dataset Boston Housing

Il **Boston Housing dataset** contiene dati su **506 quartieri** della città di Boston (anni '70).

- **13 feature** per quartiere: tasso di criminalità, distanza dai centri di lavoro, accessibilità alle autostrade, percentuale di popolazione a basso reddito, ecc.
- **Target (`MEDV`):** valore mediano delle abitazioni in migliaia di dollari (variabile continua).
- **Task:** dato un quartiere, prevedere il valore mediano delle case → **regressione**.

> **Nota etica:** il dataset originale contiene una variabile (`B`) legata alla composizione razziale del quartiere. Nella versione che useremo (caricata da OpenML) questa variabile è presente per completezza storica, ma **non va usata come feature predittiva**. Nei modelli reali è fondamentale valutare il bias dei dati.

| Feature | Descrizione |
|---------|-------------|
| CRIM | Tasso di criminalità pro capite |
| ZN | Percentuale di terreno residenziale per lotti > 25.000 ft² |
| INDUS | Percentuale di acri commerciali non retail |
| CHAS | Variabile dummy: 1 se il quartiere confina col fiume Charles |
| NOX | Concentrazione di ossidi di azoto (parti per 10 milioni) |
| RM | Numero medio di stanze per abitazione |
| AGE | Percentuale di unità abitative costruite prima del 1940 |
| DIS | Distanza ponderata dai 5 centri di lavoro di Boston |
| RAD | Indice di accessibilità alle autostrade radiali |
| TAX | Aliquota dell'imposta sulla proprietà per 10.000$ |
| PTRATIO | Rapporto alunni/insegnante per città |
| LSTAT | Percentuale di popolazione a basso status socioeconomico |
| MEDV | **Target** — Valore mediano delle abitazioni (k$) |

 **Reference:**
- [Boston Housing @ OpenML](https://www.openml.org/d/531)
- [Harrison & Rubinfeld (1978) — paper originale](https://www.sciencedirect.com/science/article/pii/0095069678900062)

---

## Task 2.1 — Caricare ed esplorare il dataset

> ℹ Il dataset Boston Housing è stato rimosso da scikit-learn dalla versione 1.2 per ragioni etiche. Lo carichiamo da OpenML, che è la fonte standard alternativa.

**Codice di partenza:**

```python
from sklearn.datasets import fetch_openml
import pandas as pd
import numpy as np

boston = fetch_openml(name="boston", version=1, as_frame=True, parser="auto")

df = boston.frame.copy()
df.columns = [c.upper() for c in df.columns]

print("Shape:", df.shape)
print("\nFeature names:", list(df.columns[:-1]))
print("Target : MEDV (valore mediano abitazioni in k$)")
print()
print(df.describe().round(2))
```

**Il tuo compito:**
1. Quante righe e colonne ha il dataset?
2. Qual è il valore **minimo** e **massimo** di `MEDV` (il target)?
3. Ci sono **valori mancanti**? (`df.isnull().sum()`)
4. Stampa le prime 5 righe con `df.head()`.

** Checkpoint:**
- `df.shape == (506, 14)` (13 feature + 1 target).
- `MEDV` va da 5.0 a 50.0 k$ con media ~22.5 k$.
- Nessun valore mancante.

## Task 2.2 — Visualizzare i dati

**Concetto chiave:** prima di modellare, **guarda i dati**. Per la regressione ci interessano soprattutto le **correlazioni** tra feature e target.

**Codice di partenza:**

```python
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Distribuzione del target
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].hist(df["MEDV"], bins=30, edgecolor="white")
axes[0].set(title="Distribuzione MEDV", xlabel="Valore mediano (k$)", ylabel="Conteggio")

# 2. Heatmap correlazioni
corr = df.corr(numeric_only=True)
sns.heatmap(corr[["MEDV"]].sort_values("MEDV"), annot=True, fmt=".2f",
 cmap="coolwarm", ax=axes[1], vmin=-1, vmax=1)
axes[1].set_title("Correlazione con MEDV")
plt.tight_layout()
plt.show()
```

**Il tuo compito:**
1. Quale feature ha la **correlazione più alta** (positiva) con `MEDV`?
2. Quale ha la **correlazione più negativa**? Ha senso intuitivamente?
3. Fai uno scatter plot di `RM` (numero di stanze) vs `MEDV` e uno di `LSTAT` vs `MEDV`:

```python
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
for ax, feat in zip(axes, ["RM", "LSTAT"]):
 ax.scatter(df[feat], df["MEDV"], alpha=0.4, s=15)
 ax.set(xlabel=feat, ylabel="MEDV (k$)", title=f"{feat} vs MEDV")
plt.tight_layout()
plt.show()
```

4. La relazione tra `RM` e `MEDV` sembra **lineare**? E quella tra `LSTAT` e `MEDV`?

** Checkpoint:**
- `RM` ha correlazione positiva (~0.70): più stanze → valore più alto.
- `LSTAT` ha correlazione negativa (~-0.74): più basso status → valore più basso.
- La relazione `LSTAT`–`MEDV` è leggermente curvilinea.

 **Lezione chiave:** la correlazione lineare è un primo indicatore, ma non cattura relazioni non lineari. Visualizzare gli scatter plot è essenziale prima di scegliere il modello.

 **Approfondimento:** [pandas `corr()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html) · [seaborn heatmap](https://seaborn.pydata.org/generated/seaborn.heatmap.html)

## Task 2.3 — Train/test split

**Concetto chiave:** come nel Lab 2, riserviamo una parte dei dati (~20%) come **test set** per misurare la generalizzazione. Per la regressione **non usiamo `stratify`** (non ci sono classi), ma fissiamo sempre `random_state`.

**Codice di partenza:**

```python
from sklearn.model_selection import train_test_split

# Separa feature e target (escludi B per ragioni etiche)
FEATURES = ["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","LSTAT"]
X = df[FEATURES].astype(float).values
y = df["MEDV"].astype(float).values

X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size=0.20, random_state=42
)

print("X_train:", X_train.shape, " X_test:", X_test.shape)
print("y_train:", y_train.shape, " y_test:", y_test.shape)
print(f"\nMedia MEDV — train: {y_train.mean():.2f} test: {y_test.mean():.2f}")
```

**Il tuo compito:**
1. Quante case finiscono nel train e quante nel test?
2. Le medie di `MEDV` nei due split sono simili? Perché è importante?
3. Prova `test_size=0.30`. Come cambiano le dimensioni?

** Checkpoint:**
- `X_train.shape == (404, 12)` e `X_test.shape == (102, 12)`.
- Le medie di `MEDV` nei due split devono essere vicine (~22 k$).

> **Punti di attenzione:**
> - **Mai** usare il test set per scegliere feature o iperparametri.
> - **Sempre** fissare `random_state` per esperimenti riproducibili.
> - Per la regressione, verifica che la **distribuzione del target** sia simile nei due split (non solo la media).

 **Approfondimento:** [`train_test_split` docs](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)

## Task 2.4 — Addestrare un modello di regressione lineare

**Concetto chiave:** la **regressione lineare** trova i coefficienti `w` che minimizzano la somma dei quadrati dei residui: `min Σ(y_i − ŷ_i)²`. È il punto di partenza per qualsiasi problema di regressione.

**Codice di partenza:**

```python
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)

print("Modello addestrato:", lr)
print("\nCoefficiente R² sul training:", lr.score(X_train, y_train).round(4))

# Coefficienti appresi
coef_df = pd.DataFrame({"feature": FEATURES, "coeff": lr.coef_}).sort_values("coeff")
print("\nCoefficienti (ordinati):")
print(coef_df.to_string(index=False))
print(f"\nIntercetta: {lr.intercept_:.4f}")
```

**Il tuo compito:**
1. Qual è il coefficiente più grande (positivo)? Ha senso con quanto visto nel Task 2.2?
2. Qual è il coefficiente più negativo?
3. Calcola l'R² **sul training set**. È un risultato affidabile per valutare il modello? Perché no?

** Checkpoint:** R² sul training ≈ 0.74–0.76. Il coefficiente di `RM` è il più alto positivo.

 **Lezione chiave:** i coefficienti della regressione lineare sono **interpretabili**: ogni unità in più di `RM` (stanze) aumenta il valore previsto di `coeff_RM` k$. Ma attenzione: i coefficienti dipendono dalla scala delle feature — feature con range molto diversi rendono i coefficienti non direttamente confrontabili.

 **Approfondimento:** [`LinearRegression` docs](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) · [Linear Models guide](https://scikit-learn.org/stable/modules/linear_model.html)

## Task 2.5 — Fare predizioni e analizzare i residui

**Codice di partenza:**

```python
y_pred = lr.predict(X_test)

# Confronto prime 10 predizioni vs valori reali
comparison = pd.DataFrame({"Reale": y_test[:10].round(1), "Predetto": y_pred[:10].round(1)})
comparison["Errore"] = (comparison["Predetto"] - comparison["Reale"]).round(1)
print(comparison.to_string(index=False))
```

**Il tuo compito:**
1. Esegui e osserva: il modello tende a **sovrastimare** o **sottostimare**?
2. Visualizza il grafico **Reale vs Predetto** (un buon modello ha i punti vicini alla diagonale):

```python
plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred, alpha=0.5, s=20)
plt.plot([5, 50], [5, 50], "r--", lw=1.5, label="Predizione perfetta")
plt.xlabel("Valore reale (k$)")
plt.ylabel("Valore predetto (k$)")
plt.title("Reale vs Predetto — Linear Regression")
plt.legend()
plt.show()
```

3. Visualizza la distribuzione dei **residui** (`y_pred - y_test`). Dovrebbe essere centrata sullo zero:

```python
residui = y_pred - y_test
plt.figure(figsize=(7, 4))
plt.hist(residui, bins=25, edgecolor="white")
plt.axvline(0, color="red", linestyle="--")
plt.xlabel("Residuo (k$)")
plt.title("Distribuzione dei residui")
plt.show()
```

4. Noti valori estremi (outlier) nei residui? Cosa potrebbe causarli?

** Checkpoint:**
- Il grafico Reale vs Predetto mostra i punti vicini alla diagonale, con più dispersione per valori alti.
- I residui sono approssimativamente centrati sullo zero.

> **Punto di attenzione:** nel dataset Boston Housing, i valori di `MEDV` sono **troncati a 50 k$** (molte case hanno esattamente 50.0). Questo crea un artefatto visibile nel grafico e nei residui — un esempio reale di **data quality issue**.

 **Lezione chiave:** analizzare i residui è fondamentale. Residui sistematicamente positivi o negativi indicano **bias** del modello; una distribuzione non centrata sullo zero suggerisce che il modello non cattura tutta la struttura dei dati.

## Task 2.6 — Valutare il modello: MAE, MSE, RMSE, R²

**Concetto chiave:** per la regressione non esiste un'unica metrica come l'accuracy. Usiamo quattro metriche complementari:

| Metrica | Formula | Interpretazione |
|---------|---------|-----------------|
| **MAE** | `mean(|y - ŷ|)` | Errore medio assoluto in k$ — facile da interpretare |
| **MSE** | `mean((y - ŷ)²)` | Penalizza gli errori grandi — sensibile agli outlier |
| **RMSE** | `√MSE` | Stessa unità del target (k$) — più interpretabile di MSE |
| **R²** | `1 - SS_res/SS_tot` | Frazione di varianza spiegata — 1.0 = perfetto, 0 = modello nullo |

**Codice di partenza:**

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"MAE : {mae:.2f} k$")
print(f"MSE : {mse:.2f} k$²")
print(f"RMSE : {rmse:.2f} k$")
print(f"R² : {r2:.4f}")
```

**Il tuo compito:**
1. Esegui e interpreta i risultati. Un RMSE di X k$ significa che in media il modello sbaglia di X k$ sul valore di una casa.
2. Calcola anche le stesse metriche **sul training set** (usa `lr.predict(X_train)` e `y_train`). Confronta train vs test.
3. Se R² sul test è ~0.70, significa che il modello spiega il 70% della varianza del target. Cosa spiega il restante 30%?
4. Quale metrica useresti per comunicare le prestazioni a un non-tecnico? Perché?

** Checkpoint:**
- MAE ≈ 3.2–3.5 k$, RMSE ≈ 4.5–5.0 k$, R² ≈ 0.68–0.72 sul test set.
- Le metriche sul training sono leggermente migliori di quelle sul test (normale).

 **Lezione chiave:**
- **MAE** è robusta agli outlier e facile da spiegare: "in media sbagliamo di X k$".
- **RMSE** penalizza gli errori grandi: utile quando gli errori grossi sono costosi.
- **R²** è adimensionale e permette confronti tra dataset diversi, ma può essere fuorviante da sola.
- Usa **sempre almeno due metriche** per avere un quadro completo.

 **Approfondimento:** [Regression metrics guide](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics)

## Task 2.7 — Sperimentare con iperparametri e confrontare modelli

**Concetto chiave:** la regressione lineare ha pochi iperparametri. Per esplorare il trade-off bias/varianza usiamo modelli più flessibili (**Ridge**, **Lasso**, **Decision Tree Regressor**) e confrontiamo i risultati.

**Parte A — Ridge e Lasso: regolarizzazione**

Ridge e Lasso aggiungono un termine di penalità ai coefficienti per ridurre l'overfitting. L'iperparametro `alpha` controlla la forza della penalità.

```python
from sklearn.linear_model import Ridge, Lasso

results = []
for alpha in [0.01, 0.1, 1.0, 10.0, 100.0]:
 for ModelClass in [Ridge, Lasso]:
 m = ModelClass(alpha=alpha)
 m.fit(X_train, y_train)
 results.append({
 "Modello": type(m).__name__,
 "alpha": alpha,
 "R² train": round(m.score(X_train, y_train), 4),
 "R² test": round(m.score(X_test, y_test), 4),
 "RMSE test": round(np.sqrt(mean_squared_error(y_test, m.predict(X_test))), 3),
 })

results_df = pd.DataFrame(results)
print(results_df.to_string(index=False))
```

**Parte B — Decision Tree Regressor: profondità dell'albero**

```python
from sklearn.tree import DecisionTreeRegressor

tree_results = []
for depth in [2, 3, 5, 7, 10, None]:
 m = DecisionTreeRegressor(max_depth=depth, random_state=42)
 m.fit(X_train, y_train)
 tree_results.append({
 "max_depth": str(depth),
 "R² train": round(m.score(X_train, y_train), 4),
 "R² test": round(m.score(X_test, y_test), 4),
 "RMSE test": round(np.sqrt(mean_squared_error(y_test, m.predict(X_test))), 3),
 })

print(pd.DataFrame(tree_results).to_string(index=False))
```

**Parte C — Grafico riassuntivo**

```python
depths = [2, 3, 5, 7, 10, 15]
train_r2, test_r2 = [], []
for d in depths:
 m = DecisionTreeRegressor(max_depth=d, random_state=42)
 m.fit(X_train, y_train)
 train_r2.append(m.score(X_train, y_train))
 test_r2.append(m.score(X_test, y_test))

plt.figure(figsize=(8, 5))
plt.plot(depths, train_r2, "o-", label="R² training")
plt.plot(depths, test_r2, "s-", label="R² test")
plt.xlabel("max_depth")
plt.ylabel("R²")
plt.title("Decision Tree Regressor — effetto di max_depth")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

**Il tuo compito:**
1. Per Ridge/Lasso: come cambia R² al variare di `alpha`? Esiste un valore ottimale?
2. Per il Decision Tree: cosa succede con `max_depth=None` (albero illimitato)? È overfitting o underfitting?
3. Quale modello ottiene il **miglior R² sul test**? E il miglior RMSE?
4. Riflessione: **sceglieresti gli iperparametri guardando il test set?** Perché è scorretto?

** Checkpoint:**
- Ridge/Lasso con `alpha` piccolo si comportano come la regressione lineare; con `alpha` grande i coefficienti si avvicinano a zero.
- Decision Tree con `max_depth=None` ha R² training ≈ 1.0 (overfitting evidente) ma R² test inferiore.
- Il Decision Tree con `max_depth=3–5` spesso supera la regressione lineare sul test.

 **Lezione chiave (importante!):**
- **Overfitting:** modello troppo complesso → R² training alto, R² test basso.
- **Underfitting:** modello troppo semplice → R² basso sia in training che in test.
- **Scegliere gli iperparametri sul test set è scorretto:** invalida la valutazione finale. Il modo corretto è la **cross-validation** sul training set.
- La regressione lineare è un ottimo **baseline**: se un modello più complesso non la batte sul test, non vale la complessità aggiuntiva.

 **Approfondimento:** [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html) · [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html) · [Decision Tree Regressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html) · [Overfitting vs underfitting](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html)

---

# Riepilogo

In questo lab abbiamo costruito il nostro **primo modello di regressione completo**, end-to-end.

| Step | scikit-learn API | Cosa abbiamo imparato |
|--------------------------|---------------------------------------------------------|----------------------------------------------------|
| Carica i dati | `fetch_openml("boston")` | Dataset reale: 506 quartieri, 12 feature, target continuo |
| Esplora | `df.describe()` + `df.corr()` + scatter plot | Correlazioni, outlier, relazioni non lineari |
| Splitta | `train_test_split(test_size=0.20)` | Test set come misura onesta di generalizzazione |
| Addestra | `LinearRegression().fit(X_train, y_train)` | API uniforme — stessa di classificazione |
| Predici | `model.predict(X_test)` | Output numerico continuo, non una classe |
| Analizza residui | Scatter reale vs predetto + istogramma residui | Bias sistematici e outlier |
| Valuta | `MAE`, `MSE`, `RMSE`, `R²` | Quattro metriche complementari |
| Tuning iperparametri | Ridge/Lasso (`alpha`) + Decision Tree (`max_depth`) | Trade-off bias/varianza, overfitting/underfitting |

---

## Comandi di riferimento rapido

```python
# === scikit-learn workflow regressione completo ===
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# 1) Load
boston = fetch_openml(name="boston", version=1, as_frame=True, parser="auto")
X = boston.data.astype(float).values
y = boston.target.astype(float).values

# 2) Split
X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size=0.20, random_state=42
)

# 3) Train
model = LinearRegression()
model.fit(X_train, y_train)

# 4) Predict
y_pred = model.predict(X_test)

# 5) Evaluate
print(f"MAE : {mean_absolute_error(y_test, y_pred):.2f} k$")
print(f"RMSE : {np.sqrt(mean_squared_error(y_test, y_pred)):.2f} k$")
print(f"R² : {r2_score(y_test, y_pred):.4f}")
```

---

## Risorse e link utili

| Argomento | Link |
|--------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| scikit-learn user guide | [User guide](https://scikit-learn.org/stable/user_guide.html) |
| Linear Models guide | [User guide §1.1](https://scikit-learn.org/stable/modules/linear_model.html) |
| `LinearRegression` docs | [LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html) |
| `Ridge` docs | [Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html) |
| `Lasso` docs | [Lasso](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Lasso.html) |
| `DecisionTreeRegressor` docs | [DecisionTreeRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html) |
| Boston Housing @ OpenML | [OpenML dataset 531](https://www.openml.org/d/531) |
| `fetch_openml` docs | [fetch_openml](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_openml.html) |
| Train/test split | [train_test_split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) |
| Regression metrics guide | [Metrics §3.3.4](https://scikit-learn.org/stable/modules/model_evaluation.html#regression-metrics) |
| Overfitting vs underfitting | [Example](https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html) |
| Cross-validation | [User guide §3.1](https://scikit-learn.org/stable/modules/cross_validation.html) |
| Seaborn heatmap | [heatmap docs](https://seaborn.pydata.org/generated/seaborn.heatmap.html) |
| Kaggle: Boston Housing | [Kaggle Boston](https://www.kaggle.com/datasets/vikrishnan/boston-house-prices) |

---

## Cosa consegnare

Salva il tuo notebook con il nome `Lab3_<Cognome>_<Nome>.ipynb` e caricalo nello spazio condiviso del corso.

**Domande di riflessione finale** (rispondi in una cella Markdown alla fine del notebook):

1. Quale metrica hai trovato più utile per valutare il modello? MAE, RMSE o R²? Perché?
2. Tra i modelli provati (LinearRegression, Ridge, Lasso, DecisionTree), quale ha ottenuto le prestazioni migliori sul test set? Ti aspettavi questo risultato?
3. Hai osservato overfitting in qualche configurazione? Come lo hai riconosciuto?

> **Buon lavoro!** Il file di **demo del formatore** (`Lab3_demo_instructor.ipynb`) è disponibile dopo il lab come riferimento.
