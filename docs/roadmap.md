# 🛣️ Data-Mapper-AI Roadmap

## Week 1 – RepoHarvester
- Script to connect to GitHub org.  
- Filter repos ending with `-connector`.  
- Download specs (`spec.yaml/json`) + transformation files (`*.jolt`, `*.xslt`).  

## Week 2 – SpecMapper
- Parse OpenAPI/XSD schemas.  
- Generate example input/output data.  

## Week 3 – Runner
- Implement JOLT runner.  
- Implement XSLT runner (or placeholder).  
- Verify transformation correctness against expected outputs.  

## Week 4 – Learner (Phase 1)
- Prepare dataset triplets: `(input → output → transformation)`.  
- Train small AI model (e.g., t5-small).  

## Week 5 – Learner (Phase 2)
- Integrate with Runner to validate AI-generated transformations.  
- Add human corrections to retraining dataset.  
- Prepare evaluation metrics: output match success rate.  
