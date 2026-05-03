def get_pshs_equivalent(percent):
    """Maps the percentage grade to PSHS GEC and Adjectival Equivalent."""
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

def calculate_tentative(q_num):
    """Collects FA/SA scores and calculates the weighted Tentative Grade."""
    print(f"\n--- Data Entry for Quarter {q_num} ---")
    
    # Collect 3 Formative Assessments
    fa_scores = []
    for i in range(1, 4):
        score = float(input(f"  Enter FA {i} score (%): "))
        fa_scores.append(score)
    
    # Collect 3 Summative Assessments
    sa_scores = []
    for i in range(1, 4):
        score = float(input(f"  Enter SA {i} score (%): "))
        sa_scores.append(score)
    
    # 1. Calculate Averages
    fa_avg = sum(fa_scores) / 3
    sa_avg = sum(sa_scores) / 3
    
    # 2. Apply Weights (30% FA, 70% SA)
    tentative = (fa_avg * 0.30) + (sa_avg * 0.70)
    
    print(f"  > FA Avg: {fa_avg:.2f}% | SA Avg: {sa_avg:.2f}%")
    print(f"  > Tentative Grade for Q{q_num}: {tentative:.2f}%")
    
    return tentative

def main():
    print("=====================================================")
    print("      PSHS CUMULATIVE QUARTER GRADE CALCULATOR       ")
    print("      (Weights: 30% FA Average, 70% SA Average)      ")
    print("=====================================================")
    
    try:
        # Store tentative grades for each quarter
        t_grades = []
        for q in range(1, 5):
            t_grades.append(calculate_tentative(q))
        
        # 3. Recursive Cumulative Logic
        # Q1 = T1
        # Qn = (Q_{n-1} + 2*Tn) / 3
        q_final = [0.0] * 4
        q_final[0] = t_grades[0]
        for i in range(1, 4):
            q_final[i] = (q_final[i-1] + 2 * t_grades[i]) / 3
            
        # 4. Final Output Table
        print("\n" + "="*70)
        print(f"{'Quarter':<8} | {'Tentative':<12} | {'Cumulative':<12} | {'GEC':<6} | {'Status'}")
        print("-" * 70)
        
        for i in range(4):
            gec, status = get_pshs_equivalent(q_final[i])
            print(f"Q{i+1:<7} | {t_grades[i]:>10.2f}% | {q_final[i]:>10.2f}% | {gec:>6.2f} | {status}")
            
        print("="*70)
        final_gec, final_status = get_pshs_equivalent(q_final[3])
        print(f"FINAL GRADE FOR THE YEAR: {final_gec:.2f} ({final_status})")
        print("="*70)

    except ValueError:
        print("\n[Error] Invalid input. Please enter numeric values (0-100).")

if __name__ == "__main__":
    main()
