# How to add an **Epidle pool day** ✨

There are currently two pools in the database: POOL-1 and POOL-3.

A pool day must be created under its pool folder.

If you need to add a new pool, you are free to choose the folder name, as it is not used by the DataLoader.

Start by creating a folder for the pool day under its respective pool folder. The folder name does not matter and only serves to make the database more readable, so feel free to use a meaningful name.

Inside that folder, you MUST have an `object.json` file containing:
- `name`: the name of the pool day (found in the subject)
- `number`: the day number (e.g., 1, 2, 3...)
- `language`: the programming language of the pool day (Shell, C, C++, Haskell, Rust, etc.)

And there you go, you just created an **Epidle pool day**, it's that easy! 😎

# **Epidle pool day's functions** ✨

## What's an **Epidle pool day's function**?

The second challenge of Epidle is to identify which day a function belongs to (e.g., my_strstr → Day 6).

A pool day must have at least one function associated with it.

## How to add an **Epidle pool day's function**

**Epidle pool day's functions** are stored in a `functions.json` file inside their respective pool day's folder.

The `functions.json` file is a JSON array containing all the functions for that pool day.

Example entry:
```json
{
    "name": "my_strdup",
    "prototype": "char *my_strdup(char const *src);",
    "description": "Write a function that allocates memory and copies the string given as argument in it.",
    "task_number": 1
}
```

Each JSON object in the array must contain:
- `name`: the function name (e.g., `my_strdup`)
- `prototype`: the function prototype as specified in the pool day subject (e.g., `char *my_strdup(char const *src);`)
- `description`: the function description as specified in the pool day subject
- `task_number`: the corresponding task number in the pool day (e.g., 1)
