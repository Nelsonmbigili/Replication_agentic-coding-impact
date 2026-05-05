
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

##  2. Repository Structure 


This repository has the following structure

```text
- README.md:             Main project documentation containing the paper summary, replication scope, and high-level results of the study.
- INSTRUCTS.md:          Technical guide for environment setup and script execution, README from replication package of original paper.
- data/:                 Input directory containing the raw CSVs for the study, including repos_with_details.csv, panel_event_monthly.csv, and matching.csv.
- notebooks/:            The workspace with R Markdown analysis logic for DiD estimation adoption time analysis, and repository metric calculations.
- replication_results/:  Output directory storing generated results by this replication study, including data_inspection_report.md and intermediate replication CSVs.
- plots/:                Directory containing the replicated graphs and tables from RQs.
- scripts/:              Scrips used to download the datasets and randomly select sampled dataset for inspection.
```

## 3. Setup Instructions and Replication Guide
This guide covers all four replication tasks:

1. **Data Inspection** — Reviewing the dataset files, Report included in replication_results
2. **AI Adoption Date Validation** — Report included in replication_results
3. **Replication of Research Questions** — Running the R notebooks to reproduce all results of RQs
4. **Data Re-Collection** — Re-fetching live GitHub data for 2 repositories and comparing against the original

---

### Prerequisites

- **Operating System:** Linux or macOS
- **Programming Languages:** R (for RQ replication), Python 3.9+ (for data re-collection)
- **Tools:** `git`, `pip`, `venv`, RStudio (recommended) or `rmarkdown::render()`
- **R Version:** 4.3.3
- **GitHub Personal Access Token:** Required only for Task 3 (data re-collection). Generate one at
  GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic).
  Minimum scope: `public_repo`

> All required R packages are listed in Task 3. All required Python packages are listed in Task 4.

---

### Task 1: Data Inspection

The full dataset inspection report is saved at:

```text
replication_Results/data_inspection_report.md
```

---

### Task 2: AI Adoption Date Validation

The full review and inspection report is saved at:

```text
replication_Results/adoption_date_validation_report.md
```
Script to randomly select the files can be found at `scripts/random_select.py` and the generated csv with selected repos can be found at `replication_results/selected_3.csv`

---

### Task 3: Replication of Research Questions (R Notebooks)

### Prerequisites

Install the following **before** running any notebook:

**1. System dependencies (macOS — run in Terminal):**
```bash
brew install --cask xquartz
brew install cairo
brew install harfbuzz fribidi
```
> Restart your Mac after installing XQuartz before proceeding.

**2. R 4.3.3** — download from [https://cran.r-project.org](https://cran.r-project.org)

**3. RStudio Desktop** — download from [https://posit.co/download/rstudio-desktop](https://posit.co/download/rstudio-desktop)

**4. R packages (run in RStudio Console):**
```r
install.packages(c(
    "didimputation",   # Borusyak et al. DiD imputation estimator
    "ggplot2",         # Plotting
    "dplyr",           # Data manipulation
    "data.table",      # Fast data operations
    "readr",           # Reading CSV files
    "tidyr",           # Data tidying
    "stringr",         # String manipulation
    "purrr",           # Functional programming
    "lubridate",       # Date/time manipulation
    "knitr",           # Dynamic report generation
    "kableExtra",      # Enhanced table formatting
    "Cairo",           # High-quality PDF graphics device
    "systemfonts",     # Font support
    "textshaping"      # Required by kableExtra
))
```

### Replication Steps

Open the `notebooks/` folder in RStudio and knit the notebooks **in this order**:

1. **`notebooks/RepoMetricsAnalysis.Rmd`**
   Generates descriptive statistics (mean, min, median, max) for both Agent-First and IDE-First groups.
   - **Output:** LaTeX table printed to the RStudio console

2. **`notebooks/AdoptionTimeAnalysis.Rmd`**
   Analyzes when repositories adopted coding agents relative to the study window.
   - **Output:** `plots/agent_adoption_time_combined.pdf`

3. **`notebooks/DiffinDiff.Rmd`**
   Main difference-in-differences analysis estimating static (ATT) and dynamic (event-study) treatment effects across six outcomes for both AF and IF groups.
   - **Output:** Static treatment effects table (rendered in HTML)
   - **Output:** `plots/dynamic_effects.pdf`

Each notebook reads data from `./data/` and saves plots to `./plots/` relative to the notebook location. All outputs are also embedded in the knitted HTML file produced alongside each `.Rmd`.

---

### Task 4: Data Re-Collection (From the CursorStudy replication package)

This task randomly selects 2 repositories from `scripts/CursorStudy/data/repos.csv` via a seed specified, re-fetches their current metrics from the GitHub API, and prints a field-by-field comparison against the original values captured in the paper (March 2025). The console log with differences is included in `scripts/CursorStudy/recolection_log.txt`. The script `cripts/CursorStudy/scripts/recollect_two_repos.py` is adopted from the original [CursorStudy](https://zenodo.org/records/18368662) and only slighly modified to also hihlight the differenced bweteen the two versions of metadatas

### Prerequisites

- Python 3.9+
- A GitHub Personal Access Token (see above)

| Package | Version | Purpose |
|---|---|---|
| PyGithub | >= 2.3.0 | GitHub API client |
| pandas | >= 2.0.0 | Data loading and CSV output |
| python-dotenv | >= 1.0.0 | Loading the `.env` token file |

### Replication Steps

1. **From within the Script Repository**
```bash
cd CursorStudy
```

2. **Set Up Environment**
   Create a virtual environment and install the required dependencies:
```bash
python3 -m venv venv
source venv/bin/activate
pip install PyGithub pandas python-dotenv
```

3. **Configure Your GitHub Token**
   Copy the example env file and add your token:
```bash
cp .env.example .env
```
   Open `.env` and set:
```text
GITHUB_TOKEN=ghp_yourPersonalAccessTokenHere
```

4. **Run the Re-Collection Script**
```bash
python scripts/recollect_two_repos.py
```

#### What the Script Does

1. Loads all 8,621 repositories from `data/repos.csv`
2. Randomly selects 2 repositories using `random_state=42` (reproducible)
3. Queries the GitHub API for current values of all 13 fields
4. Saves the new data to `data/repos_recollected.csv`
5. Prints a field-by-field diff to stdout showing what changed and by how much, this is also saved in `scripts/CursorStudy/recolection_log.txt`

---

### 4. GenAI Usage

- **Tool Used:** [Claude Code](https://claude.ai/new)

- **How It Was Used:**
  - Assisted in installing and seting up the requirements and Assisted in understanding the data flow in replication steps.