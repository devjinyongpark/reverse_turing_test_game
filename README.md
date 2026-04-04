# Reverse Turing Test Game

A small terminal game where **one human player** and several **AI players** answer questions and vote on who they think is human.

You are the human player.

The goal is simple:

- answer naturally
- avoid being detected as the human
- survive until the end

---

## What is this project?

This project runs in the **Terminal** (Mac) or **Command Prompt / PowerShell** (Windows).

When you start the game:

1. you enter your own name
2. you enter names for the AI players
3. the host gives everyone a random question
4. all players answer
5. all players explain who seems human
6. everyone votes
7. one player may be eliminated
8. the game continues until the result is decided

In short, it is like a social deduction game, but the hidden player is the **human**, not the AI.

---

## Before you start

You need these things before running the game:

- a computer with **Python 3.11 or newer**
- an internet connection
- an **OpenAI API key**
- the project files downloaded to your computer

---

## Important note about the OpenAI API key

This project uses the OpenAI API, so you need your **own API key**.

Please note:

- **ChatGPT Plus or Pro is not the same thing as API access**
- API usage may cost money depending on how much you use
- keep your API key private
- **never upload your API key to GitHub**

You will store your API key in a local file called `.env`.

---

## Step 1. Download the project from GitHub

If you have never used GitHub before, do this:

1. Open this repository page.
2. Click the green **Code** button.
3. Click **Download ZIP**.
4. Find the downloaded ZIP file on your computer.
5. Unzip it.
6. Open the unzipped folder.

You do **not** need to know Git or use git commands for this project.

---

## Step 2. Install Python

1. Go to the official Python website.
2. Download **Python 3.11 or newer**.
3. Install it.

### On Windows
During installation, make sure to check:

- **Add Python to PATH**

This is very important.

### On Mac
Install Python normally.  
After that, you can check whether it worked by opening Terminal and typing:

```bash
python3 --version
````

---

## Step 3. Open Terminal or Command Prompt

### On Mac

Open:

* **Terminal**

### On Windows

Open one of these:

* **Command Prompt**
* **PowerShell**

---

## Step 4. Move into the project folder

You need to tell the terminal where your project folder is.

Use the `cd` command.

Example:

```bash
cd path/to/reverse_turing_test_game
```

### Example on Mac

```bash
cd ~/Downloads/reverse_turing_test_game
```

### Example on Windows

```bash
cd C:\Users\YourName\Downloads\reverse_turing_test_game
```

After this, your terminal should be “inside” the project folder.

---

## Step 5. Install the required libraries

This project needs a few Python packages before it can run.

In the terminal, type:

```bash
pip install -r requirements.txt
```

If that does not work, try:

```bash
pip3 install -r requirements.txt
```

This installs the libraries listed in `requirements.txt`.

---

## Step 6. Create a `.env` file

Inside the project folder, create a new file named:

```text
.env
```

Open that file and write:

```text
OPENAI_API_KEY=sk-...
```

Replace `sk-...` with your real OpenAI API key.

### Very important

* do not add extra spaces
* do not upload this file to GitHub
* do not share your key with anyone

### Correct example

```text
OPENAI_API_KEY=sk-1234567890example
```

---

## Step 7. Run the game

In the terminal, type:

```bash
python main.py
```

If that does not work, try:

```bash
python3 main.py
```

---

## How to play

After the game starts:

1. Enter **your own name**
2. Enter names for the AI players
3. Read the host’s question
4. Type your answer
5. Read everyone’s responses
6. During voting, decide who you think is human
7. Type the exact player name you want to vote for

The game keeps going round by round.

### You lose if:

* the other players correctly identify and eliminate you

### You win if:

* you survive until only two players remain

---

## Example of what you may see

```text
Enter Your Name: Jin
Enter Name for AI: Alex
Enter Name for AI: Mina
Enter Name for AI: Leo
Host: What is your favorite childhood memory?

Response:
```

At that point, you type your own answer and press Enter.

---

## Files in this project

Here is a simple explanation of the main files:

* `main.py`
  Starts and runs the game

* `Players.py`
  Contains the human player and AI player logic

* `questions.txt`
  Stores the questions used in the game

* `requirements.txt`
  Lists the Python packages you need to install

* `sounds.py`
  Plays sound effects

* `sounds/`
  Contains the sound files

You usually only need to run:

```bash
python main.py
```

---

## Common problems and fixes

### 1. `python` does not work

Try:

```bash
python3 main.py
```

If that still does not work, Python may not be installed correctly.

---

### 2. `pip` does not work

Try:

```bash
pip3 install -r requirements.txt
```

---

### 3. `No module named ...`

This usually means the required packages were not installed.

Run:

```bash
pip install -r requirements.txt
```

or

```bash
pip3 install -r requirements.txt
```

---

### 4. API key error

Check these carefully:

* is the file name exactly `.env`?
* did you write `OPENAI_API_KEY=...` correctly?
* is your API key valid?
* did you accidentally include extra spaces?

---

### 5. No sound plays

This project includes sound effects, but sound playback may behave differently depending on your operating system and environment.

If the game runs but you do not hear sound, the main game may still work.

---

### 6. Nothing happens after downloading from GitHub

Make sure you:

1. unzipped the downloaded ZIP file
2. opened Terminal / Command Prompt
3. moved into the correct folder with `cd`
4. installed the requirements
5. created the `.env` file
6. ran `python main.py`

---

## For complete beginners

If this is your first time using GitHub or Python, here is the shortest version:

1. Download ZIP from GitHub
2. Unzip it
3. Install Python
4. Open Terminal / Command Prompt
5. Go into the project folder with `cd`
6. Run `pip install -r requirements.txt`
7. Create `.env`
8. Put your OpenAI API key inside `.env`
9. Run `python main.py`

---

## Safety reminder

Your API key is private.

Do **not**:

* post it in screenshots
* upload it to GitHub
* send it to other people
* leave it inside public files

---

## AI Disclosure

No AI tools were used in writing the code for this project.

However, this README was written with the help of ChatGPT in order to make the instructions as clear, detailed, and beginner-friendly as possible.
