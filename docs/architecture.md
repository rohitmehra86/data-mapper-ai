# 📐 Data-Mapper-AI System Architecture

## 🎯 Overview
Data-Mapper-AI is an AI-powered platform to generate **data transformation mappings** automatically.  
It supports multiple transformation types (JOLT, XSLT, etc.) and is modular to allow future extensions.

**Core Goals:**
1. Learn from existing transformation mappings.  
2. Generate new transformation rules automatically.  
3. Verify generated transformations against expected output.  

---

## 🖼️ High-Level Flow

```
       ┌───────────────┐
       │ RepoHarvester │
       │  (collects)   │
       └───────┬───────┘
               │
               ▼
       ┌───────────────┐
       │  SpecMapper   │
       │ (examples)    │
       └───────┬───────┘
               │
   ┌───────────┼───────────┐
   ▼           ▼           ▼
Runner for  Runner for    Training
  JOLT       XSLT         Dataset
(verify)   (verify)
               │
               ▼
       ┌───────────────┐
       │ JoltLearner / │
       │ AI Learner    │
       │ (Brain)       │
       └───────┬───────┘
               │
               ▼
       Generates new transformation mappings
```

---

## 🔧 Components

### 1. RepoHarvester
- Crawls GitHub org.  
- Finds repos ending with `-connector`.  
- Downloads:  
  - OpenAPI spec (JSON/YAML)  
  - Transformation files (`*.jolt`, `*.xslt`)  
- Saves into `data/raw/`.

**Input:** GitHub org path  
**Output:** Specs + transformation files  

---

### 2. SpecMapper
- Reads specs (OpenAPI, XML Schema, etc.).  
- Generates **example input/output data**.  
- Uses schema constraints (types, enums, formats).  
- Stores into `data/examples/`.

**Input:** Spec file  
**Output:** Example input + output data JSON/XML  

---

### 3. Runner
- Executes transformations and verifies correctness.  
- Supports multiple types via submodules:  
  - `runner/jolt_runner/` → JSON → JSON (JOLT)  
  - `runner/xslt_runner/` → XML → XML (XSLT)  
- Used in **two phases**:  
  1. Training → generate verified outputs.  
  2. Inference → validate AI-generated mappings.  

**Input:** Input data + transformation  
**Output:** Transformed output + Pass/Fail status  

---

### 4. Learner (AI Brain)
- Trains on triplets: `(input, output → transformation mapping)`.  
- Learns patterns to predict transformations.  
- Works with Runner for validation.  
- Human corrections can be added to retraining dataset.  

**Input:** Training dataset (triplets)  
**Output:** Predicted transformation mappings  

---

## 📂 Suggested Repo Structure

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

---

## ✅ Key Principles
- **Output-based validation:** Success = transformed output matches expected data.  
- **Human-in-the-loop:** Corrections feed back into AI training.  
- **Start simple, extend later:** Begin with JOLT → add XSLT or other formats.  
- **Reusable core modules:** `repo_harvester` & `spec_mapper` can serve other transformation types.  
