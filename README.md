## 1. Project Title and Overview

**Namu Go**  (New York University Abu Dhabi) and **Nelson Mbigili**  (New York University Abu Dhabi) 



- **Paper Title**: Replication of "*AI IDEs or Autonomous Agents? Measuring the Impact of Coding Agents on Software Development*"
- **Authors**: Shyam Agarwal, Hao He, Bogdan Vasilescu (Carnegie Mellon University)
- **Replication Team**: Namu Go and Nelson Mbigili
- **Course**: CS-UH 3260 Software Analytics, NYUAD
- **Brief Description**: 
  - **Original Paper Summary**:

  The original paper performs a longitudinal causal study to measure the impact of **autonomous coding agents** (e.g., Claude Code, Devin, OpenHands) on software development velocity and quality. By analyzing repositories from the **AIDev dataset**, the authors use a staggered difference-in-differences design to compare projects that adopted agents as their first AI tool versus those with prior AI IDE experience. The study reveals that while agents provide a significant initial boost in development velocity for "AI-new" projects, they consistently lead to increased **technical debt**, with static-analysis warnings and code complexity rising by approximately 18% and 39%, respectively, across all settings.

- **Replication Scope Summary**:

  This replication study evaluates the data integrity and core causal claims of the original research through the following tasks:
    1. **Task 1: Data Inspection**:
        * **Dataset Provenance**: Involves a comprehensive audit of the replication package to categorize files and determine which data points were sourced from the original **AIDev dataset** versus those generated or augmented by the authors.
        * **Adoption Credibility**: Performs a manual validation of agent adoption timelines by randomly selecting 3 repositories from `repos_with_details.csv` (where `num_agent_prs > 0`) and inspecting their Pull Request history around the recorded `first_agent_adopted_at` timestamp to verify accuracy.
    2. **Task 2: Full Paper Replication**:
        * **Result Reproduction**: Executes provided scripts to replicate the findings for all Research Questions (RQs), ensuring that the statistical outputs and causal estimates match the reported figures.
        * **Data Pipeline Validation**: Tests the robustness of the data collection process by randomly picking 2 repositories and re-running the [data collection scripts( from another study)](https://zenodo.org/records/18368662). This includes regenerating `repos_with_details.csv` for these specific repos and analyzing any discrepancies between the original and newly fetched live data.

    All scripts, datasets, and evaluation artifacts needed to reproduce the replication results are provided in this repository.
---


### 2. Repository Structure

Document your repository structure clearly. Organize your repository using the following standard structure:

```
README                    # Documentation for your repository
datasets/                 # Subset of data you used (if any). If you used the whole dataset, include instructions on how to download it
replication_scripts/      # Scripts used in your replication:
                          #   - If you used scripts as-is: document which scripts you ran
                          #   - If you modified scripts: include the modified scripts
                          #   - If you created new scripts: include all new scripts
outputs/                  # Your generated results only
logs/                     # Console output, errors, screenshots
notes/                    # Optional if you have any notes you took during reproduction (E.g., where you noted discrepencies etc)
```

**For each folder and file, provide a brief description of what it contains.**

### 3. Setup Instructions

- **Prerequisites**: Required software, tools, and versions
  - OS requirements
  - Programming language versions (Python, R, etc.)
  - Required packages/libraries and versions
  - Any other dependencies
- **Installation Steps**: Step-by-step instructions to set up the environment
  - How to install dependencies
  - How to configure paths or settings
  - Any environment variables needed

### 4. GenAI Usage

**GenAI Usage**: Briefly document any use of generative AI tools (e.g., ChatGPT, GitHub Copilot, Cursor) during the replication process. Include:

  - Which tools were used
  - How they were used (e.g., understanding scripts, exploring datasets, understanding data fields, debugging)
  - Brief description of the assistance provided


## Grading Criteria for README

Your README will be evaluated based on the following aspects (Total: 40 points):

### 1. Completeness (10 points)
- [ ] All required sections are present
- [ ] Each section contains sufficient detail
- [ ] Repository structure is fully documented
- [ ] All files and folders are explained
- [ ] GenAI usage is documented (if any AI tools were used)

### 2. Clarity and Organization (5 points)
- [ ] Information is well-organized and easy to follow
- [ ] Instructions are clear and unambiguous
- [ ] Professional writing and formatting
- [ ] Proper use of markdown formatting (headers, code blocks, lists)

### 3. Setup and Reproducibility (10 points)
- [ ] Setup instructions are complete and accurate, i.e., we were able to rerun the scripts following your instructions and obtain the results you reported


## Best Practices

1. **Be Specific**: Include exact versions, paths, and commands rather than vague descriptions
2. **Keep It Updated**: Ensure the README reflects the current state of your repository
3. **Test Your Instructions**: Have someone else (or yourself in a fresh environment) follow the setup instructions
4. **Document AI Usage**: If you used any GenAI tools, be transparent about how they were used (e.g., understanding scripts, exploring datasets, understanding data fields)


## Acknowledgement

This guideline was developed with the assistance of [Cursor](https://www.cursor.com/), an AI-powered code editor. This tool was used to:

- Draft and refine this documentation iteratively
