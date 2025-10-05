# Data-Mapper-AI

## 🚀 Overview
**Data-Mapper-AI** is an AI-powered platform to automatically generate **data transformation mappings**. It is modular and extensible, supporting multiple transformation types like:

- **JOLT** → JSON → JSON transformations
- **XSLT** → XML → XML transformations
- Future transformations (CSV, YAML, etc.)

The platform learns from existing input/output examples and transformation rules to predict new mappings.


## 🗂️ Project Structure
```
data-mapper-ai/
│── repo_harvester/
│    └── main.py
│── spec_mapper/
│    └── main.py
│── runner/
│    ├── jolt_runner/
│    │    └── main.py
│    ├── xslt_runner/
│         └── main.py
│── learner/
│    ├── train.py
│    └── predict.py
│── java/
│    └── jolt_executor/
│         └── JoltExecutor.java
│── data/
│    ├── raw/
│    ├── examples/
│    └── training/
│── docs/
│    ├── architecture.md
│    ├── roadmap.md
│    └── usage.md
│── README.md


```


## 🛠️ Getting Started

### 1. RepoHarvester
Fetch OpenAPI/XSD specs and transformation files from GitHub:
python repo_harvester/main.py --org your-github-org

### 2. SpecMapper
Generate example input/output JSON or XML from specs:

python spec_mapper/main.py --spec data/raw/spec.yaml
### 3. Runner
Run transformations and verify correctness:

#### JOLT example
python runner/jolt_runner/main.py --input data/examples/input.json --jolt mapping.jolt --output data/examples/output.json

#### XSLT example
python runner/xslt_runner/main.py --input data/examples/input.xml --xslt mapping.xslt --output data/examples/output.xml
### 4. Learner
Train the AI model with training data:

python learner/train.py --data data/training/
Predict new transformations:
python learner/predict.py --input data/examples/input.json --output data/examples/output.json

### ✅ Key Features
AI-assisted generation of transformation mappings

Extensible for multiple transformation formats (JSON, XML, etc.)

Human-in-the-loop for corrections and retraining

Output-based verification to ensure correctness

### 📚 Next Steps
Implement real GitHub fetching logic in repo_harvester

Enhance spec_mapper to parse OpenAPI/XSD fully

Integrate real JOLT/XSLT execution in the runner

Train the AI model in learner using real transformation triplets

### ⚡ License
This project is for internal use and experimentation. Adapt and extend as needed.
