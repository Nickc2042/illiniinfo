# Finish the GitHub setup

This package contains the foundation only. Completing these steps publishes the foundation; it does not implement the project.

## 1. Create the repository

On GitHub, create a repository under **Nickc2042** with these settings:

| Setting | Initial value |
| --- | --- |
| Repository name | `illiniinfo` |
| Description | UIUC student information retrieval project comparing TF-IDF and BM25 over official academic sources. |
| Visibility | Private initially; confirm course submission access before final submission |
| Default branch | `main` |
| Initialize with README | Off; this package already includes one |
| Add .gitignore | None; this package already includes one |
| License | None until the team decides |

## 2. Upload the foundation

Install Git if needed. Extract `IlliniInfo_Foundation.zip`, open a terminal inside the extracted `illiniinfo` folder, and run:

```bash
git init -b main
git add .
git commit -m "Set up IlliniInfo project foundation"
git remote add origin https://github.com/Nickc2042/illiniinfo.git
git push -u origin main
```

These commands assume the repository is newly created and empty. If you already created a repository with files, clone it and copy this package into that clone instead of creating a second Git history. Sign in through Git's normal authentication flow if prompted.

After pushing, check that README.md, docs/, and .github/ are visible on GitHub. Update the pending repository URL in README.md and docs/proposal.md.

## 3. Add the team

Ask Kayetan and Yoyo for their exact GitHub usernames. Invite those accounts as collaborators through the repository's access settings. Do not infer usernames from their names. Each teammate must accept the invitation.

Teammates can then clone the repository:

```bash
git clone https://github.com/Nickc2042/illiniinfo.git
cd illiniinfo
```

## 4. Organize the work

- Turn the items in [backlog.md](backlog.md) into GitHub issues when implementation is authorized. Lead names are tentative; assign accounts after usernames are confirmed.
- Use milestones: Scope agreed, Corpus ready, Retrieval ready, Interface ready, Evaluation complete, Submission ready. Add dates after confirming the course schedule.
- If useful, create a GitHub Project with Backlog, Ready, In progress, In review, and Done columns.
- Use short task branches and pull requests. Have a teammate review changes before merging.
- Where your repository plan supports it, configure a rule for `main` requiring a pull request and one approval. No status checks exist yet, so do not require a nonexistent check.

The collaborator invitations, issues, milestones, board, and branch rules are manual follow-up steps unless explicitly confirmed as completed on GitHub.

## 5. Before implementation

Resolve the program and catalog-year decisions in [decisions.md](decisions.md). Python 3.12 is proposed, but the team should agree on the interpreter before adding dependencies. No virtual environment, package installation, data download, or Streamlit launch is needed for this foundation.
