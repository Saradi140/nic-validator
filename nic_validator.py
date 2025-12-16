"""
Sri Lankan NIC (National Identity Card) Validator
Automata Theory Make-Up Assignment
Author: [Your Name]
Date: December 2025

This program implements a Deterministic Finite Automaton (DFA) to validate
Sri Lankan NIC numbers in both old and new formats.

NIC Formats:
- Old Format: 9 digits + V/X (e.g., 891234567V)
  * First 2 digits: Last two digits of birth year (00-99)
  * Next 3 digits: Day of year (001-366 for males, 501-866 for females)
  * Last 4 digits: Serial number
  * Last character: V (male) or X (female/special cases)

- New Format: 12 digits (e.g., 199851234567)
  * First 4 digits: Year of birth
  * Next 3 digits: Day of year (001-366 for males, 501-866 for females)
  * Last 5 digits: Serial number
"""

import re
from datetime import datetime
from typing import Tuple, List


class NICValidator:
    """
    DFA-based validator for Sri Lankan NIC numbers
    
    Formal Definition:
    - Σ (Alphabet): {0-9, V, X, v, x}
    - Q (States): {q0, q1, ..., q17, qReject}
    - q₀ (Start State): q0
    - F (Accept States): {q11, q17}
    - δ (Transition Function): Defined in validate() method
    """
    
    def __init__(self):
        self.states = {
            'q0': 'Start',
            'q1': 'Year digit 1',
            'q2': 'Year digit 2',
            'q3': 'Day digit 1',
            'q4': 'Day digit 2',
            'q5': 'Day digit 3',
            'q6': 'Serial digit 1',
            'q7': 'Serial digit 2',
            'q8': 'Old format: serial digit 3',
            'q9': 'Old format: serial digit 4',
            'q10': 'Old format: V/X (ACCEPT)',
            'q12': 'New format: serial digit 1',
            'q13': 'New format: serial digit 2',
            'q14': 'New format: serial digit 3',
            'q15': 'New format: serial digit 4',
            'q16': 'New format: serial digit 5 (ACCEPT)',
            'qReject': 'Reject'
        }
        
        self.accepting_states = {'q10', 'q16'}
    
    def validate(self, nic: str) -> Tuple[bool, List[str], str]:
        """
        Main validation function using DFA
        
        Returns:
            Tuple of (is_accepted, state_trace, final_state)
        """
        nic = nic.strip().upper()
        
        # Initialize DFA
        current_state = 'q0'
        state_trace = [current_state]
        
        # Process each character
        for i, char in enumerate(nic):
            prev_state = current_state
            
            # State q0: Must start with any digit (0-9)
            if current_state == 'q0':
                if char.isdigit():
                    current_state = 'q1'
                else:
                    current_state = 'qReject'
            
            # States q1-q6: Accept any digit (year and day digits)
            elif current_state in ['q1', 'q2', 'q3', 'q4', 'q5', 'q6']:
                if char.isdigit():
                    next_state_num = int(current_state[1]) + 1
                    current_state = f'q{next_state_num}'
                else:
                    current_state = 'qReject'
            
            # State q7: Branch point based on length
            elif current_state == 'q7':
                if len(nic) == 10:  # Old format: next is serial digit 3
                    if char.isdigit():
                        current_state = 'q8'
                    else:
                        current_state = 'qReject'
                elif len(nic) == 12:  # New format: next is serial digit 1
                    if nic[0] not in '12':
                        current_state = 'qReject'
                    elif char.isdigit():
                        current_state = 'q12'
                    else:
                        current_state = 'qReject'
                else:
                    current_state = 'qReject'
            
            # Old format path (q8 → q9 → q10 → q11)
            # Old format path (q8 → q9 → q10)
            elif current_state == 'q8':
                if char.isdigit():
                    current_state = 'q9'
                else:
                    current_state = 'qReject'
            
            elif current_state == 'q9':
                if char.upper() in 'VX':
                    current_state = 'q10'
                else:
                    current_state = 'qReject'
            
            # New format path (q12 → q13 → q14 → q15 → q16)
            elif current_state == 'q12':
                if char.isdigit():
                    current_state = 'q13'
                else:
                    current_state = 'qReject'
            
            elif current_state == 'q13':
                if char.isdigit():
                    current_state = 'q14'
                else:
                    current_state = 'qReject'
            
            elif current_state == 'q14':
                if char.isdigit():
                    current_state = 'q15'
                else:
                    current_state = 'qReject'
            
            elif current_state == 'q15':
                if char.isdigit():
                    current_state = 'q16'
                else:
                    current_state = 'qReject'
            
            # Already in accept or reject state
            elif current_state in ['q11', 'q17']:
                # Should not have more characters after accept state
                current_state = 'qReject'
            
            else:
                current_state = 'qReject'
            
            state_trace.append(current_state)
            
            # Early termination if reached reject state
            if current_state == 'qReject':
                break
        
        # Check if final state is accepting
        is_accepted = current_state in self.accepting_states
        
        return is_accepted, state_trace, current_state
    
    def validate_semantic(self, nic: str) -> Tuple[bool, str]:
        """
        Additional semantic validation (beyond DFA structure)
        Validates year and day values
        """
        nic = nic.strip().upper()
        
        if len(nic) not in [10, 12]:
            return False, "Invalid length"
        
        try:
            if len(nic) == 10:  # Old format
                year = int(nic[:2]) + 1900
                day = int(nic[2:5])
                if not (1 <= day <= 366):
                    return False, f"Invalid day: {day}"
                suffix = nic[-1]
                if suffix == 'V':
                    gender = "Male"
                elif suffix == 'X':
                    gender = "Female"
                else:
                    return False, f"Invalid suffix: {suffix}"
            else:  # New format
                year = int(nic[:4])
                day = int(nic[4:7])
                # Check gender and day range
                if 1 <= day <= 366:
                    gender = "Male"
                elif 501 <= day <= 866:
                    gender = "Female"
                    day -= 500  # Adjust for validation
                else:
                    return False, f"Invalid day: {nic[4:7]}"
            
            # Check day is valid for the year
            if day > 366:
                return False, "Day out of range"
            
            return True, f"Valid - Year: {year}, Gender: {gender}"
            
        except ValueError:
            return False, "Invalid numeric values"


