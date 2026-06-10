# Course Recommendation System
**Codsoft Internship Task - Artificial Intelligence**


---

## What is this project?

This is a beginner level AI Course Recommendation System built using Python.
The program shows users a list of beginner friendly online courses from 4 different tech fields.
It uses Content Based Filtering to rank and sort courses based on ratings, and the ranking actually updates in real time when users give their own ratings during the session.

---

## How to Run

Make sure Python 3 is installed. No extra libraries needed.

```
python course_recommendation.py
```

---

## Program Flow

```
START
  |
  v
Show Welcome Screen
  |
  v
Show 4 Categories
  1. Artificial Intelligence
  2. Web Development
  3. Data Science
  4. Cybersecurity
  |
  v
User Selects a Category (1 to 4)
  |
  v
Content Based Filter Runs
  - calculate_final_score() runs for each course
  - sort_courses_by_score() sorts them highest first
  |
  v
Sorted Courses are Displayed
  |
  v
User Selects a Course
  |
  v
User Gives a Rating (1 to 5)
  |
  v
Rating is Stored
  - saved inside the course (updates future score)
  - saved in all_ratings list (for session summary)
  |
  v
AI Suggests a Related Category (based on rating given)
  |
  v
Thank You Message is Shown
  |
  v
Ask: Explore Another Category?
  |-- yes --> go back to Show Categories
  |-- no  --> Show Session Summary --> EXIT
  
END
```

---

## How the Data is Stored

Each course is stored as a plain list with 5 values inside it:

```
[ Name, Platform, Level, Base Rating, User Ratings List ]
  [0]    [1]       [2]    [3]          [4]
```

Example:
```
["AI For Everyone by Andrew Ng", "Coursera", "Beginner", 4.8, []]
```

To make it easy to access each value, index constants are defined at the top:

```
NAME         = 0
PLATFORM     = 1
LEVEL        = 2
BASE_RATING  = 3
USER_RATINGS = 4
```

So instead of remembering position numbers, the code uses `course[NAME]`, `course[BASE_RATING]` etc.

---

## Content Based Filtering - How it Actually Works

### What is Content Based Filtering?

Content Based Filtering is a recommendation technique where the system recommends items based on the features (content) of those items. In this project, the feature used is the **score** of each course. Courses with higher scores are shown first.

The important thing is that this score is **not fixed**. It changes every time a user gives a rating. So the filtering is actually learning from user input and updating recommendations in real time.

---

### The Two Part Score System

Each course has two separate rating fields:

**base_rating** - This is the original rating the course has on the internet (like on Coursera or Udemy). This number never changes. It is set when the program starts.

**user_ratings** - This is an empty list at the start. Every time a user rates a course, that number gets added to this list. Over time, this list fills up with real user feedback.

---

### How the Final Score is Calculated

The `calculate_final_score()` function handles this:

**Step 1** - If no user has rated the course yet, just return the base rating as is.

**Step 2** - If users have rated it, calculate the average of all user ratings by adding them up and dividing by the count.

**Step 3** - Mix the base rating and the user average together using this formula:

```
Final Score = (Base Rating x 0.6) + (User Average x 0.4)
```

This means base rating carries 60% of the weight and user ratings carry 40%.

The reason for keeping base rating heavier is so that one single bad rating does not completely destroy a course that is genuinely good. But user ratings still have real influence - if many users rate it low, the score will drop noticeably.

---

### Example of Score Changing

Say a course starts with a base rating of 4.5 and no one has rated it yet.

**Before any ratings:**
```
user_ratings = []
Final Score = 4.5
```

**After one user rates it 2 out of 5:**
```
user_ratings = [2]
user average = 2.0
Final Score = (4.5 x 0.6) + (2.0 x 0.4)
            = 2.70 + 0.80
            = 3.5
```
The course drops from 4.5 to 3.5 and moves down in the sorted list.

**After a second user rates it 5 out of 5:**
```
user_ratings = [2, 5]
user average = (2 + 5) / 2 = 3.5
Final Score = (4.5 x 0.6) + (3.5 x 0.4)
            = 2.70 + 1.40
            = 4.1
```
The course recovers to 4.1 because of the positive rating.

This is content based filtering working in real time. The ranking changes based on actual user input during the session.

---

### How Sorting Works

The `sort_courses_by_score()` function uses **Bubble Sort** to arrange courses from highest score to lowest.

