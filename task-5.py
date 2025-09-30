
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('zomato.csv' , encoding = 'latin-1')

#To display all the columns in the dataframe
print("\nTotal Columns\n",(df.columns))

#To display the information of the dataframe
print("\nInfo of Data Frame\n",df.info())

 #Shows first 5 rows of the dataframe
print("\nFirst 5 Rows of Data Frame\n",df.head())

 #Shows the shape of the dataframe i.e, Number of rows and columns
print("\nShape of data\n", df.shape)

# To display the statistical summary of the dataframe
print("\nStatistical Summary\n",df.describe(include = "all").T)

# To display the number of missing values in each column
print("\nMissing Values in Columns\n",df.isnull().sum())

# To display the number of duplicate rows in the dataframe
print("\nDuplicated Rows\n", df.duplicated().sum())

# Univariate Analysis

# Setting the figure size
plt.figure(figsize=(6,4))
# Plotting the histogram for 'Aggregate rating' column
sns.histplot(df["Aggregate rating"], bins=70, kde=True)
# Adding title to the plot
plt.title("Distribution of Aggregate Ratings")
# Displaying the plot
plt.show()

# Count how many restaurants in each country
plt.figure(figsize=(6,4))
# Plotting the countplot for 'Country Code' column
sns.countplot(y=df['Country Code'])
# Adding title to the plot
plt.title("Restaurant Count by Country Code")
# Displaying the plot
plt.show()

# Spreading of the Price range 
plt.figure(figsize=(6,4))
# Plotting the boxplot for 'Price range' column
sns.boxplot(x=df["Price range"])
# Adding title to the plot
plt.title("Price Range Distribution")
# Displaying the plot
plt.show()

# Bivariate Analysis 

# Relationship between Aggregate rating and Price range
plt.figure(figsize=(8,5))
# Plotting the boxplot for 'Price range' vs 'Aggregate rating'
sns.boxplot(x="Price range" , y="Aggregate rating" , data = df)
# Adding title to the plot
plt.title("Price Range vs Aggregate Rating")
# Displaying the plot
plt.show()

# Correlation between Votes and Aggregate rating
plt.figure(figsize=(6,4))
# Plotting the scatterplot for 'Votes' vs 'Aggregate rating'
sns.scatterplot(x="Votes" , y="Aggregate rating" , data = df, alpha=0.6)
# Adding title to the plot
plt.title("Votes vs Aggregate Rating")
# Displaying the plot
plt.show()
corr = df.corr() 
# Calculate correlation matrix
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
plt.title("Correlation Heatmap")  
plt.show()
# Show the heatmap
plt.show()

# Correlation & Heatmap
plt.figure(figsize=(8,5))
# Plotting the heatmap for correlation matrix
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")  
# Adding title to the plot
plt.title("Correlation Heatmap")  
# Displaying the plot       
plt.show()
sns.pairplot(df[["Aggregate rating", "Votes", "Price range"]])  
# Pairplot draws scatterplots for every pair of selected columns
plt.show()

# Categorical Insights
plt.figure(figsize=(10,5))
df['Cuisines'].value_counts().head(10).plot(kind='bar')  
plt.title("Top 10 Cuisines")  
plt.show()
plt.figure(figsize=(6,4))  
sns.boxplot(x="Has Online delivery", y="Aggregate rating", data=df)  
# Compare ratings of restaurants that have online delivery vs those that don’t
plt.title("Online Delivery vs Ratings")  
plt.show()

# -------------------------------
#  Observations (to be written manually after seeing graphs)
# -------------------------------
# - After running the code and looking at charts, write down things like:
# - Most restaurants have ratings between 3.0 and 4.0
# - Restaurants with more votes usually have higher ratings
# - Indian cuisine is most common
# - Price range affects ratings slightly
# - Restaurants with online delivery may have different ratings
