# Tech Stack / Career Recommender

A content-based recommendation system that suggests the **Top 3 best-matching job roles** from the skills a user enters. Built for the **DecodeLabs AI Internship, Project 3: AI Recommendation Logic**.

## What it does

1. The user enters **at least 3 skills** (e.g. `python, cloud computing, automation`).
2. The program compares those skills against a dataset of job roles.
3. It prints the **Top 3 roles** with a match percentage.

### Example

```
Enter at least 3 skills (comma-separated): python, cloud computing, automation

Top 3 recommendations:

1. Cloud Architect - 64.6% match
2. DevOps Engineer - 16.6% match
3. Cybersecurity Analyst - 8.9% match
```

## How it works

This project uses **content-based filtering**: it matches the user's skills to the attributes of each job role, so it needs no data from other users.

| Step | What happens | Tool |
|------|--------------|------|
| 1. Ingestion | Read the skills, clean them (trim, lowercase), require at least 3 | Python |
| 2. Vectorization | Turn each role's skills into a TF-IDF vector over one shared vocabulary | `TfidfVectorizer` |
| 3. Scoring | Measure the angle between the user vector and every role vector | `cosine_similarity` |
| 4. Sorting | Order roles from highest to lowest score | `pandas.sort_values` |
| 5. Filtering | Keep only the Top 3 (roles with a 0% match are dropped) | `.head(3)` |

### Why TF-IDF?

Plain 1/0 matching treats every skill equally. TF-IDF gives **rare, specific skills more weight** (like `pandas` or `kubernetes`) and **common skills less weight** (like `python`), so the results reflect what makes each role distinctive.

### Why cosine similarity?

It compares the **direction** of two vectors, not their size, so a role with a long skills list is not unfairly favoured over a short one. A score near 1 is a strong match, and 0 means nothing in common.

### Cold start handling

If none of the entered skills exist in the dataset (for example `singing, dancing, cooking`), the user vector is all zeros and every score would be 0. The program detects this and shows a friendly message with example skills instead of meaningless results. Skills that are not recognized are also reported to the user.

## Project structure

```
.
├── project_3.py                   # main script
├── raw_skills.csv                 # dataset: job roles and their skills
└── README.md
```

## Dataset

`raw_skills.csv` has two columns:

| Column | Description |
|--------|-------------|
| `role` | Job role name |
| `skills` | Space-separated, lowercase skills for that role |

Skill names are kept **consistent and lowercase** so the shared vocabulary stays clean. You can add more roles by adding rows.

## How to run

### Locally

Keep `project_3.py` and `raw_skills.csv` in the same folder, then run:

```bash
pip install pandas scikit-learn
python project_3.py
```

Enter your skills when prompted.

### Google Colab

1. Upload `project_3.py` and `raw_skills.csv` using the folder icon in the left sidebar.
2. Run in a cell:

```python
!python project_3.py
```

## Test cases

| Input | Expected behaviour |
|-------|--------------------|
| `python, cloud computing, automation` | Cloud Architect ranked first |
| `java, sql, apis` | Backend Developer ranked first |
| `python, sql, rust` | Notes that `rust` is not recognized, still returns results |
| `python, sql` | Asks for at least 3 skills |
| `singing, dancing, cooking` | Cold start fallback message |

## Tech stack

- Python
- pandas
- scikit-learn (`TfidfVectorizer`, `cosine_similarity`)
- Developed in Google Colab

## Limitations and future improvements

- The dataset is small (10 roles), so lower-ranked results can be weak matches. Adding more roles will improve quality.
- Multi-word skills such as `machine learning` are split into single words by default. Using n-grams (`ngram_range=(1, 2)`) could treat them as one skill.
- Possible extensions: a "why this matched" explanation, user ratings on results, and a Streamlit web interface.

## Author

**Sree Harsha**
GitHub: [SreeHarsha733](https://github.com/SreeHarsha733)
