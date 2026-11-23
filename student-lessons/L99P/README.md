# GitHub: Follow a Change from File to Pull Request

**Presenters:** Lisa Passov and Tal Ayala Shafran  
**Length:** About 50 minutes, including the live tour, activities, questions, and discussion.

Ever had a file called `project_final_final_really-final.py`? GitHub helps teams keep track of project files and changes without naming every new version “final.” In this lesson, you’ll follow the journey of a small proposed change and see how a pull request gives people a place to review and discuss it before it joins the shared version.

The goal is familiarity, not mastery. You do not need to know Git commands, write code, or have a GitHub account.

## By the end of this lesson

- Find a repository, a file, and that file’s history on GitHub.
- Explain what a pull request proposes and what a reviewer can check.

## Get ready

1. Open the public [octocat/Hello-World demo repository](https://github.com/octocat/Hello-World) in a browser tab. You should see the repository name, a **Code** tab, and its short README, “Hello World!”
2. Open the README’s [file history](https://github.com/octocat/Hello-World/commits/master/README) in another tab. You should see a list of saved changes. Select a commit to compare versions: the **diff** highlights added and removed lines.
3. Open GitHub’s [Hello World pull request tutorial](https://docs.github.com/en/get-started/using-github/hello-world) in another tab. Find its steps for creating a branch, committing a change, opening a pull request, and merging. Follow the illustrated workflow as a tour; you do not need to create anything.

There is nothing to install or run for this noncoding lesson. The live example is the read-only browser tour above; no sign-in is needed.

## A worked example

Imagine your team is keeping the instructions for a study in one shared project folder. On GitHub, that home for the files and their change history is called a **repository**. The team’s current shared version usually lives on a branch called `main`.

Now suppose you spot a typo. You probably don’t want to rewrite the shared instructions while everyone else is using them (or start a new file called `instructions_FIXED_FINAL_v8`). Instead, you make a **branch**: a separate line of work based on the current version. You can edit there while `main` stays as it is.

When you’ve made a useful change, you save a **commit**. Think of it as a checkpoint in the project’s history, with a short message such as “Clarify the start button instruction.” If you make several commits, the team can follow the steps you took.

When you are ready for another pair of eyes, open a **pull request (PR)** to propose bringing your branch’s changes into `main`. The PR lays out what changed, shows the added and removed lines, and gives reviewers a place to ask questions or suggest edits. You can revise your branch after feedback. Opening a PR is like putting your draft on the review table; it does not mean the change has been accepted. If the team agrees, someone merges the change into `main`, and it becomes part of the shared version.

**The journey:** shared repository → branch for your work → commit checkpoints → pull request for review → merge if accepted.

Now let's follow the rote of our lesson PR!

1. **The project:** On the repository page, we can spot the **Code** tab for example. A repository is the home for related project files and their history.
2. **One file:** Since we are interested in the journey of our PR we can go to the **Pull requests** tab.
3. **Its history:** We can now go to the **Commits** tab where each entry is a commit with a message and author. Clicking on one of the commits or on **Files changed** will show a comparison between versions: added lines are green and removed lines are red. This helps answer “what changed?”
4. **And now we wait:** If the team accepts the proposal, it can be merged into `main`. The PR is the review table between “I changed this” and “let’s add it to the shared version.”


## Try it yourself

### Pull request detective

Think about the following questions for a few minutes, then we will compare your answers with those of the group.

Imagine a fictional repository called “Shape Study.” Its README has an instruction: **“Press Begin.”** Mira makes a branch and changes the line to **“Select Begin.”** She records the edit in a commit and opens a pull request to `main`. The PR shows one red line (`Press Begin`) and one green line (`Select Begin`). A reviewer comments: “The button in the study says **Start**. Should the instruction match the button?” Mira replies and updates her proposed change.

1. Which branch is the proposed edit on: Mira’s branch or `main`?
2. What clues can the reviewer use to understand and check this change?
3. Did the change enter `main` just because Mira opened a PR? What would need to happen next?

<details>
<summary>Pull request detective answers and discussion</summary>

1. The proposed edit is on Mira’s branch. In this example, `main` is still the shared version.
2. The reviewer can read the PR description and discussion and inspect the diff: the red removed wording and green replacement. The comment asks whether the instruction matches the actual button.
3. No. The PR is a proposal. If the team accepts it, someone with permission merges it into `main`.

**Discuss:** Which wording would you suggest: “Select Start,” “Press Start,” or something else? Why? A useful instruction matches the button text and tells the reader what action to take.

</details>

### Final activity: GitHub true or false?

Let's finish with a short game of four behind-the-scenes claims!
The claims are worded carefully: a true headline can still have an exaggerated detail.

**1. Code on Mars:** NASA’s Ingenuity helicopter used F´ (F Prime), an open-source flight-software framework developed at NASA’s Jet Propulsion Laboratory. Its source code is available on GitHub.

<details>
<summary>Reveal answer</summary>

**True, with a small wording check.** NASA says the open-source F Prime framework powered Ingenuity. NASA’s project repository is publicly available on GitHub. That does not mean every line of the helicopter’s software was open source.

</details>

**2. A very chilly archive:** GitHub archived a snapshot of all its active public repositories from 2 February 2020 on special archival film, stored in a decommissioned coal mine in Svalbard as part of a project aiming to preserve the archive for 1,000 years.

<details>
<summary>Reveal answer</summary>

**True, with a scope check.** The vault stores a snapshot of active public GitHub repositories from 2 February 2020 on archival film in an Arctic mountain’s decommissioned coal mine. The 1,000 years is the archive program’s preservation goal.

</details>

**3. The swear-word timeout:** GitHub’s system automatically scans every commit message for English swear words and suspends the account for exactly 24 hours if it finds one.

<details>
<summary>Reveal answer</summary>

**False as stated.** GitHub’s published policy discusses possible restrictions for behavior that disrupts other users; it does not describe an automatic, blanket 24-hour suspension for swear words in commit messages.

</details>

**4. The sushi-and-pizza Octocat:** GitHub’s Octocat began as the logo for a San Francisco sushi-and-pizza delivery company. GitHub bought the design for $50 after that restaurant closed.

<details>
<summary>Reveal answer</summary>

**False.** GitHub’s early creative director says the founders purchased a stock illustration of a cat-octopus character by Simon Oxley. The sushi restaurant and $50 story are made up.

</details>


## Quick reference

| Tool or idea | What it does |
| --- | --- |
| Repository | A project space containing files and their recorded history. |
| Branch | A separate line of work that can change without immediately changing the shared branch. |
| Commit | A recorded snapshot of selected changes, usually with a short message. |
| Diff | A comparison that highlights additions and removals. |
| Pull request (PR) | A proposal to review and discuss changes before bringing them into another branch. |
| Merge | The step that incorporates accepted changes into another branch. |

**Tiny takeaway:** a PR asks, “Could we include this change?” A merge is what brings an accepted change in.

## Sources and further learning

- GitHub Docs, [Hello World: GitHub workflow tutorial](https://docs.github.com/en/get-started/using-github/hello-world) (branches, commits, pull requests, review, and merge).
- GitHub Docs, [About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories) (what repositories contain).
- GitHub Docs, [Viewing and understanding files](https://docs.github.com/en/repositories/working-with-files/using-files/viewing-and-understanding-files) (opening files and viewing their history).
- GitHub Docs, [About pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) (what a PR is and how discussion works).
- NASA Jet Propulsion Laboratory, [Open-source software powering Ingenuity](https://www.nasa.gov/missions/meet-the-open-source-software-powering-nasas-ingenuity-mars-helicopter/), and NASA’s [F´ source repository](https://github.com/nasa/fprime) (Mars game claim).
- GitHub Blog, [Arctic Code Vault](https://github.blog/open-source/maintainers/if-you-dont-make-it-beautiful-its-for-sure-doomed-putting-the-vault-in-githubs-arctic-code-vault/) (archive game claim).
- GitHub Docs, [Disrupting the experience of other users](https://docs.github.com/en/site-policy/acceptable-use-policies/github-disrupting-the-experience-of-other-users) (published platform policy referenced in the commit-message claim).
- Cameron McEfee, GitHub’s early creative director, [The Octocat—a nerdy household name](https://cameronmcefee.com/work/the-octocat/) (Octocat origin game claim).
- Live-tour example: [octocat/Hello-World](https://github.com/octocat/Hello-World) and its [README history](https://github.com/octocat/Hello-World/commits/master/README). The tour is read-only; the PR workflow is illustrated in GitHub’s official tutorial.

---

[Back to student-led lessons](../README.md) · [Back to the course](https://github.com/EdenHeilprin/technion-096609-python-ai)
