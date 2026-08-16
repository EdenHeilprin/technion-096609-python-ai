# Privacy and research-data policy

Status: working course policy draft; institutional and study-specific rules take precedence

## Default rule

Use synthetic or explicitly approved public data for course exercises, demonstrations, public repositories, and ordinary AI queries.

If you are uncertain whether material may be shared with a person, repository, or AI service, do not upload it. Ask the instructor privately using a synthetic/minimal description.

## Data categories

| Category | Examples | Public repository | Ordinary AI service | Course use |
|---|---|---:|---:|---|
| Synthetic | Invented participant `SYN001`, generated trial rows | Yes | Yes | Preferred default |
| Approved public | Open dataset with compatible license and no restricted fields | Usually; follow license | Only if terms permit | Instructor confirms source/attribution |
| De-identified but real | Study export with direct identifiers removed | No by default | No by default | Requires explicit authorization and approved storage/tools |
| Identifiable or confidential | Names, emails, IDs, consent, sensitive free text, unpublished/private study data | No | No | Not used in ordinary course workflows |
| Credentials/secrets | Passwords, API keys, tokens, private access links | Never | Never | Store only through approved secure methods |

Removing a name does not automatically make a dataset anonymous. Combinations of demographics, dates, text responses, location, condition, or rare behavior may still identify someone.

## Synthetic means synthetic

Do not paste a real row and merely replace the participant's name. Create a minimal invented example that preserves the technical structure without preserving the person's distinctive values or text.

Good course identifiers look like `SYN001`, `PILOT_A`, or `TEST_CONDITION_2`. Do not use a student ID, national ID, phone number, email address, or realistic credential as an exercise input.

## Public GitHub boundary

The public course repository may contain:

- original course notes and examples;
- synthetic/public licensed data;
- starter code and public tests;
- released solutions when intentionally approved;
- documentation and links.

It must not contain:

- student grades, submissions, or identity mappings;
- identifiable or confidential research data;
- credentials, private links, or environment-secret files;
- hidden tests or unreleased solutions;
- copyrighted papers/materials without redistribution permission;
- private student or collaborator content without explicit permission.

Student projects are private by default. Making a capstone public is optional and requires a privacy/licensing review.

## Safe error sharing

When requesting help:

1. reproduce the error with a small synthetic input when possible;
2. copy the full error as text;
3. remove usernames and identifying folder names if they reveal sensitive information;
4. show only the smallest relevant code/configuration;
5. check screenshots for browser tabs, emails, tokens, and participant rows.

Do not weaken the technical question so much that it becomes impossible to diagnose; replace sensitive details with structurally equivalent synthetic values.

## Data-minimization rule for course tasks

Collect, store, and print only the information the program genuinely needs. An exercise about validation may use a fictional course code rather than a national/student identifier. An experiment may use neutral participant codes rather than names. Feedback should be neutral rather than infer titles or gender from demographic fields.

## Incident response

If protected material is accidentally committed, uploaded, or pasted:

1. stop sharing and do not create further copies;
2. contact the instructor privately immediately;
3. revoke/rotate exposed credentials;
4. remove access using the relevant repository/service procedure;
5. remember that deleting the latest GitHub file may not remove it from history;
6. follow institutional/data-owner reporting instructions.

Do not paste the exposed content into a public forum to ask how to remove it.

## Capstone rule

Capstones use synthetic or explicitly approved pilot data. Reimplementing a published method does not authorize redistributing its participant data, instruments, stimuli, paper, code, or proprietary survey content. Cite and link to sources, respect licenses/permissions, and document any adaptation.
