# How to add an **Epidle project** ✨

A project must be created under its module folder (for the database to be well structured).

If you need to create a module, you are free to choose the folder name, as it is not used by the DataLoader.
However, you MUST add a `DESC.md` file inside that folder containing the real name of the module (which will be displayed on the website).

Start by creating a folder for the project under that module folder. The folder name does not matter and only serves to make the database more readable, so feel free to use a meaningful name.

Inside that folder, you MUST have an `object.json` file containing:
- `name`: the name of the project
- `emoji`: emoji(s) describing the project (used in Epidle's first challenge 'Guess the project by the emoji')
- `semester`: the semester when the project takes place (given as a hint in the first challenge after a few wrong answers)

And there you go, you just created an **Epidle project**, it's that easy! 😎

# **Epidle project's code** ✨

## What's an **Epidle project's code**?

The fourth challenge of Epidle is to guess which project a given code belongs to.
The code must be explicit enough for the player to identify the project clearly, and consist of only one function/method.

Note that:
- A project can have multiple codes representing it
- A project can also have no code at all

## How to add an **Epidle project's code**

**Epidle project's codes** are stored in the `examples` folder of their respective project folder.
If no `examples` folder exists, create one.

Inside that folder, create `.c` or `.cpp` files.
Each file represents one **Epidle project's code** that can appear during the fourth challenge.
