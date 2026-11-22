# Teaching Text Cleaning in Python

**Presenter** · yishai kandler

Keep one question visible throughout the lesson: “How many students meant the same thing?” By the end, students should recognize which string method handles each spelling difference, trace a chain, and interpret the resulting counts.

## Teaching sequence

| Minutes | Display | Say, ask, or do |
| --- | --- | --- |
| 0–5 | Opening Kahoot | Give about 30 seconds per question. Ask students to remember one guess they would like to revisit. |
| 5–9 | Lesson README, then VS Code with demo.py | Show the three yes answers. Ask someone to count exact matches, then count by meaning. Reveal one demo output line at a time. |
| 9–13 | README method table and practice.py exercise 1 | Ask which spaces should survive in a two-word label. Let students edit and rerun. Expected value: `'study group'`. |
| 13–17 | Exercise 2 | Have a student predict the result for GEMINI. Run it and ask whether lowercase conversion would also remove punctuation. Expected: `'gemini'`. |
| 17–21 | Exercise 3 | Ask how many marks disappear in one call. Run it with an empty replacement. Expected: `'yes'`. |
| 21–25 | Exercise 4 | Give a minute of quiet work. Ask a volunteer to read the chain from left to right. Expected: `'chatgpt'`. |
| 25–40 | README checkpoints, then starter.py and terminal | Use 3 minutes to inspect raw labels, 6 to edit, 3 to compare totals, and 3 for interpretation and questions. Ask which labels merged and whether removing punctuation suits free text. |
| 40–45 | Closing Kahoot | Replay the original five questions in the same order. Invite one explanation of a changed answer. |
| 45–50 | VS Code with regex_bonus.py, time permitting | Predict the result for the parenthesized number. Run the file. Each of three lines reads `0541234567`. Ask what the pattern removes. |

## Answer desk

The live demo turns `' CLAUDE!! '` into `'CLAUDE!!'`, then `'claude!!'`, then `'claude'`. Point to the original printed again. If a learner calls a method and later prints the old variable, ask where the return value went.

Show [the four practice answers](practice_solution.py) after students have tried them. To display the completed survey from the lesson folder, run `python -m instructor.survey_solution`. The [survey answer](survey_solution.py) uses the same tally as the starter. Expect 10 distinct yes/no spellings to become two (32 yes and 8 no). The 19 tool spellings become four (16 chatgpt, 8 claude, 8 gemini, 8 none). Ask a student to add either set of counts.

If spaces persist, compare the quoted output with the input and check whether students saved the result. If exclamation marks turn into spaces, check the difference between `""` and `" "`. If runs look identical, save the edited file and confirm the terminal command names it. For interpreter or file-path errors, use [Get ready](../README.md#get-ready).

If running behind, demonstrate exercise 4 aloud and give students the first assignment in the survey function. Allow time to interpret one column and take a question. Start the closing quiz at minute 40. Drop the bonus if the class ends at minute 45.

## Quiz for both rounds

During preparation, manually enter [the question bank](kahoot_questions.csv) into one Kahoot. Use that same quiz twice with question and answer order fixed. If Kahoot is unavailable, read each question and its choices below, take an A–D vote, then discuss the key.

**1. What is the main purpose of text cleaning?**

- A. `To translate text`
- B. `To make text consistent`
- C. `To make Python run faster`
- D. `To delete all text`

**B.** Consistent labels let equivalent answers count together.

**2. What does .strip() remove by default?**

- A. `All spaces everywhere`
- B. `Spaces at the beginning and end`
- C. `Capital letters`
- D. `Punctuation marks`

**B.** It trims surrounding whitespace, including tabs. Interior spaces stay.

**3. What is the output of "ChatGPT!".lower()?**

- A. `chatgpt`
- B. `ChatGPT!`
- C. `chatgpt!`
- D. `Error`

**C.** Only the letters change case.

**4. What is the output of "yes!!!".replace("!", "")?**

- A. `yes!!`
- B. `YES`
- C. `yes`
- D. `yes!`

**C.** Each exclamation mark is replaced by an empty string.

**5. What is the output of "  YES!!  ".strip().lower().replace("!", "")?**

- A. `YES!!`
- B. `yes!!`
- C. `"  yes  "`
- D. `yes`

**D.** The steps remove edge spaces, lowercase the letters, then remove both marks.
