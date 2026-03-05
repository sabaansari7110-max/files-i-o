 Files I/O 

# Python File I/O – Read, Write, Append & with Statement

A beginner-friendly repository to learn **file handling in Python** — one of the most important skills for real-world Python programming.

Topics covered:
- Opening and closing files
- Reading files (`read()`, `readline()`, `readlines()`)
- Writing to files (`write()`, `writelines()`)
- Appending to files (mode `'a'`)
- Different file modes (`'r'`, `'w'`, `'a'`, `'r+'`, `'w+'`, `'a+'`)
- The **recommended** `with` statement (context manager – auto-closes files!)
- Basic error handling with `try-except`
- Common real-world patterns

## Why Learn File I/O?

Almost every useful program needs to:
- Read configuration / data files
- Save results / logs
- Append daily reports / chat history
- Work with CSV, JSON, logs, etc.

## File Modes Quick Reference

| Mode   | Description                              | Creates file? | Overwrites? | Starts at     |
|--------|------------------------------------------|---------------|-------------|---------------|
| `'r'`  | Read only (default)                      | No            | —           | beginning     |
| `'w'`  | Write (truncates file to 0 length)       | Yes           | Yes         | beginning     |
| `'a'`  | Append (writes at end)                   | Yes           | No          | end           |
| `'r+'` | Read + Write                             | No            | No          | beginning     |
| `'w+'` | Read + Write (truncates)                 | Yes           | Yes         | beginning     |
| `'a+'` | Read + Append                            | Yes           | No          | end           |

Add `b` for binary mode → `'rb'`, 
`'wb'`, etc.

## Recommended Way – Always Use `with`

```python
with open("notes.txt", "a") as file:
    file.write("New line added!\n")
# file is automatically closed – even if error occurs
```
# Practice Codes Included
All examples are in the examples/ folder (or directly below):
1. Basic Read + Write + Append (file_basics.py)
## 1. Writing (creates/overwrites)
```python
with open("story.txt", "w") as f:
    f.write("Once upon a time...\n")
    f.write("Python was learning file I/O.\n")
```
## 2. Appending
```python
python
with open("story.txt", "a") as f:
    f.write("And it lived happily ever after.\n")
```

## 3. Reading whole file
```python
with open("story.txt", "r") as f:
    content = f.read()
    print("Complete story:\n", content)
```
## 4. Reading line by line (most memory efficient)
```python
print("\nLine by line:")
with open("story.txt", "r") as f:
    for line in f:
        print(line.strip())
```
