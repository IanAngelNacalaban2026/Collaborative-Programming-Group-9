def get_pshs_equivalent(percent):
    """Maps the percentage grade to PSHS Equivalent and Adjectival Equivalent."""
    if percent >= 96:
        return 1.00, "EXCELLENT"
    elif percent >= 90:
        return 1.25, "VERY GOOD"
    elif percent >= 84:
        return 1.50, "VERY GOOD"
    elif percent >= 78:
        return 1.75, "GOOD"
    elif percent >= 72:
        return 2.00, "GOOD"
    elif percent >= 66:
        return 2.25, "SATISFACTORY"
    elif percent >= 60:
        return 2.50, "SATISFACTORY"
    elif percent >= 55:
        return 2.75, "FAIR"
    elif percent >= 50:
        return 3.00, "FAIR"
    elif percent >= 40:
        return 4.00, "FAILED ON CONDITION"
    else:
        return 5.00, "FAILED"

def calculate_grades():
    print("--- PSHS Quarter Grade Calculator ---")
    
    try:
        # Input tentative grades for each quarter
        t1 = float(input("Enter Tentative Grade for Q1 (%): "))
        t2 = float(input("Enter Tentative Grade for Q2 (%): "))
        t3 = float(input("Enter Tentative Grade for Q3 (%): "))
        t4 = float(input("Enter Tentative Grade for Q4 (%): "))
        
        # Cumulative Calculation Logic
        q1 = t1
        q2 = (q1 + 2 * t2) / 3
        q3 = (q2 + 2 * t3) / 3
        q4 = (q3 + 2 * t4) / 3
        
        quarters = [q1, q2, q3, q4]
        
        print("\n" + "="*50)
        print(f"{'Quarter':<10} | {'Percent':<10} | {'Equivalent':<12} | {'Status'}")
        print("-" * 50)
        
        for i, grade in enumerate(quarters, 1):
            eq, adj = get_pshs_equivalent(grade)
            print(f"Q{i:<8} | {grade:>9.2f}% | {eq:>12.2f} | {adj}")
            
        print("="*50)
        final_eq, final_adj = get_pshs_equivalent(q4)
        print(f"FINAL GRADE: {final_eq:.2f} ({final_adj})")

    except ValueError:
        print("Invalid input. Please enter numeric values for grades.")

if __name__ == "__main__":
    calculate_grades()