Bubble Sort works by going through the list repeatedly and comparing two courses side by side. If the left one has a lower score than the right one, they get swapped. This keeps repeating until everything is in the right order.

Two separate lists are kept in sync during sorting - one for courses and one for their scores - so the displayed score always matches the right course.

The filter reruns every time a category is shown. So if a user comes back to the same category after giving a rating, the order of courses may be different because the scores have been updated.

---

## AI Suggestion Feature

After the user rates a course, the `ai_suggest_next()` function suggests a related category to explore next.

Related category pairs used in this project:

```
Artificial Intelligence  -->  Data Science
Web Development          -->  Cybersecurity
Data Science             -->  Artificial Intelligence
Cybersecurity            -->  Web Development
```

The message shown also changes based on what rating the user gave:

```
Rating 4 or 5  -->  "You liked it! Try this related field too."
Rating 3       -->  "Average rating. Maybe try a different angle."
Rating 1 or 2  -->  "Maybe this other field is a better fit for you."
```

---

## All Functions Explained

| Function | What it does |
|---|---|
| show_welcome() | Prints the welcome banner at the start |
| show_categories() | Prints the 4 category options |
| get_user_category() | Takes category input from user and validates it |
| get_category_name() | Returns category name from category number |
| get_course_list() | Returns the correct course list for the category |
| calculate_final_score() | Calculates mixed score from base rating and user ratings |
| sort_courses_by_score() | Sorts course list by score using bubble sort |
| show_courses() | Displays sorted courses with all details |
| get_user_course() | Takes course selection from user and validates it |
| get_user_rating() | Takes rating input (1 to 5) from user and validates it |
| store_rating() | Saves rating inside the course and in session summary list |
| ai_suggest_next() | Suggests a related category based on rating given |
| show_all_ratings() | Prints all ratings given in the current session |
| show_thankyou() | Prints the closing thank you message |
| main() | Runs the full program loop from start to finish |

---

## Input Validation

Every input in the program is validated before being used. The program uses `.isdigit()` to check if the user typed a number or not. If they type letters or leave it blank, the program prints an error and asks again using a `while True` loop.

This is done for:
- Category selection (must be 1 to 4)
- Course selection (must be within the displayed range)
- Rating input (must be 1 to 5)

---

## Sample Output

```
==================================================
  WELCOME TO COURSE RECOMMENDATION SYSTEM
==================================================

------ COURSE CATEGORIES ------
1. Artificial Intelligence
2. Web Development
3. Data Science
4. Cybersecurity
--------------------------------

Enter category number (1-4): 1

--- COURSES FOR: Artificial Intelligence ---
(sorted by score - best rated courses come first)

1. AI For Everyone by Andrew Ng
   Platform    : Coursera
   Level       : Beginner
   Base Rating : 4.8 / 5.0
   Final Score : 4.8 / 5.0

2. Machine Learning Crash Course
   Platform    : Google
   Level       : Beginner
   Base Rating : 4.7 / 5.0
   Final Score : 4.7 / 5.0

...

Enter course number (1-5): 1

You selected : AI For Everyone by Andrew Ng
Your Rating (1-5): 2

Your rating has been saved!
It will affect how courses are ranked if you come back to this category.

--- AI SUGGESTION ---
You gave an average rating for Artificial Intelligence
How about trying: Data Science instead?
Sometimes a different starting point helps a lot!
```

---

## Concepts Used in This Project

- Lists and nested lists to store course data
- Index constants (NAME, PLATFORM etc.) to access list values cleanly
- Functions to break the program into small reusable parts
- While loops for input validation and session looping
- For loops for calculating averages and bubble sort
- Bubble sort algorithm to sort courses by score
- Content Based Filtering using a mixed score formula
- AI suggestion logic based on category and user rating

---

## Possible Future Improvements

- Save ratings to a text file so they stay even after the program closes
- Add more categories like Cloud Computing or Mobile App Development
- Let users search for a course by typing a keyword
- Show a learning path like beginner to advanced
- Add Collaborative Filtering which recommends based on what other similar users liked

---


## Author

Made by Kalal Sohana

LinkedIn: [https://lnkd.in/gzafaPJ8]

GitHub: [https://github.com/sohanamahendar-ux/CODSOFT/tree/main/Task_Course_Recommendation]

*Built as part of the Codsoft AI Internship Program.*