# Lab — Column-Typing & Collection-Concern Practice

**Skills assessed:** Data Literacy, Critical Thinking, Curiosity (see this lab's own `RUBRIC.md`)

**Estimated time:** ~100 minutes (10 min intro · 75 min collaborative work · 15 min shareout)

## Scenario

You've just joined a data team, and someone drops `data/energy_sample.csv` in your lap: country-level energy figures your team wants to use in a report next week. Nobody has documented it. Before a single chart gets made or a single number gets quoted, somebody has to say — out loud, with a reason — what each column actually holds, how much data is really in there, and what about the way it was collected should make a careful analyst cautious. Today that somebody is your group.

*Work with your group, but complete and push/commit your own copy of this lab — collaboration is encouraged, a shared submission isn't.*

## Your Objectives

- **Open the Raw File Before You Classify a Single Column**
  - *Same lab dataset from DATASET.md — a different file than the project's own co2-data, on purpose. Run every command from the module folder, so `data/energy_sample.csv` resolves.*

- **Preview Every Column's Actual Values — All Seven, Not Just the First Few**
  - *Hint: `cut` is new. It pulls specific columns out of a line: `-d,` says the columns are separated by commas, and `-f` says which ones you want.*

- **Classify All Seven Columns, Each With a Reason Drawn From the Data**

- **Confirm How Many Rows and How Many Countries You Actually Have**
  - *Hint: `sort` and `uniq -c` are new, and they work together: `uniq -c` counts repeats, but only ones sitting next to each other, so the values have to be sorted first.*

- **Check Whether Every Country Reports Every Column — Then Name Two Collection Concerns**

## Share Out

Two questions, in this order. First: how did your group figure out whether every country reports every column? Different groups almost certainly took different routes to the same file — compare them before deciding which you'd reach for next time. Second: which collection concerns did your group flag, and which single data-quality question did you sharpen out of them? Put each group's question up where everyone can read it, then ask the class which ones a real analyst could actually go answer — and which ones sound serious but can't be checked.

1. My group figured out whether every country reports every column by using the following command: 

```bash
cut -d ',' -f1 data/energy_sample.csv |sort|uniq -c| sort -nr
```

The output of this was the following:

```bash
7 Vietnam
7 United States 
7 Nigeria
7 Kenya
7 Japan
7 India
7 Germany
7 Canada
7 Brazil
7 Australia
```

Each country is reported the same number of times. However, after performing another command that pulled all info pertaining to a country, two countries were missing values. See the commands below:

```bash
awk -F ',' '$1=="Nigeria"' energy_sample.csv
awk -F ',' '$1=="Kenya"' energy_sample.csv
```

These two countries had missing values in the last two columns, but all other countries were fully populated across each column.

2. The collection concerns my group flagged were:

Why were there missing values for Kenya and Nigeria?

How were their `energy_per_capita` was populated if their `fossil_share_energy` and `renewables_share_energy` weren't recorded?

The single data-quality question we sharpened out of them was: why were only these two countries missing values for both types of energy consumption recorded?

### Notes

```bash
awk -F ',' '$1=="Nigeria"' energy_sample.csv > nigeria.csv
# -f = filter
# -F = filter
# $ = searches a column, $[number] = check specified column for value
# $1 = column or row 1
# NR==1 = Header
# grep = global regex print 
# || = OR, & = AND
# filter by ',', search only for Nigeria in column 1 in energy_sample.csv, copy data to new .csv 
cut -d ',' -f3 output.csv |sort|uniq -c| sort -nr
# -d = delimiter
# -f3 column 3
# sort = sort 
# uniq -c = remove duplicates
# sort -n = sort by number
awk -F',' 'NR==1' '$1=="Kenya"' energy_sample.csv > kenya.csv  
```
