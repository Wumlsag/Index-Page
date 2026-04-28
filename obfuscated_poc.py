import random

# --- REFINEMENT (Step 4): Identifier Renaming ---
# We use non-descriptive names for the internal logic classes to hinder human comprehension[cite: 1766].

class NDG_m0:
    """
    Simulates the paper's 'Non-deterministic Generator' (NDG) class[cite: 1880].
    This manages the Dynamic Predicate Variable.
    """
    def __init__(self, count):
        self.state = random.randint(0, count - 1)

    def mvn(self):
        # Dynamically updates the state at runtime[cite: 1880].
        self.state = (self.state + 1) % 3

    def sn(self, target_id):
        # The Selection method determining which clone to execute[cite: 1881].
        return self.state == target_id

# --- SELECT (Step 2): Semantically Equivalent Code Clones ---
# Each 'clone' provides identical functionality but has a different AST.

def c1_bubble_sort(data):
    """Clone 1: Traditional Bubble Sort."""
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def c2_selection_sort(data):
    """Clone 2: Selection Sort (structurally dissimilar)[cite: 1864]."""
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

# --- LINK (Step 3): Dynamic Opaque Predicate Selection ---

def s(input_data):
    """
    Obfuscated entry point for sortData().
    The original logic is replaced by a non-deterministic combination of clones.
    """
    # Initialize or update the dynamic predicate variable[cite: 1880].
    # In the paper, 'm_0' is the correlated boolean variable.
    global m_0
    if 'm_0' not in globals():
        m_0 = NDG_m0(3)
    else:
        m_0.mvn()

    # The conditional logic acts as the 'Linker' between clones[cite: 1831].
    # An attacker cannot statically determine which branch is taken[cite: 1765].
    if m_0.sn(0):
        # Executes Clone 1 (Bubble)
        return c1_bubble_sort(input_data)
    elif m_0.sn(1):
        # Executes Clone 2 (Selection)
        return c2_selection_sort(input_data)
    else:
        # Executes the original logical fragment or a third clone.
        return sorted(input_data)

# --- EXECUTION (Proof of Concept) ---
if __name__ == "__main__":
    test_data = [54, 23, 89, 12, 1]
    print(f"Original Data: {test_data}")
    
    # Each run potentially triggers a different structural path[cite: 1765].
    result = s(test_data)
    print(f"Obfuscated Output: {result}")