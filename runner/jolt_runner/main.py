import json
# Sample JoltRunner (simplified)
input_file = '../data/examples/input.json'
output_file = '../data/examples/output.json'
with open(input_file) as f: input_data = json.load(f)
with open(output_file) as f: expected_output = json.load(f)
# Simulate transformation (identity mapping)
transformed_output = input_data  # Replace with real JOLT execution
print("JoltRunner: transformed output matches expected:", transformed_output == expected_output)
