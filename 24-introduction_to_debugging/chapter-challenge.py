"""
========================================
CHAPTER CHALLENGE – DEBUG THE CODE
========================================

Find and fix all the bugs in the code below.

Original buggy code (DO NOT RUN - has errors):

def plant_recommendation(care):
    if care = 'low':
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'medium':
        print('orchid')

plant_rec('low')
plant_recommendation('medium')
plant_recommendation('high')

"""

# =========================================
# DEBUGGING EXERCISE
# =========================================

print("=== CHAPTER CHALLENGE: DEBUG THE CODE ===\n")

print("BUGGY CODE:")
print("""
def plant_recommendation(care):
    if care = 'low':          # BUG 1: = instead of ==
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'medium':    # BUG 2: duplicate condition
        print('orchid')

plant_rec('low')              # BUG 3: wrong function name
plant_recommendation('medium')
plant_recommendation('high')  # BUG 4: no case for 'high'
""")

print("\n--- ERRORS FOUND ---\n")

print("ERROR 1: Syntax Error")
print("  Line: if care = 'low'")
print("  Problem: Using = (assignment) instead of == (comparison)")
print("  Fix: if care == 'low'")
print()

print("ERROR 2: Logic Error")
print("  Line: elif care == 'medium' (second time)")
print("  Problem: Duplicate condition - never reaches 'orchid'")
print("  Fix: elif care == 'high'")
print()

print("ERROR 3: NameError")
print("  Line: plant_rec('low')")
print("  Problem: Function name is wrong")
print("  Fix: plant_recommendation('low')")
print()

print("ERROR 4: Logic Error")
print("  Problem: No handling for 'high' care level")
print("  Fix: Add else or elif for 'high'")
print()

# =========================================
# CORRECTED CODE
# =========================================

print("--- CORRECTED CODE ---\n")

def plant_recommendation(care):
    """Recommend a plant based on care level."""
    if care == 'low':
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'high':
        print('orchid')
    else:
        print('unknown care level')

# Test all cases
plant_recommendation('low')
plant_recommendation('medium')
plant_recommendation('high')
plant_recommendation('unknown')

print("\n--- SUMMARY ---")
print("""
| Bug Type   | Line | Issue                    |
|------------|------|--------------------------|
| Syntax     | 2    | = instead of ==          |
| Logic      | 6    | Duplicate condition      |
| Runtime    | 9    | Wrong function name      |
| Logic      | N/A  | Missing 'high' case      |
""")