class SimpleGithubProject:
    def __init__(self):
        self.project_data = {
            "name": "Simple Github Project",
            "description": "This is a simple project created using GitHub.",
            "features": [
                {"feature_name": "First Feature", "description": "Adds functionality to the project."},
                {"feature_name": "Second Feature", "description": "Another feature added to the project."},
                {"feature_name": "Third Feature", "description": "Adding a new feature"},
                {"feature_name": "Fourth Feature", "description": "Testing multiple features"}
            ]
        }

    def display_project_info(self):
        print(f"Project Data: {self.project_data}")
        for feature in self.project_data["features"]:
            print(f"\n{feature['feature_name']}:")
            for step in feature["steps"]:
                print(f"  - Step {step[0]}: {step[1]}")

if __name__ == "__main__":
    project = SimpleGithubProject()
    project.display_project_info()
