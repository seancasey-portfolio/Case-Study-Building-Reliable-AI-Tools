# Case Study: Building Reliable & Well-Behaved AI Tools

### **What This Method Achieves for Your Organisation**

This document outlines a practical "quality control" framework for working with modern AI tools. It ensures that any AI-assisted work is accurate, complete, and trustworthy.

*   **Guarantees accuracy and reliability** in any automated task, from data entry to report writing, by implementing a mandatory, built-in "self-correction" process.
*   **Builds trust and confidence** in using new technology by transforming a complex AI from an unpredictable "black box" into a transparent and auditable team member that follows a clear set of rules.
*   **Eliminates common AI errors**, such as incomplete summaries, fabricated information ("hallucinations"), or the omission of key details, ensuring the final output is always production-ready.

### **Practical, Real-World Use Cases**

This framework is a critical safeguard for any process where you rely on an AI tool to produce important work:

*   **Ensuring Complete Data Migration:** When using an AI to help transfer supporter information to a new CRM, this method guarantees that every single field and note is copied completely and without summarisation.
*   **Creating Accurate Board Reports:** When asking an AI to synthesise data for a board report, this framework ensures the final document is a complete and faithful representation of the source data, with no critical details omitted.
*   **Automating Funder Communications:** Before sending an AI-drafted thank-you letter to a major donor, this process provides a final quality check to ensure it is accurate, personalised, and complete.

---

### **The Technical Approach: A High-Level Look at the Method**

The core of this method is a simple but powerful required checklist that any AI tool must follow before it is allowed to show its work.

1.  **Step 1: The tool does a full first draft of the work privately.** First, the AI tool is required to complete the entire task silently, in an internal draft that is not visible to the user. For example, if asked to copy a supporter's record, it must create a full, complete copy of that record in its own memory.

2.  **Step 2: It then must stop and check its own work.** Second, and most critically, the tool is required to perform a self-audit. It must compare its internal draft to the original source material and ask itself a direct, mandatory question **based on a human-provided checklist:** "Is my work incomplete in any way? Does it contain any summaries or placeholders?"

3.  **Step 3: The tool is only allowed to show its work if it passes its own quality check.** The AI is only permitted to provide its final output if the answer to its own internal audit is "No." If the answer is "Yes," it is forced to go back to Step 1 and do the work again correctly. **This required checking process guarantees** that only complete and accurate work is ever delivered.

---
### **Technical Appendix: The Demonstration Script**
    
For those interested in the practical implementation, a clean, well-commented Python script demonstrating the core methodology of this case study can be found in the `src` directory of this repository. The script is designed to be a self-contained, illustrative example, not a production-ready engine.
    
  *   [**View the script: `demo_ai_quality_framework.py`**](./src/demo_ai_quality_framework.py)

---

*Go back to the [**Main Portfolio Page**](https://github.com/seancasey-portfolio) or explore another case study:*
*   *[Turning Messy Spreadsheets into a Usable Database](https://github.com/seancasey-portfolio/Case-Study-Cleaning-Legacy-Data)*
*   *[Automating Internal Reports & Documentation](https://github.com/seancasey-portfolio/Case-Study-Automating-Internal-Documentation)*
*   *[Building Reliable & Well-Behaved AI Tools](https://github.com/seancasey-portfolio/Case-Study-Building-Reliable-AI-Tools)*
*   *[Transforming Raw Data into Compelling Stories](https://github.com/seancasey-portfolio/Case-Study-Data-To-Impact-Stories)*
