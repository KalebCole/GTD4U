# Fill-ins for each category
import random
import csv
categories = ["Research", "Model", "Web App", "Pitch Deck", "Misc"]

research_topics = ["emerging technologies", "hackathon organization", "remote work best practices", "project management tools", "agile vs. waterfall methodologies"]
model_technologies = ["predictive analytics", "workflow optimization", "task prioritization algorithms", "cost estimation techniques", "risk identification strategies"]
web_app_features = ["task creation", "user interface design", "real-time collaboration", "notification systems", "project progress visualization"]
pitch_deck_focuses = ["startup benefits", "unique tool features", "funding acquisition", "tech conference showcases", "market advantage analysis"]
misc_tasks = ["team-building activities", "documentation updates", "user feedback collection", "competitive analysis", "security protocol review"]

# Enhanced task templates with placeholders
task_templates = {
    "Research": [
        "Research the most effective practices for {}.",
        "Investigate the latest trends in {}.",
        "Compile a comprehensive report on the best {}.",
        "Analyze the impact of {} on project efficiency.",
        "Study the benefits of {} in product development."
    ],
    "Model": [
        "Develop a {} to predict task completion times.",
        "Create a simulation model for {}.",
        "Implement a {} for project task prioritization.",
        "Design a {} for project cost estimation.",
        "Build a {} for identifying project risks."
    ],
    "Web App": [
        "Implement a {} function for the project management app.",
        "Design a user-friendly {} for task tracking.",
        "Develop a {} feature for the project board.",
        "Enhance the app's {} for overdue tasks.",
        "Create a {} for visualizing project metrics."
    ],
    "Pitch Deck": [
        "Prepare a pitch deck outlining the {} of GTD4U.",
        "Design a presentation highlighting the {}.",
        "Develop a pitch deck for {} with GTD4U.",
        "Create an engaging pitch deck for {}.",
        "Assemble a pitch deck to illustrate GTD4U's {}."
    ],
    "Misc": [
        "Plan a {} to enhance team collaboration.",
        "Update the GTD4U {} with the latest features.",
        "Organize a {} for the GTD4U application.",
        "Conduct a {} of GTD4U against competitors.",
        "Review and update the GTD4U {}."
    ]
}

# Function to generate a random task with contextual fill-ins
def generate_task(category):
    template = random.choice(task_templates[category])
    fill_in_lists = {
        "Research": research_topics,
        "Model": model_technologies,
        "Web App": web_app_features,
        "Pitch Deck": pitch_deck_focuses,
        "Misc": misc_tasks
    }
    fill_in = random.choice(fill_in_lists[category])
    return template.format(fill_in)



# Adjust the dataset generation function for testing and validation
def generate_dataset(size, filename):
    tasks = [(generate_task(category), category) for category in random.choices(categories, k=size)]
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["text", "category"])
        for task in tasks:
            writer.writerow(task)
    print(f"Dataset with {size} tasks and labels created and saved as {filename}.")

# Generate testing and validation datasets
generate_dataset(30, 'testing_tasks_dataset.csv')
generate_dataset(30, 'validation_tasks_dataset.csv')


