import os
import json
from sklearn.metrics import f1_score

# Dictionary to store labels for each file
labels = {}

# Load labels from each file in 'model_results' directory
for file_path in os.listdir('model_results'):
    with open('model_results/' + file_path, 'r') as file:
        labels[file_path] = json.load(file)

# Dictionary to store final aggregated labels
final_labels = {}

# Get the number of models
nb_models = len(os.listdir('model_results'))

# Iterate through discussions
for graph_name in labels[os.listdir('model_results')[0]]:
    graph_labels = []

    # Get the number of utterances
    nb_utterances = len(labels[os.listdir('model_results')[0]][graph_name])

    # Iterate through utterances
    for i in range(nb_utterances):
        sum = 0

        # Iterate through models
        for file_path in os.listdir('model_results'):
            sum += labels[file_path][graph_name][i]

        # Determine the label based on the sum
        label = 0
        if sum > 2:
            label = 1

        graph_labels.append(label)

    final_labels[graph_name] = graph_labels

# Save the final aggregated labels to a JSON file
with open('aggregate_results.json', 'w') as file:
    json.dump(final_labels, file)
