# Structured vs. Unstructured Data

**Module 0: Foundations**

**Learning Objectives:**
- Explain the difference between structured and unstructured data
- Classify a real file as structured or unstructured, with a reason
- Justify that call using what you actually see in the file

## Scenario

A teammate hands you a folder of files and asks, "can you tell me what shape this data is in before we plan how to clean it?" You'll practice making that call yourself - sorting real files into structured and unstructured, and being able to defend the call with what's actually in the file, not a guess.

*Reminder: type the commands inside the shaded code blocks below into your own terminal.*

## Look at a Structured File

*Context: Same file from the environment-setup lecture — every row has the exact same columns: country, year, iso_code, and so on.*

**AI Mode:** Try Without AI, Then Tutor If Stuck

*Complete the TODOs below as you work through this step.*

```bash
# TODO: preview the first 3 lines of the structured file
head -n 3
```

## Look at Unstructured Text

*Context: A single free-text sentence — no columns, no fixed fields to compare row to row.*

**AI Mode:** Try Without AI, Then Tutor If Stuck

*Complete the TODOs below as you work through this step.*

```bash
$ echo "Great class today, the git demo finally clicked for me!" > note.txt
# TODO: print the contents of note.txt to the screen
cat note.txt
```

## Pulling a Field Out of Unstructured Text

*Context: grep searches text for a pattern — here, finding the word "git" inside the free-text note.*

**AI Mode:** Try Without AI, Then Tutor If Stuck

*Complete the TODOs below as you work through this step.*

```bash
# TODO: search note.txt for lines containing "git"
grep "git" note.txt
```

## Row Count vs. Word Count

*Context: wc -l counts lines (rows) — a natural unit for structured data. wc -w counts words — a more natural unit for free text.*

**AI Mode:** Try Without AI, Then Tutor If Stuck

*Complete the TODOs below as you work through this step.*

```bash
# TODO: count how many lines are in the structured file
wc -l ../../data/energy_sample.csv 
# TODO: count how many words are in the unstructured note
wc -w note.txt
```