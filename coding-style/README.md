# How to add an **Epidle coding style error** ✨

A coding style error must be created under its category folder (for the database to be well structured).

If you need to create a category, you are free to choose the folder name, as it is not used by the DataLoader.
However, you MUST add a `DESC.md` file inside that folder containing the real name of the category (which will be displayed on the website).

Start by creating a folder for the coding style error under its respective category folder. The folder name does not matter and only serves to make the database more readable, so feel free to use a meaningful name.

Inside that folder, you MUST have an `object.json` file containing:
- `name`: the name of the error
- `description`: the official description of the error
- `type`: the type error of the coding style (INFO, MINOR, MAJOR)

And there you go, you just created an **Epidle coding style error**, it's that easy! 😎

# **Epidle coding style's code** ✨

## What's an **Epidle coding style's code**?

The third challenge of Epidle is to identify which coding style is present in a given code.
The code must be only have a single coding style, and consist of only one function/method.

Note that:
- A coding style can have multiple codes representing it
- A coding style can also have no code at all

## How to add an **Epidle coding style's code**

**Epidle coding style's codes** are stored in the `examples` folder of their respective error folder.
If no `examples` folder exists, create one.

Inside that folder, you can create a `.c` or `.cpp` file.
Each file represents one **Epidle coding style's code** that can appear during the third challenge.
