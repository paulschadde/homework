# Week 3 – Analysis Plan (Disney+ dataset)

## 1. Questions (Project Director)
1. Are Disney+ titles released more recently rated higher or lower than older ones?
2. Which genres have the highest average rating, and does this change across decades?
3. Do titles with more genres get better or worse ratings?
4. Which genres have the highest average rating, and does that change over decades?

## 2. Refined Question (Project Manager)

**Chosen question:** Which genres have the highest average rating, and does this change across decades?

**Definitions and decisions:**
- **Rating measure:** I will use `imdb_rating` (0–10). `metascore` is missing for many titles, which would leave too few observations per genre.
- **Minimum votes:** I will only keep titles with at least 1,000 IMDb votes, so that ratings based on very few votes do not distort the averages.
- **Titles with multiple genres:** A title is counted once in each genre it lists
  (e.g. "Animation, Comedy" counts for both). This uses all available information, but genres are therefore not independent groups.
- **Time variable:** I will use the original release year (`year`), not the date the title was added to Disney+ (`added_at`), since almost all titles were added after 2019. From `year` I will create a `decade` variable (e.g. 1990s).
- **Content type:** I will include only movies (`type == "movie"`), because movies and series are rated differently and mixing them could distort genre averages.
- **Minimum group size:** I will only report genres (and genre–decade combinations) with at least 10 titles, since averages from very small groups are unreliable.
- **Scope:** I will first answer part 1 (overall genre ranking) and then part 2
  (change across decades) if time and data allow.

**Variables needed:** `title`, `type`, `genre`, `year`, `imdb_rating`, `imdb_votes`

## 3. Data Cleaning Steps (Data Analyst)

1. **Remove empty rows:** The dataset has 992 rows, but only 894 have an `imdb_id` and `title`.I will drop rows where `imdb_id` is missing, since they contain no information besides `added_at`.
2. **Filter to movies:** I will keep only rows where `type` is "movie" (to be verified with `unique()`).
3. **Clean `year`:** `year` is stored as text, not as a number. I will extract the first four digits (to handle entries such as "2019–") and convert them to an integer.
4. **Create `decade`:** From `year`, I will create `decade` as `year // 10 * 10` (e.g. 1994 → 1990).
5. **Clean `imdb_votes`:** `imdb_votes` is stored as text. I will remove thousands separators (",") and convert it to a number.
6. **Handle missing values:** I will drop titles with a missing `genre` or `imdb_rating`,since they cannot contribute to the answer. Imputing a rating would distort the averages.
7. **Apply vote threshold:** I will keep only titles with `imdb_votes >= 1000`.
8. **Split `genre`:** `genre` contains several values in one cell (e.g. "Animation, Comedy"). I will split it by comma, strip whitespace, and give each title–genre combination its own row (one row per title and genre). This is the "multiple values in one column" problem from Wickham's Tidy Data.
9. **Aggregate:** I will compute the mean `imdb_rating` and the number of titles per genre(part 1) and per genre and decade (part 2), keeping only groups with at least 10 titles.

## 4. Feasibility and Open Issues
- After filtering (movies only, ≥1,000 votes, no missing values), the sample may become small.I will check how many titles remain before deciding on the 10-title minimum.
- Older decades likely contain few titles, so part 2 may only be meaningful for recent decades.
- Counting a title in several genres means genre averages are not independent; this should be
  mentioned when interpreting the results.
- The dataset only covers titles available on Disney+, so the results describe Disney's catalogue, not films in general.