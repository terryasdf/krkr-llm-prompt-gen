from pandas import DataFrame
from typing import Any
from collections.abc import Callable

def default_user_wrapper(text: str):
    return { 'role': 'user', 'content': text }

def default_assistant_wrapper(text: str):
    return { 'role': 'assistant', 'content': text }

def generate_prompt_messages(data: DataFrame,
                             characters: list[str],
                             language: str,
                             is_multi_turn: bool = True,
                             user_wrapper: Callable[[str], Any] = default_user_wrapper,
                             assistant_wrapper: Callable[[str], Any] =default_assistant_wrapper):
    """
    Generates a list of one-turn or multi-turn chat examples, where `character` is the
    assistant.

    `language` is one of the keys of `data`.

    `user_mapper` and `assistant_mapper` are custom wrappers that wraps the text into
    format expected by LLM APIs.

    The default wrappers can be applied to llama models.
    """

    selected = []
    msg = []
    if data.shape[0] < 2:
        return selected

    for i in range(1, data.shape[0] - 1):
        assert data['CHARACTER'][i-1] != data['CHARACTER'][i]
        if data['CHARACTER'][i] in characters:
            if data['CHARACTER'][i-1] == '<END>':
                continue
            msg.append(user_wrapper(data[language][i-1]))
            msg.append(assistant_wrapper(data[language][i]))
            if not is_multi_turn:
                selected.append(msg)
                msg = []
        elif data['CHARACTER'][i-1] not in characters:
            if not msg:
                continue
            selected.append(msg)
            msg = []
    return selected
