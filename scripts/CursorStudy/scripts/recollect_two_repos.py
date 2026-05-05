#!/usr/bin/env python3
"""
Re-collect GitHub data for 2 randomly selected repos from repos.csv
and compare the new values against the original dataset.

Usage:
    python scripts/recollect_two_repos.py

Output:
    - data/repos_recollected.csv  : new data for the 2 selected repos
    - Printed diff to stdout
"""

import os
import sys
import logging
import pandas as pd
from github import Github, GithubException, Auth
from dotenv import load_dotenv

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler(sys.stdout)],
)

ORIGINAL_CSV = "data/repos.csv"
OUTPUT_CSV = "data/repos_recollected.csv"
RANDOM_SEED = 42


def get_github_token():
    load_dotenv(override=True)
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError(
            "GitHub token not found. Set GITHUB_TOKEN in your .env file."
        )
    return token


def fetch_repo_data(g, repo_name):
    """Fetch current metrics for a single repo via GitHub API."""
    logging.info("Fetching data for %s ...", repo_name)
    try:
        repo = g.get_repo(repo_name)
    except GithubException as e:
        logging.error("Could not fetch %s: %s", repo_name, e)
        return None

    data = {
        "repo_name": repo.full_name,
        "repo_stars": repo.stargazers_count,
        "repo_forks": repo.forks_count,
        "repo_created": repo.created_at.isoformat() if repo.created_at else None,
        "repo_updated": repo.updated_at.isoformat() if repo.updated_at else None,
        "repo_description": repo.description,
    }

    # issues count
    try:
        data["repo_issues"] = repo.get_issues(state="all").totalCount
    except GithubException as e:
        logging.warning("issues error for %s: %s", repo_name, e)
        data["repo_issues"] = None

    # pull requests count
    try:
        data["repo_pulls"] = repo.get_pulls(state="all").totalCount
    except GithubException as e:
        logging.warning("pulls error for %s: %s", repo_name, e)
        data["repo_pulls"] = None

    # commit count
    try:
        data["repo_commits"] = repo.get_commits().totalCount
    except GithubException as e:
        logging.warning("commits error for %s: %s", repo_name, e)
        data["repo_commits"] = None

    # contributor count
    try:
        data["repo_contributors"] = repo.get_contributors().totalCount
    except GithubException as e:
        logging.warning("contributors error for %s: %s", repo_name, e)
        data["repo_contributors"] = None

    # repo size (KB)
    try:
        data["repo_size"] = repo.size
    except GithubException as e:
        logging.warning("size error for %s: %s", repo_name, e)
        data["repo_size"] = None

    # language breakdown
    try:
        langs = repo.get_languages()
        # Filter out non-integer entries (e.g. stray 'url' key from API)
        langs = {k: v for k, v in langs.items() if isinstance(v, int)}
        if langs:
            data["repo_languages"] = "; ".join(
                f"{lang}: {bytes_}" for lang, bytes_ in langs.items()
            )
            data["repo_primary_language"] = max(langs.items(), key=lambda x: x[1])[0]
        else:
            data["repo_languages"] = None
            data["repo_primary_language"] = None
    except GithubException as e:
        logging.warning("languages error for %s: %s", repo_name, e)
        data["repo_languages"] = None
        data["repo_primary_language"] = None

    return data


def print_comparison(original_row, new_row):
    """Print a field-by-field diff between original and new data."""
    cols = [
        "repo_stars", "repo_forks", "repo_created", "repo_updated",
        "repo_description", "repo_issues", "repo_pulls", "repo_commits",
        "repo_contributors", "repo_size", "repo_languages", "repo_primary_language",
    ]
    changed = []
    unchanged = []

    for col in cols:
        orig_val = original_row.get(col, "N/A")
        new_val = new_row.get(col, "N/A")
        # Normalize for comparison (floats stored as int in original)
        try:
            if float(orig_val) == float(new_val):
                unchanged.append(col)
                continue
        except (TypeError, ValueError):
            pass
        if str(orig_val).strip() == str(new_val).strip():
            unchanged.append(col)
        else:
            changed.append((col, orig_val, new_val))

    print(f"\n{'='*60}")
    print(f"Repo: {new_row['repo_name']}")
    print(f"{'='*60}")

    if changed:
        print("\n  CHANGED FIELDS:")
        for col, orig, new in changed:
            print(f"    {col}:")
            print(f"      Original : {orig}")
            print(f"      New      : {new}")
            try:
                delta = float(new) - float(orig)
                print(f"      Delta    : {delta:+.0f}")
            except (TypeError, ValueError):
                pass
    else:
        print("\n  No changes detected.")

    print(f"\n  Unchanged fields: {', '.join(unchanged)}")


def main():
    # Load original data
    if not os.path.exists(ORIGINAL_CSV):
        logging.error("Original data file not found: %s", ORIGINAL_CSV)
        sys.exit(1)

    original = pd.read_csv(ORIGINAL_CSV)
    logging.info("Loaded %d repos from %s", len(original), ORIGINAL_CSV)

    # Randomly sample 2 repos
    sampled = original.sample(n=2, random_state=RANDOM_SEED).reset_index(drop=True)
    logging.info("Randomly selected repos (seed=%d):", RANDOM_SEED)
    for name in sampled["repo_name"]:
        logging.info("  - %s", name)

    # Connect to GitHub
    token = get_github_token()
    g = Github(auth=Auth.Token(token))
    rate = g.get_rate_limit()
    logging.info("GitHub rate limit: %d/%d remaining", rate.rate.remaining, rate.rate.limit)

    # Fetch fresh data for each selected repo
    new_rows = []
    for _, row in sampled.iterrows():
        result = fetch_repo_data(g, row["repo_name"])
        if result:
            new_rows.append(result)

    if not new_rows:
        logging.error("No data collected. Check your GitHub token and network.")
        sys.exit(1)

    new_df = pd.DataFrame(new_rows)
    new_df.to_csv(OUTPUT_CSV, index=False)
    logging.info("Saved recollected data to %s", OUTPUT_CSV)

    # Print comparison
    print("\n\n*** FIELD-BY-FIELD COMPARISON (Original vs. Recollected) ***")
    print(f"Original data collected: ~March 2025 (per repo_updated timestamps)")
    print(f"New data collected      : today (May 2025)")

    for _, new_row in new_df.iterrows():
        name = new_row["repo_name"]
        orig_matches = sampled[sampled["repo_name"] == name]
        if orig_matches.empty:
            logging.warning("No original row found for %s", name)
            continue
        orig_row = orig_matches.iloc[0].to_dict()
        print_comparison(orig_row, new_row.to_dict())

    print("\n\nDone. See data/repos_recollected.csv for the full new dataset.")


if __name__ == "__main__":
    main()
