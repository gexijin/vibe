# Simple Iris Dataset Analysis
# This script demonstrates basic R data exploration

# Load the built-in iris dataset
data(iris)

# View the first few rows
head(iris)

# Generate summary statistics
summary(iris)

# Create a histogram of sepal length
hist(iris$Sepal.Length,
     col = 'steelblue',
     border = 'white',
     xlab = 'Sepal Length (cm)',
     main = 'Distribution of Iris Sepal Length')

# Create a histogram of petal length
hist(iris$Petal.Length,
     col = 'coral',
     border = 'white',
     xlab = 'Petal Length (cm)',
     main = 'Distribution of Iris Petal Length')
