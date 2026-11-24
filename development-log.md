# Development log

One entry per milestone (add more if useful). Fill in as you go and commit
the update with the work it describes. For AI assistance, name the tool and
what it was used for; keep prompts and outputs private.

## Milestone 1 – Initial setup
- **Date (UTC):** 2026-11-24
- **Work completed:** Created the GitHub repository and a Google Cloud Shell
  working environment. Added the project structure, pinned runtime and test
  dependencies (requirements.txt, requirements-dev.txt), .gitignore,
  .env.example with placeholder values, pytest.ini, and an initial README
  covering installation, configuration and running locally. Added the
  configuration module (app/config.py) and the clock module (app/clock.py).
  Created a virtual environment, installed the dependencies and checked that
  both modules import correctly.
- **Key decision or problem:** All settings, including the JWT signing secret,
  are read from environment variables rather than written in the code. This
  keeps the secret out of GitHub and lets the same Docker image run locally,
  on the VM and on GKE with different configuration. The app refuses to start
  if the secret is missing or shorter than 32 characters. Time is read through
  a clock object so that tests can control it instead of waiting for posts to
  expire.
- **Commits:** (link added after pushing)
- **Sources / assistance:** Claude (Anthropic) generated the initial code and
  setup instructions; I reviewed and ran each file before committing. Week 6
  FastAPI container tutorial for project layout and configuration.

## Milestone 2 – Application development
- **Date (UTC):**
- **Work completed:**
- **Key decision or problem:**
- **Commits:**
- **Sources / assistance:**

## Milestone 3 – Automated testing
- **Date (UTC):**
- **Work completed:**
- **Key decision or problem:**
- **Commits:**
- **Sources / assistance:**

## Milestone 4 – Containerisation
- **Date (UTC):**
- **Work completed:**
- **Key decision or problem:**
- **Commits:**
- **Sources / assistance:**

## Milestone 5 – Kubernetes deployment
- **Date (UTC):**
- **Work completed:**
- **Key decision or problem:**
- **Commits:**
- **Sources / assistance:**