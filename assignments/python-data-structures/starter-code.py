# Python Data Structures Starter Code
# Work with lists, dictionaries, sets, and tuples

from typing import List, Dict, Set, Tuple, Any


# TODO: List and Tuple Functions

def find_min_max(numbers: List[int]) -> Tuple[int, int]:
    """
    Find the minimum and maximum values in a list.
    
    Args:
        numbers: List of integers
    
    Returns:
        Tuple of (min_value, max_value)
    """
    # TODO: Implement min/max finding
    pass


def remove_duplicates_ordered(items: List[Any]) -> List[Any]:
    """
    Remove duplicates from a list while preserving order.
    
    Args:
        items: List that may contain duplicates
    
    Returns:
        List with duplicates removed, original order preserved
    """
    # TODO: Implement duplicate removal with order preservation
    pass


def flatten_list(nested_list: List[Any]) -> List[Any]:
    """
    Flatten a nested list into a single-level list.
    
    Args:
        nested_list: List containing nested lists
    
    Returns:
        Single-level flattened list
    """
    # TODO: Implement list flattening
    pass


def merge_sorted_lists(list1: List[int], list2: List[int]) -> List[int]:
    """
    Merge two sorted lists into one sorted list.
    
    Args:
        list1: First sorted list
        list2: Second sorted list
    
    Returns:
        Merged sorted list
    """
    # TODO: Implement sorted list merging
    pass


def demonstrate_tuple_immutability() -> None:
    """
    Demonstrate the immutability of tuples and when to use them.
    """
    # TODO: Create examples showing tuple immutability
    # and compare with list mutability
    pass


# TODO: Dictionary Functions

def count_frequencies(items: List[Any]) -> Dict[Any, int]:
    """
    Count the frequency of each item in a list.
    
    Args:
        items: List of items
    
    Returns:
        Dictionary with items as keys and frequencies as values
    """
    # TODO: Implement frequency counting
    pass


def merge_dictionaries(dict1: Dict, dict2: Dict) -> Dict:
    """
    Merge two dictionaries, handling key conflicts.
    
    Args:
        dict1: First dictionary
        dict2: Second dictionary
    
    Returns:
        Merged dictionary
    """
    # TODO: Implement dictionary merging
    pass


def invert_dictionary(original_dict: Dict) -> Dict:
    """
    Invert a dictionary (swap keys and values).
    
    Args:
        original_dict: Dictionary to invert
    
    Returns:
        Dictionary with keys and values swapped
    """
    # TODO: Implement dictionary inversion
    pass


def find_keys_with_value(dictionary: Dict, target_value: Any) -> List[Any]:
    """
    Find all keys that have a specific value.
    
    Args:
        dictionary: Dictionary to search
        target_value: Value to find
    
    Returns:
        List of keys with the target value
    """
    # TODO: Implement value-based key finding
    pass


def access_nested_value(nested_dict: Dict, keys: List[str]) -> Any:
    """
    Access deeply nested dictionary values.
    
    Args:
        nested_dict: Dictionary that may have nested structure
        keys: List of keys representing the path
    
    Returns:
        Value at the nested location
    """
    # TODO: Implement nested dictionary access
    pass


# TODO: Set Functions

def find_common_elements(lists: List[List[Any]]) -> Set[Any]:
    """
    Find common elements across multiple lists using sets.
    
    Args:
        lists: List of lists to compare
    
    Returns:
        Set of common elements
    """
    # TODO: Implement common element finding with sets
    pass


def find_set_difference(set1: Set, set2: Set) -> Set:
    """
    Find elements in set1 that are not in set2.
    
    Args:
        set1: First set
        set2: Second set
    
    Returns:
        Set difference
    """
    # TODO: Implement set difference
    pass


def check_subset(list1: List[Any], list2: List[Any]) -> bool:
    """
    Check if all elements in list1 are in list2.
    
    Args:
        list1: Potential subset
        list2: Potential superset
    
    Returns:
        True if list1 is a subset of list2
    """
    # TODO: Implement subset checking
    pass


# TODO: Data Structure Selection

def recommend_data_structure(scenario: str) -> str:
    """
    Recommend which data structure to use for a given scenario.
    
    Args:
        scenario: Description of the task
    
    Returns:
        Recommended data structure with explanation
    """
    # TODO: Implement data structure recommendations
    # Consider: lists, dictionaries, sets, tuples, collections
    pass


if __name__ == "__main__":
    # Example usage (uncomment and modify as you implement functions)
    # numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    # print(find_min_max(numbers))
    # print(remove_duplicates_ordered(numbers))
    pass
