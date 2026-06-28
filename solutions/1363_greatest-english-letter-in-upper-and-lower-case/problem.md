# 2309. Greatest English Letter in Upper and Lower Case

**Difficulty:** 🟢 Easy  
**Tags:** Hash Table, String, Enumeration  
**LeetCode:** https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

---

1363 - Greatest English Letter in Upper and Lower CaseDifficulty: Easy - greatest-english-letter-in-upper-and-lower-caseGiven a string of English letters `s`, return *the **greatest **English letter which occurs as **both** a lowercase and uppercase letter in* `s`. The returned letter should be in **uppercase**. If no such letter exists, return *an empty string*.

An English letter `b` is **greater** than another letter `a` if `b` appears **after** `a` in the English alphabet.

 

**Example 1:**

```
**Input:** s = "l**Ee**TcOd**E**"
**Output:** "E"
**Explanation:**
The letter 'E' is the only letter to appear in both lower and upper case.
```

**Example 2:**

```
**Input:** s = "a**rR**AzFif"
**Output:** "R"
**Explanation:**
The letter 'R' is the greatest letter to appear in both lower and upper case.
Note that 'A' and 'F' also appear in both lower and upper case, but 'R' is greater than 'F' or 'A'.
```

**Example 3:**

```
**Input:** s = "AbCdEfGhIjK"
**Output:** ""
**Explanation:**
There is no letter that appears in both lower and upper case.
```

 

**Constraints:**

	- `1 <= s.length <= 1000`

	- `s` consists of lowercase and uppercase English letters.