import tiktoken

# Credit: This function is based on code by Rok Benko
# Source: https://stackoverflow.com/questions/75804599/openai-api-how-do-i-count-tokens-before-i-send-an-api-request

def num_tokens_from_string(string: str, encoding_name: str) -> int:

    """
    Calculate the number of tokens in a string for a given encoding.

    Parameters:
    string (str): The string for which to count tokens.
    encoding_name (str): The name of the encoding to use (e.g., "gpt-3.5-turbo").

    Returns:
    int: The number of tokens in the string according to the specified encoding.

    Credit:
    This function is based on a Stack Overflow answer.
    Source: https://stackoverflow.com/questions/75804599/openai-api-how-do-i-count-tokens-before-i-send-an-api-request

    """

    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens