## Files I/O 

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

Add `b` for binary mode → `'rb'`, `'wb'`, etc.

## Recommended Way – Always Use `with`

```python
with open("notes.txt", "a") as file:
    file.write("New line added!\n")
# file is automatically closed – even if error occurs
