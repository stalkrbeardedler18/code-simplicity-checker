import os
import sys

class CodeSimplicityChecker:
    def __init__(self, filepath):
        self.filepath = filepath

    def analyze(self):
        with open(self.filepath, 'r') as file:
            code = file.read()
        # Placeholder for analysis logic
        print(f'Analyzing {self.filepath} for simplicity...')
        # Example recommendation
        recommendations = self.get_recommendations(code)
        return recommendations

    def get_recommendations(self, code):
        # Dummy implementation; replace with actual analysis
        if 'complex' in code:
            return ['Consider simplifying complex structures.']
        return ['Code appears simple.']

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: code-simplicity-checker <your_script.py>')
        sys.exit(1)
    checker = CodeSimplicityChecker(sys.argv[1])
    recommendations = checker.analyze()
    for recommendation in recommendations:
        print('- ' + recommendation)