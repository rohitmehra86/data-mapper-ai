import os, json
# Sample SpecMapper: generate example input/output JSON
example_input = {"field1": "value1", "field2": 123}
example_output = {"fieldA": "value1", "fieldB": 123}
os.makedirs("../data/examples", exist_ok=True)
with open("../data/examples/input.json", "w") as f: json.dump(example_input, f, indent=2)
with open("../data/examples/output.json", "w") as f: json.dump(example_output, f, indent=2)
print("SpecMapper: example input/output JSON generated.")
