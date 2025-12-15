# 🇱🇰 Sri Lankan NIC Validator - DFA Implementation

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Automata Theory](https://img.shields.io/badge/theory-DFA-orange.svg)]()

A **Deterministic Finite Automaton (DFA)** implementation for validating Sri Lankan National Identity Card (NIC) numbers. This project demonstrates practical application of automata theory to solve a real-world problem.

## 📋 Project Overview

This is a make-up assignment for **Automata Theory** that implements a DFA to validate both old and new format Sri Lankan NIC numbers.

### NIC Formats Supported

- **Old Format (Pre-2016):** 9 digits + V/X suffix  
  Example: `199812345V`
  
- **New Format (2016+):** 12 digits  
  Example: `199851234567`

## 🎯 Features

- ✅ Complete DFA with 18 states
- ✅ Validates both old and new NIC formats
- ✅ State transition tracing for debugging
- ✅ Semantic validation (year range, day validation, gender detection)
- ✅ Interactive and automated testing modes
- ✅ Comprehensive test suite with 13+ test cases
- ✅ 100% test pass rate
- ✅ Zero external dependencies

## 🏗️ Automata Design

### Formal Definition

**M = (Q, Σ, δ, q₀, F)**

- **Σ:** {0-9, V, X}
- **Q:** {q0, q1, ..., q17, qReject}
- **q₀:** q0 (start state)
- **F:** {q11, q17} (accepting states)
- **δ:** See state transition diagram below

### State Diagram

```
         q0 (Start)
          |
        [1,2] (Year must start with 1 or 2)
          ↓
       q1-q7 (Process 7 digits: year + day)
          |
    ┌─────┴─────┐
    |           |
  [2 digits]  [5 digits]
    ↓           ↓
  q8-q10     q12-q16
    |           |
  [V,X]      [digit]
    ↓           ↓
 ((q11))     ((q17))
  ACCEPT      ACCEPT
Old Format  New Format
```

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- No external dependencies required!

### Clone Repository
```bash
git clone https://github.com/yourusername/nic-validator.git
cd nic-validator
```

## 💻 Usage

### Run the Program
```bash
python nic_validator.py
```

### Interactive Mode
```python
# Select option 2 from menu
Enter NIC (or command): 199812345V

# Output:
✓ ACCEPTED by DFA
Valid - Year: 1998, Gender: Male
```

### Test Suite Mode
```bash
# Select option 1 from menu
# Runs 13 automated test cases
```

### Programmatic Usage
```python
from nic_validator import NICValidator

validator = NICValidator()

# Validate a NIC
is_valid, state_trace, final_state = validator.validate("199812345V")

if is_valid:
    print(f"✓ Valid NIC")
    print(f"State trace: {' → '.join(state_trace)}")
else:
    print(f"✗ Invalid NIC")
```

## 📊 Test Cases

### Valid Cases
| NIC Number | Format | Description |
|------------|--------|-------------|
| 199812345V | Old | Male, born 1998, day 123 |
| 856234567V | Old | Female, born 1985 |
| 200067890X | Old | With X suffix |
| 199851234567 | New | Female, born 1998 |
| 200012345678 | New | Born 2000 |

### Invalid Cases
| Input | Reason |
|-------|--------|
| 12345678V | Too short |
| 199812345A | Invalid suffix |
| 399812345V | Invalid year start |
| 19AB12345V | Non-numeric characters |

## 🧪 Testing

Run the comprehensive test suite:
```bash
python nic_validator.py
# Select option 1
```

**Test Results:** 13/13 passed (100% success rate)

## 📁 Project Structure

```
nic-validator/
│
├── nic_validator.py          # Main implementation
├── README.md                  # This file
├── REPORT.md                  # Detailed project report
├── requirements.txt           # (Empty - no dependencies)
├── demo/
│   └── demonstration.mp4      # Video demonstration
└── docs/
    ├── state_diagram.png      # DFA state diagram
    └── transition_table.pdf   # Complete transition table
```

## 🎥 Video Demonstration

A 5-7 minute video demonstration is included in the `demo/` folder covering:
1. Problem explanation (30 seconds)
2. DFA design walkthrough (2 minutes)
3. Code implementation (2 minutes)
4. Live testing with real data (1-2 minutes)
5. Summary and conclusion (30 seconds)

[Watch Demo Video](demo/demonstration.mp4)

## 📖 Documentation

Detailed documentation is available in:
- `REPORT.md` - Complete project report (2-3 pages)
- Inline code comments
- Docstrings for all functions

## 🎓 Educational Value

This project demonstrates:
- **DFA Design:** Formal automata construction
- **State Transitions:** Deterministic state-based processing
- **Pattern Matching:** Structured text validation
- **Real-world Application:** National identification system

### Key Concepts Covered
- Alphabet and state definitions
- Transition functions
- Accept and reject states
- State tracing and debugging
- Complexity analysis (O(n) time, O(n) space)

## 🔧 Technical Specifications

- **Algorithm:** Deterministic Finite Automaton (DFA)
- **Time Complexity:** O(n) where n = input length
- **Space Complexity:** O(n) for state trace
- **States:** 18 total (including reject state)
- **Accepting States:** 2 (for old and new formats)

## 🌟 Practical Applications

This validator can be integrated into:
- 🏛️ Government e-services portals
- 🏦 Banking systems for KYC verification
- 🏥 Healthcare patient registration
- 🎓 Educational institution enrollment
- 🛒 E-commerce platforms (identity verification)

## 🤝 Contributing

This is an academic project, but suggestions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**[Your Name]**  
Student ID: [Your ID]  
Course: Automata Theory  
Institution: [Your University]  
Date: December 2025

## 🙏 Acknowledgments

- Sri Lankan Department of Registration of Persons for NIC format specifications
- Course instructor for assignment guidelines
- Automata Theory textbooks: Hopcroft, Motwani & Ullman

## 📧 Contact

For questions or feedback:
- Email: [your.email@example.com]
- GitHub: [@yourusername](https://github.com/yourusername)

---

**⭐ If you find this project helpful, please give it a star!**

---

## 🔍 Quick Reference

### NIC Structure

**Old Format (10 characters):**
```
[1-2][digit][digit][digit][day][day][day][serial][serial][V/X]
 \_____/                   \_____/ \________/          \__/
   Year                      Day    Serial           Suffix
```

**New Format (12 digits):**
```
[1-2][digit][digit][digit][day][day][day][serial][serial][serial][serial][serial]
 \_____/                   \_____/ \_________________________________/
   Year                      Day                Serial
```

### Gender Encoding
- **Male:** Day 001-366
- **Female:** Day 501-866 (actual day + 500)

### Commands
```bash
# Run program
python nic_validator.py

# Interactive validation
> 2 [Enter]
> 199812345V [Enter]

# Run tests
> 1 [Enter]

# Exit
> 3 [Enter]
```

---