def print_separator():
    """Print a visual separator"""
    print("=" * 70)


def print_result(nic: str, is_accepted: bool, trace: List[str], 
                final_state: str, semantic_valid: bool, semantic_msg: str):
    """Print formatted validation result"""
    print_separator()
    print(f"Input NIC: {nic}")
    print(f"Length: {len(nic)}")
    print(f"\nState Trace: {' → '.join(trace)}")
    print(f"Final State: {final_state}")
    print(f"\n{'✓ ACCEPTED' if is_accepted else '✗ REJECTED'} by DFA")
    
    if is_accepted:
        print(f"Semantic Validation: {'✓ PASSED' if semantic_valid else '✗ FAILED'}")
        print(f"Details: {semantic_msg}")
    
    print_separator()
    print()


def run_test_suite():
    """Run comprehensive test suite"""
    validator = NICValidator()
    
    test_cases = [
        # Old format - Valid
        ("891234567V", True, "Old format - Male, born 1989, day 123"),
        ("851234567X", True, "Old format - Female, born 1985, day 123"),
        ("001234567X", True, "Old format with X - born 1900"),
        
        # New format - Valid
        ("199851234567", True, "New format - Female, born 1998"),
        ("200012345678", True, "New format - born 2000"),
        ("195501234567", True, "New format - old person born 1955"),
        
        # Invalid cases
        ("123456V", False, "Too short"),
        ("19981234567", False, "11 digits - neither format"),
        ("900012345678", False, "New format starting with 9 - invalid year"),
        ("891234567A", False, "Wrong suffix (A instead of V/X)"),
        ("391234567V", True, "Old format - Male, born 1939"),
        ("89AB123456V", False, "Letters in numeric section"),
        ("891234567", False, "Old format missing V/X"),
        ("8990123456V", False, "Invalid day (901)"),
    ]
    
    print("\n" + "=" * 70)
    print("SRI LANKAN NIC VALIDATOR - TEST SUITE")
    print("=" * 70)
    print()
    
    passed = 0
    failed = 0
    
    for nic, expected, description in test_cases:
        is_accepted, trace, final_state = validator.validate(nic)
        semantic_valid, semantic_msg = validator.validate_semantic(nic)
        
        # Check if test passed
        test_passed = (is_accepted == expected)
        
        if test_passed:
            passed += 1
            status = "✓ PASS"
        else:
            failed += 1
            status = "✗ FAIL"
        
        print(f"{status} | {description}")
        print(f"       Input: {nic}")
        print(f"       Expected: {'ACCEPT' if expected else 'REJECT'}, "
              f"Got: {'ACCEPT' if is_accepted else 'REJECT'}")
        print()
    
    print_separator()
    print(f"Test Results: {passed} passed, {failed} failed out of {len(test_cases)} tests")
    print_separator()


def interactive_mode():
    """Interactive mode for user input"""
    validator = NICValidator()
    
    print("\n" + "=" * 70)
    print("INTERACTIVE NIC VALIDATION MODE")
    print("=" * 70)
    print("\nEnter Sri Lankan NIC numbers to validate.")
    print("Commands: 'quit' to exit, 'test' to run test suite, 'help' for info")
    print()
    
    while True:
        try:
            user_input = input("Enter NIC (or command): ").strip()
            
            if user_input.lower() == 'quit':
                print("Exiting. Thank you!")
                break
            
            elif user_input.lower() == 'test':
                run_test_suite()
                continue
            
            elif user_input.lower() == 'help':
                print("\nValid NIC Formats:")
                print("  • Old: 9 digits + V/X (e.g., 199812345V)")
                print("  • New: 12 digits (e.g., 199851234567)")
                print("\nYear: Must start with 1 or 2 (19XX or 20XX)")
                print("Day: 001-366 (males), 501-866 (females)")
                print()
                continue
            
            elif not user_input:
                continue
            
            # Validate the NIC
            is_accepted, trace, final_state = validator.validate(user_input)
            semantic_valid, semantic_msg = validator.validate_semantic(user_input)
            
            print_result(user_input, is_accepted, trace, final_state, 
                        semantic_valid, semantic_msg)
            
        except KeyboardInterrupt:
            print("\n\nExiting. Thank you!")
            break
        except Exception as e:
            print(f"Error: {e}\n")


def main():
    """Main entry point"""
    print("""
    ╔══════════════════════════════════════════════════════════════════╗
    ║                                                                  ║
    ║          SRI LANKAN NIC VALIDATOR - DFA IMPLEMENTATION          ║
    ║                                                                  ║
    ║              Automata Theory Make-Up Assignment                  ║
    ║                                                                  ║
    ╚══════════════════════════════════════════════════════════════════╝
    """)
    
    while True:
        print("\nSelect Mode:")
        print("1. Run Test Suite")
        print("2. Interactive Validation")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == '1':
            run_test_suite()
        elif choice == '2':
            interactive_mode()
        elif choice == '3':
            print("Thank you for using NIC Validator!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()