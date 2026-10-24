<<<<<<< HEAD
# Personal Assistant — learning-oriented starter

A **portable, voice-first hybrid AI assistant** in early development.
Planned: local Kokoro speech synthesis and interchangeable local/remote
language models. This repository currently contains **only a permission
policy prototype**; it is not a functioning assistant.

## Development approach

- Write readable, commented Python; explain *why* code exists.
- Keep the smallest working checkpoint at every commit.
- Leave genuine learning exercises as `TODO` comments, **not intentional bugs**.
- The developer owns design decisions and implements learning exercises.
- Keep public source code separate from personal data and API credentials.

## Contents

- `core/permissions.py` — dependency-free permission decisions.
- `tests/test_permissions.py` — standard-library tests.
- `docs/LEARNING_NOTES.md` — exercises and design questions.
- `.gitignore` — excludes private data, downloaded models, and caches.

## Setup later (Windows 11)

Install a fresh supported Python 3 version from python.org. Confirm with:

```powershell
py --version
```

Then, from this folder:

```powershell
py -m venv .venv
.venv\Scripts\python.exe -m unittest discover -s tests -v
```

No third-party packages are required for this first checkpoint.
The virtual environment is local to your machine and should not be committed.

## Safety boundary

`check_permission` does **not** sandbox anything, authenticate a user, or
intercept tool calls. A future controller must enforce decisions before
performing actions. `user_approved` is a placeholder for a trusted UI signal,
never a value chosen by the language model.

## Suggested first Git commit

`Initialize documented permission prototype and learning tests`

Before publishing, review staged files to ensure no secrets or private data
are included. `.gitignore` is a safeguard, not a guarantee.

## Project purpose and public portfolio

This is a **noncommercial, personal-use project** built as a Python learning
exercise and a public software-development portfolio / résumé demonstration.
The goal is to show architectural decisions, readable documentation, tests,
and incremental engineering progress. The application is intended for its
creator's own use; it is **not a commercial product or hosted public service**.

The repository is public so others can inspect the source code. Personal
conversations, local memory, credentials, and model files are **not** public.
A public source repository does not imply that the running assistant is public.

**License status:** No redistribution or commercial-use license has been
selected yet. A personal-use statement is not a substitute for a license;
third-party model and dependency licenses must be reviewed separately.

## Repository access boundaries

- Grant collaborators or connected AI tools access to **this repository only**,
  using selected-repository permissions where supported.
- Do not grant account-wide access to unrelated GitHub repositories.
- Prefer the minimum required permissions; start with read-only access and
  enable write access only for explicitly approved work.
- Review any requested GitHub authorization scopes before approving them.
- Repository access configuration happens in GitHub; this README does not
  enforce or grant permissions.

## Security roadmap (not yet implemented)

This is an educational prototype, **not a hardened or security-audited agent**.
Future work includes:

- Trusted, user-visible approval for consequential tool actions.
- Tool allowlists and operating-system-enforced limits / sandboxing.
- Secure handling of API keys and private configuration.
- Separation of public source, private memory, and logs.
- Tests for unauthorized access, prompt injection, and approval bypasses.
- Dependency review and a documented process for reporting vulnerabilities.

**Current limitation:** `core/permissions.py` is only a policy demonstration;
it does not enforce operating-system permissions or isolate processes.
Do not connect it to unrestricted file, shell, or network execution.
=======
# Personal AI Assistant

## Project Overview

This repository documents the development of my personal artificial intelligence assistant.

The primary purpose of this project is to design, develop, and maintain a lightweight, portable, voice-first AI assistant intended for my own personal use.

Additionally, this repository serves as a public programming portfolio, allowing potential employers, fellow developers, friends, and other interested individuals to review my work, technical knowledge, and progression as a software developer.

The project is being developed as both a practical application and an opportunity to expand my knowledge of Python, artificial intelligence integration, software architecture, and application security.

## Project Goals

The primary development objectives include:

- **Voice-first interaction:** Prioritize natural spoken communication over traditional text-based interfaces.
- **Customizable voice synthesis:** Develop a distinctive, locally generated voice with adjustable vocal characteristics.
- **Modular architecture:** Support interchangeable local and cloud-based language models.
- **Portability:** Minimize hardware requirements and avoid unnecessary dependence on dedicated graphics hardware.
- **Privacy and security:** Maintain user control over personal information, system permissions, and AI-assisted actions.
- **Independent learning:** Develop and maintain a clear understanding of the underlying code and architecture.

## Development Status

**Status: Early Development**

This project is currently in its foundational development stage. Features described in the project goals are planned objectives and should not be considered fully implemented.

Development will proceed incrementally, with an emphasis on readable code, documentation, testing, and maintainability.

## Security and Privacy

The assistant is intended to operate with clearly defined permission boundaries.

Future development will include additional security measures to restrict unauthorized actions, protect sensitive information, and ensure that consequential operations remain subject to human approval.

Security-related functionality will be documented and tested as it is implemented.

## Project Ownership and Usage Permissions

This project is intended exclusively for personal, noncommercial use and is made publicly visible for portfolio evaluation and educational reference.

All original source code and project materials remain the intellectual property of their respective copyright holders.

**No general permission is granted to copy, modify, redistribute, or commercially use my original source code without obtaining prior authorization.**

Visitors are welcome to inspect the repository and contact me with suggestions, questions, or constructive feedback.

GitHub's platform terms may permit certain activities, including viewing and forking public repositories. Public availability does not otherwise constitute a general open-source license.

**All rights reserved unless otherwise explicitly stated.**

## Future Development

### AI-Assisted Development

This project is developed with the assistance of OpenAI's ChatGPT as a supplementary learning, research, and development tool.

AI assistance is used for technical explanations, architectural planning, debugging, documentation, and generating portions of the initial code foundation.

The project is independently directed and maintained by me, with an emphasis on understanding the underlying implementation, developing my Python programming skills, and progressively taking greater responsibility for the codebase.

All AI-assisted contributions are subject to my review, testing, and revision.

Planned improvements include local speech recognition, configurable conversational models, persistent memory, expanded security controls, and further voice customization.

This README will be updated as development progresses to reflect implemented features, architectural decisions, and project milestones.
>>>>>>> e6b7eaf5e90656442a07180bb95777d7f9be108d
