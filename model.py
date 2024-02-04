from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import csv

# Function to load dataset from a CSV file
def load_dataset(filename):
    with open(filename, 'r') as csvfile:
        data = list(csv.reader(csvfile))
    return [(item[0], item[1]) for item in data[1:]]  # Skip header and return dataset

# Load training, testing, and validation datasets
training_data = load_dataset('training_tasks_dataset.csv')
testing_data = load_dataset('testing_tasks_dataset.csv')
validation_data = load_dataset('validation_tasks_dataset.csv')

# Train the classifier
classifier = NaiveBayesClassifier(training_data)

# Function to evaluate the classifier on a dataset
def evaluate_classifier(classifier_param, dataset):
    accuracy = classifier_param.accuracy(dataset)
    print(f"Accuracy: {accuracy*100:.2f}%")
    return accuracy

# Evaluate on validation and testing datasets
print("Validation Dataset Evaluation:")
evaluate_classifier(classifier, validation_data)
print("Testing Dataset Evaluation:")
evaluate_classifier(classifier, testing_data)
