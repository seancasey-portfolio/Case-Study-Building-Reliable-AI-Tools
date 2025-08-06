# TSD-ID: SSD-3
# Filename: demo_ai_quality_framework.py (v1.2)
# Purpose: To provide a clear, simplified demonstration of a quality assurance
#          framework for AI-generated content. This script simulates a mandatory
#          "cognitive harness" that forces an AI to check its own work against
#          quality standards before delivering an output. This serves as the
#          technical appendix for the "Case-Study-Building-Reliable-AI-Tools"
#          portfolio piece.

# --- INPUT DATA ---
# A simple source document and two drafts generated from it. One draft is
# deliberately flawed to demonstrate the failure path of the quality audit.
SOURCE_DOCUMENT = "This is the full, complete, and unabridged source document for Project Nightingale."
FLAWED_DRAFT = "This is the full... source document for Project Nightingale."
CORRECT_DRAFT = "This is the full, complete, and unabridged source document for Project Nightingale."

# --- CONFIGURATION ---
# This checklist represents the non-negotiable quality standards that any
# generated artifact must meet. In a real system, this could be much more complex.
QUALITY_CHECKLIST = {
    "is_unabridged": lambda draft: "..." not in draft,
    "is_complete": lambda draft, source: len(draft) >= len(source) * 0.95,
}

def step1_generate_internal_draft(source_text, is_flawed=False):
    """
    Simulates the AI's first attempt at generating an output.
    
    This function represents the raw, unchecked output of a language model.
    We can force it to produce a flawed version for demonstration purposes.
    """
    print("Step 1: AI generating internal draft...")
    if is_flawed:
        print("  -> (Simulating a flawed generation with summarization)")
        return FLAWED_DRAFT
    else:
        print("  -> (Simulating a correct, complete generation)")
        return CORRECT_DRAFT

def step2_internal_audit(draft, source):
    """
    Simulates the mandatory self-correction and quality assurance loop.

    This is the core of the "cognitive harness." Before the AI is allowed to
    present its output, it must check its own work against a set of
    pre-defined, objective quality standards.

    Args:
        draft (str): The internally generated text.
        source (str): The original source text for comparison.

    Returns:
        bool: True if the audit passed, False otherwise.
    """
    print("\nStep 2: Performing mandatory internal quality audit...")
    
    # Check for summarization (e.g., ellipses)
    if not QUALITY_CHECKLIST["is_unabridged"](draft):
        print("  - Failed: Draft is not unabridged (contains '...').")
        return False
        
    # Check for completeness (e.g., significant truncation)
    if not QUALITY_CHECKLIST["is_complete"](draft, source):
        print("  - Failed: Draft is significantly shorter than the source.")
        return False

    print("  - Passed: All quality checks met.")
    return True

def step3_generate_final_output(draft):
    """
    Represents the final, approved output being delivered to the user.
    
    This function is only ever called if the internal audit (Step 2) passes,
    ensuring that the user only ever sees high-quality, compliant results.
    """
    print("\nStep 3: Generating final, quality-approved output for user.")
    print("-----------------------------------------------------")
    print(draft)
    print("-----------------------------------------------------")


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("--- Demonstrating AI Quality Framework ---\n")

    # --- SCENARIO 1: FLAWED DRAFT ---
    # This demonstrates the "failure" path, where the AI's first attempt
    # does not meet quality standards and is therefore rejected internally.
    print("--- SCENARIO 1: A flawed draft is generated ---")
    internal_draft_1 = step1_generate_internal_draft(SOURCE_DOCUMENT, is_flawed=True)
    
    audit_passed_1 = step2_internal_audit(internal_draft_1, SOURCE_DOCUMENT)
    
    if not audit_passed_1:
        print("\n  -> Conclusion: Output blocked. Retrying generation or escalating...")
    print("\n" + "="*50 + "\n")


    # --- SCENARIO 2: CORRECT DRAFT ---
    # This demonstrates the "success" path. The AI generates a compliant draft,
    # it passes the internal audit, and is therefore delivered to the user.
    print("--- SCENARIO 2: A correct draft is generated ---")
    internal_draft_2 = step1_generate_internal_draft(SOURCE_DOCUMENT, is_flawed=False)
    
    audit_passed_2 = step2_internal_audit(internal_draft_2, SOURCE_DOCUMENT)
    
    if audit_passed_2:
        step3_generate_final_output(internal_draft_2)
        print("\n  -> Conclusion: High-quality output successfully delivered.")

    print("\n--- Framework Demonstration Complete ---")
