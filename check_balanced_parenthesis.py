"""
Check Balanced Parenthesis Algorithm
Validates whether parentheses/brackets/braces are properly balanced in a string
Time Complexity: O(n)
Space Complexity: O(n) for stack
"""

def is_balanced_parenthesis(string):
    """
    Check if parentheses are balanced in a string.
    
    Args:
        string (str): String containing text and parentheses
    
    Returns:
        bool: True if balanced, False otherwise
    """
    stack = []
    matching_pairs = {')': '(', '}': '{', ']': '['}
    
    for char in string:
        if char in matching_pairs.values():  # Opening bracket
            stack.append(char)
        elif char in matching_pairs:  # Closing bracket
            if not stack or stack[-1] != matching_pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0


def is_balanced_parenthesis_detailed(string):
    """
    Check balanced parenthesis with detailed information.
    
    Args:
        string (str): String to validate
    
    Returns:
        dict: Contains result, error_info, and position details
    """
    stack = []
    matching_pairs = {')': '(', '}': '{', ']': '['}
    opening = set(['(', '{', '['])
    
    for i, char in enumerate(string):
        if char in opening:
            stack.append((char, i))
        elif char in matching_pairs:
            if not stack:
                return {
                    "balanced": False,
                    "error": f"Closing bracket '{char}' without opening at position {i}",
                    "position": i
                }
            top_bracket, top_pos = stack[-1]
            if top_bracket != matching_pairs[char]:
                return {
                    "balanced": False,
                    "error": f"Mismatched bracket: '{top_bracket}' at {top_pos} doesn't match '{char}' at {i}",
                    "position": i
                }
            stack.pop()
    
    if stack:
        unclosed_bracket, position = stack[0]
        return {
            "balanced": False,
            "error": f"Unclosed bracket '{unclosed_bracket}' at position {position}",
            "position": position
        }
    
    return {
        "balanced": True,
        "error": None,
        "position": None
    }


def balance_parenthesis_count(string):
    """
    Count open and close parenthesis and check balance.
    
    Returns:
        dict: Count of each type and balance status
    """
    opening = {'(': 0, '{': 0, '[': 0}
    closing = {')': 0, '}': 0, ']': 0}
    
    for char in string:
        if char in opening:
            opening[char] += 1
        elif char in closing:
            closing[char] += 1
    
    balanced = (
        opening['('] == closing[')'] and
        opening['{'] == closing['}'] and
        opening['['] == closing[']']
    )
    
    return {
        "opening": opening,
        "closing": closing,
        "balanced": balanced and is_balanced_parenthesis(string)
    }


# Test Cases
if __name__ == "__main__":
    print("=" * 60)
    print("CHECK BALANCED PARENTHESIS ALGORITHM TESTS")
    print("=" * 60)
    
    test_cases = [
        "({[]})",
        "({[}])",
        "()",
        "({[",
        ")}]",
        "{[()]}",
        "Hello (World {and [Universe]})",
        "([)]",
        "",
        "((()))",
    ]
    
    for i, test_string in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: '{test_string}'")
        result = is_balanced_parenthesis(test_string)
        print(f"Balanced: {result}")
        
        detailed = is_balanced_parenthesis_detailed(test_string)
        if detailed["error"]:
            print(f"Error: {detailed['error']}")
        
        print("-" * 60)
