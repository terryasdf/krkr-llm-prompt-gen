# KrKr LLM Prompt Generator

This is a personal project for automating the process of creating fine-tuning dataset from character conversations in KrKr-based visual novels.

## How To Use
tba

## Features

- **Conversation dialogue extraction**: Extracts all conversation by all characters while excluding lines indicating characters' thoughts.
- **Text pre-processing**: Removes all irrelevant symbols and ensures all alphabets and numbers are half-width.
- **Multi-language support**: Collects texts in all languages available in-game.

## Data Format

The conversations of all scn files are saved into **one single CSV file**. The format of each row is as follows:
- The row below stores a line said by `[CHARACTER]` in multiple languages during a conversation.
```
[CHARACTER], [LANGUAGE_0], [LANGUAGE_1], ...
```
- The row below indicates ending of a conversation.
```
<END>, ...
```
