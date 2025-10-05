# ▶️ Usage Guide - Data-Mapper-AI

## 1. RepoHarvester
Run the script to fetch specs + transformation files:
```bash
python repo_harvester/main.py --org your-github-org
```

## 2. SpecMapper
Generate input/output examples from specs:
```bash
python spec_mapper/main.py --spec data/raw/spec.yaml
```

## 3. Runner
Run transformation and verify:
```bash
# JOLT example
python runner/jolt_runner/main.py --input input.json --jolt mapping.jolt --output expected.json

# XSLT example
python runner/xslt_runner/main.py --input input.xml --xslt mapping.xslt --output expected.xml
```

## 4. Learner
Train AI model:
```bash
python learner/train.py --data data/training/
```

Predict transformation for new specs:
```bash
python learner/predict.py --input input.json --output output.json
```
