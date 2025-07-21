# 🎮 Guess the Number - Python GUI Game

A fun and simple number guessing game built with `tkinter` and enhanced using `customtkinter`. The player tries to guess a randomly selected number between **1 and 20**. The game gives feedback on whether the guess is too high, too low, or correct, and keeps track of score and highscore.

![Game Screenshot Placeholder]

---

## 🧠 Game Idea

The game selects a random number between 1 and 20 at the start. You must guess this number:

- If your guess is **correct**, the background turns green, and you win the round.
- If your guess is **too high or too low**, your score decreases by 1.
- If your score reaches 0, you **lose** and the background turns red.
- You can press **"Again!"** to restart the game at any time.
- Your **highscore** is saved during the session.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **tkinter** (standard Python GUI toolkit)
- **customtkinter** (for modern-looking UI components)

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/guess-number-tkinter.git
cd guess-number-tkinter
```

### 2. Install Dependencies
Make sure you have `customtkinter` installed:

```bash
pip install customtkinter
```

---

## 🚀 Run the Game

```bash
python guess_game.py
```

> Replace `guess_game.py` with the filename if you've saved it differently.

---

## 🖼️ GUI Overview

- **Main Title**: "Guess My Number!"
- **Input Field**: Enter your guess (between 1 and 20)
- **Check Button**: Submit your guess
- **Score and Highscore**: Score decreases with each wrong guess
- **Feedback Label**: Shows messages like "Too High", "Too Low", or "Correct"
- **Again! Button**: Restarts the game with a new number

---

## 📂 Project Structure

```
guess-number-tkinter/
│
├── guess_game.py         # Main game file
├── README.md             # Game documentation
```

---

## 💡 Features

- Clean and modern GUI with `customtkinter`
- Real-time feedback on guesses
- Score tracking with a highscore system
- Responsive and well-placed GUI elements
- Fully restartable game with "Again!" button

---

## 📸 Screenshots

> You can add your own screenshot here by replacing this section.

---

## 🤝 Contribution

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📃 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🧑‍💻 Author

- [Your Name or GitHub Username](https://github.com/yourusername)

---

## 📌 Notes

- You can modify the range (e.g., 1–50) by editing the line:
  ```python
  self.hds = random.randint(1, 20)
  ```
- Want to add sound, animations, or timer? That could be your next challenge!

Enjoy the game! 🎉