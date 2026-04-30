<p style="border:1px; border-style:solid; border-color:black; padding: 1em;">
CS-UH 3260 Software Analytics<br/>
Replication Study Guidelines<br/>
Dr. Sarah Nadi, NYUAD
</p>

# Replication Repository README Template -- CS-UH-3260 Software Analytics


## Overview

This repo provides a template and and guidelines for creating a README file for your replication study repository. The README serves as the primary documentation for your repository and helps evaluators understand your work, navigate your repository structure, and reproduce your replication. You can create a repo based on this template and modify the README and content as needed.


## README Structure Template

Your repository README should include the following sections:

### 1. Project Title and Overview

- **Paper Title**: [Full title of the replicated paper]
- **Authors**: [Original paper authors]
- **Replication Team**: [Your team members' names]
- **Course**: CS-UH 3260 Software Analytics, NYUAD
- **Brief Description**: 
  - 2-3 sentences summarizing what the original paper is about
  - 2-3 sentences summarizing what this replication study does

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
