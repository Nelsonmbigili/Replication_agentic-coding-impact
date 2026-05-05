## Data Inspection Report

### 1. Dataset Summary and File Contributions

#### 1. `repos_with_details.csv` (768 rows)

Repository-level metadata for all repositories releted to AI-Agent adoption (those that adopted a coding agent). Each row is one repository.

**columns:**
- `name`, `url` — repository identity
- `first_agent_adopted_at`, `agent_adopt_month`, `agent_adopt_week` : when the first agent-authored PR was merged
- `num_agent_prs`, `num_human_prs`, `num_bot_prs`, `num_prs` : PR counts by author type
- `agent_prs_per_month`, `human_prs_per_month` — monthly breakdown of PR activity
- `stars`, `forks`, `primary_language`, `repo_created`: descriptive metadata

> **Usage:** This is the repository index. It identifies treatment units, classifies adoption timing, and provides statistics used in `RepoMetricsAnalysis.Rmd`.

---

#### 2. `panel_event_monthly.csv` (28,911 rows)

The main panel dataset for the difference-in-differences analysis. Each row is one (repository, month) observation for both treatment and matched control repositories.

**columns:**
- `repo_name`, `time`: panel identifiers (repo x month)
- `is_treatment` : 1 for treatment repos, 0 for controls
- `event` : the adoption month (YYYY-MM) for treated repos; NA for controls
- `time_to_event` : months relative to adoption (negative = pre, 0 = adoption month)
- `lead_1`...`lead_6`, `lag_0`...`lag_6` : event-study indicator 
- `agent`, `commits`, `lines_added`, `lines_removed`, `contributors` : activity outcomes
- `stars`, `issues`, `issue_comments`, `age` : repo-level controls
- `ncloc`, `bugs`, `vulnerabilities`, `code_smells`, `cognitive_complexity` : SonarQube code quality metrics
- `matched_agent_first_or_corresponding_matched_control`, `matched_ide_first_or_corresponding_matched_control` : flags for the two study groups (AF = agent-first, IF = IDE-first)
- `dataset_source`, `has_cursor_files` : Origin and Cursor AI detection flags

> **Usage:** This is the core dataset fed into `DiffinDiff.Rmd` to estimate both static (ATT) and dynamic (event-study) treatment effects.

---

#### 3. `matching.csv` (115,846 rows)

Propensity score matching results. Each row is a repository (treatment or control candidate) at a specific matching period, with features used for matching and the identity of its matched partners.

**columns:**
- `repo_name`, `matched_period`, `group` (`treatment` / `control`)
- `propensity_score` : estimated probability of being a treatment unit
- `age_days`, `users_involved`, `n_stars`, `n_forks`, `n_releases`, `n_pulls`, `n_issues`, `n_comments`, `total_events` : pre-treatment covariates used in matching
- `matched_control_1`, `matched_control_2`, `matched_control_3` : up to three matched control repos per treatment repo

> **usage:** Defines which control repositories are paired with each treated repository for the DiD analysis. Ensures comparability between treatment and control groups.

---

#### 4. `ts_repos_monthly.csv` (37,069 rows)

Monthly time series of activity and code quality metrics for treatment repositories. One row per (repository, month).

**columns:**
- `month`, `repo_name`, `latest_commit` : identifiers
- `agent` : boolean: was at least one PR in this month authored by an agent?
- `commits`, `lines_added`, `lines_removed`, `contributors`, `stars`, `issues`, `issue_comments`, `age` : activity metrics
- `ncloc`, `bugs`, `vulnerabilities`, `code_smells`, `duplicated_lines_density`, `comment_lines_density`, `cognitive_complexity`, `technical_debt` : SonarQube code quality metrics

> **Usage:** Raw monthly time series for treatment repositories, used in `AdoptionTimeAnalysis.Rmd` and as a building block for `panel_event_monthly.csv`.

---

#### 5. `ts_repos_control_monthly.csv` (49,095 rows)

Same structure as `ts_repos_monthly.csv` but for **control** repositories. Note: lacks the `software_quality_maintainability_remediation_effort` column present in the treatment file.

**columns:** Identical to `ts_repos_monthly.csv` (minus one quality column).

> **Usage:** Provides the control group's pre- and post-period metrics, enabling the parallel-trends assumption check and DiD estimation.

---

#### 6. `agent_first.txt` (400 lines)

 A plain-text list of repository names (one per line) classified as **Agent-First (AF)** — these repositories adopted a coding agent with no prior evidence of AI IDE usage (e.g., no Cursor configuration files detected before adoption).

> ** Usage:** Used to split the treatment group into AF vs. IF sub-groups for the heterogeneous treatment effect analysis.

---

#### 7. `ide_first.txt` (116 lines)

A plain-text list of repository names classified as **IDE-First (IF)** — repositories that had prior evidence of AI IDE usage (e.g., Cursor `.cursorrules` files) before adopting a coding agent.

> **Usage:** Counterpart to `agent_first.txt`. Allows comparison of agent impact between repos that are "clean" adopters vs. those already using AI-assisted IDEs.

---

## Tabular summary and origin of Files

The paper's README explicitly states that data collection and processing scripts are **adapted from the replication package of He et al. (MSR '26)** — the Cursor AI study hosted on Zenodo. The original AIDev dataset (from that package) provides the raw GitHub event and PR data, as well as SonarQube-based code quality metrics.

The authors of this paper **added or constructed** the following on top of the original data:

| File | Origin |
|---|---|
| `repos_with_details.csv` | Authors constructed  |
| `panel_event_monthly.csv` | Authors constructed |
| `matching.csv` | Authors constructed |
| `agent_first.txt` / `ide_first.txt` |Authors constructed |
| `ts_repos_monthly.csv` / `ts_repos_control_monthly.csv` | Authors constructed from original AIDev|

None of these processed files are provided directly in the original AIDev dataset
