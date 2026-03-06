# Python Text Processing Starter Code
# Work with strings, files, and text manipulation

from collections import Counter
from typing import Dict, List


# TODO: String Manipulation Functions

def count_word_frequency(text: str) -> Dict[str, int]:
    """
    Count the frequency of each word in the text.
    
    Args:
        text: Input text string
    
    Returns:
        Dictionary with words as keys and frequencies as values
    """
    # TODO: Implement word frequency counting
    pass


def reverse_words(sentence: str) -> str:
    """
    Reverse the order of words in a sentence.
    
    Args:
        sentence: Input sentence
    
    Returns:
        Sentence with words in reverse order
    """
    # TODO: Implement word reversal
    pass


def remove_duplicates(text: str) -> str:
    """
    Remove duplicate characters while maintaining order.
    
    Args:
        text: Input text string
    
    Returns:
        Text with duplicate characters removed
    """
    # TODO: Implement duplicate removal
    pass


# TODO: File I/O Functions

def read_file_lines(filepath: str) -> List[str]:
    """
    Read a file and return its lines.
    
    Args:
        filepath: Path to the file to read
    
    Returns:
        List of lines from the file
    """
    # TODO: Implement file reading
    pass


def write_to_file(filepath: str, content: str) -> None:
    """
    Write content to a file.
    
    Args:
        filepath: Path to the output file
        content: Text content to write
    """
    # TODO: Implement file writing
    pass


def count_file_stats(filepath: str) -> Dict[str, int]:
    """
    Count lines, words, and characters in a file.
    
    Args:
        filepath: Path to the file
    
    Returns:
        Dictionary with 'lines', 'words', and 'characters' counts
    """
    # TODO: Implement file statistics
    pass


# TODO: Text Processing Tool

def process_text_file(input_file: str, output_file: str) -> None:
    """
    Read text from input file, process it, and write to output file.
    
    Args:
        input_file: Path to input text file
        output_file: Path to output text file
    """
    # TODO: Implement complete text processing workflow
    # 1. Read the input file
    # 2. Apply text transformations
    # 3. Generate statistics
    # 4. Write processed text and report to output file
    pass


if __name__ == "__main__":
    # Example usage (uncomment and modify as you implement functions)
    # text = "Hello world! Hello python world!"
    # print(count_word_frequency(text))
    # print(reverse_words("The quick brown fox"))
    pass
