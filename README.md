# Elevate-Labs-Task-5

---

# 📊 Exploratory Data Analysis (EDA) – Zomato Dataset

## 📌 Objective

Perform **Exploratory Data Analysis (EDA)** on the Zomato dataset using **Pandas, Matplotlib, and Seaborn** to extract insights, identify patterns, and visualize relationships in the data.

---

## 📂 Dataset

* **File:** `zomato.csv`
* Contains details about restaurants such as:

  * Restaurant ID, Name, Location (Country, City, Locality)
  * Cuisines offered
  * Price range and Average cost for two
  * Online delivery availability
  * Ratings, Votes, and Reviews

---

## ⚙️ Steps Performed

### 1. **Data Loading**

* Loaded dataset using Pandas.
* Checked shape, column names, and first few rows.

### 2. **Data Summary**

* Used `.info()`, `.describe()`, and `.isnull()` to explore column types and missing values.

### 3. **Univariate Analysis**

* Distribution of restaurant ratings.
* Count of restaurants by country.
* Price range distribution.

### 4. **Bivariate Analysis**

* Relationship between price range and ratings.
* Votes vs. ratings scatterplot.

### 5. **Correlation Analysis**

* Heatmap for correlations between numerical features.
* Pairplot to study multiple relationships at once.

### 6. **Categorical Insights**

* Top 10 cuisines served.
* Comparison of ratings for restaurants with vs. without online delivery.

---

## 📈 Key Insights

* Most restaurants fall in the **3.0 – 4.0 rating range**.
* **Votes** are moderately positively correlated with ratings.
* **Indian cuisine** is among the most popular.
* **Online delivery** shows differences in ratings compared to restaurants without delivery.
* **Price range** has a weaker effect on ratings compared to other factors.

---

## 🛠️ Tools & Libraries

* **Python 3**
* **Pandas** – data loading & exploration
* **Matplotlib** – basic plotting
* **Seaborn** – advanced visualizations

---

## 📦 Installation

Install the required libraries:

```bash
pip install pandas matplotlib seaborn
```

---

## 🚀 How to Run

1. Clone this repository.
2. Place `zomato.csv` in the same folder as the notebook.
3. Open Jupyter Notebook and run:

   ```bash
   jupyter notebook task-5.ipynb
   ```
4. Run each cell step by step to reproduce analysis and plots.

---

## 📜 Deliverables

* Jupyter Notebook: `task-5.ipynb`
* Summary Report: `task-5-summary.pdf`
* Dataset: `zomato.csv`

---
