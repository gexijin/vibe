# Medical Research Skill

A Claude Code skill that retrieves scientific papers from PubMed and creates accessible, plain-language research summaries.

## What It Does

This skill bridges the gap between complex scientific literature and general understanding by:

1. **Retrieving** - Searches PubMed for relevant scientific papers on any biomedical topic
2. **Analyzing** - Identifies key themes, findings, and implications from multiple papers
3. **Translating** - Converts technical research into plain language that anyone can understand
4. **Summarizing** - Creates comprehensive markdown reports with clear structure and context

## When to Use

The skill automatically activates when you:
- Ask about medical or scientific research (e.g., "What's the latest on diabetes treatment?")
- Request information about diseases, treatments, or clinical trials
- Want to understand scientific consensus on health topics
- Need to catch up on recent research in a specific area

## Quick Start

Simply ask natural questions:

```
Summarize research on immunotherapy for lung cancer
```

```
What does research say about ketogenic diet for epilepsy?
```

```
Tell me about recent CRISPR gene therapy studies
```

Claude will automatically:
1. Use the skill to search PubMed
2. Analyze the most recent papers
3. Create a comprehensive plain-language summary
4. Save it as a markdown file in your working directory

## Output Format

Each summary includes:

- **Overview**: What the research area is and why it matters
- **Key Research Themes**: Major findings organized by topic
- **Clinical Implications**: What this means for patients and treatment
- **Challenges**: Current problems and limitations
- **Key Terminology**: Definitions of important scientific terms
- **Selected Papers**: Highlighted papers with PMIDs and links
- **Summary**: Overall synthesis and future directions

## File Naming

Summaries are saved as:
```
Research_Summary_{Topic}_{YYYY-MM-DD}.md
```

Examples:
- `Research_Summary_Immunotherapy_Melanoma_2025-12-13.md`
- `Research_Summary_Alzheimers_Treatment_2025-12-13.md`

## Requirements

The skill includes a built-in `pubmed_search.py` script located at `.claude/skills/medical-research/pubmed_search.py`. This script requires:
- Python 3.x
- Biopython library (`pip install biopython`)

These should already be installed in the Vibe environment.

## Customization

### Retrieve More Papers

Edit `.claude/skills/medical-research/pubmed_search.py` and change the `max_results` parameter:

```python
papers = search_pubmed(query, max_results=20)  # Default is 10
```

### Set Your Email

PubMed requires an email address for API access. Update in `.claude/skills/medical-research/pubmed_search.py`:

```python
Entrez.email = "your.email@example.com"
```

### Search Strategy

For better results:

**Be Specific**:
- ✓ "immunotherapy for triple-negative breast cancer"
- ✗ "cancer treatment"

**Use Medical Terms**:
- ✓ "myocardial infarction rehabilitation"
- ✗ "heart attack recovery"

**Include Context**:
- ✓ "CRISPR gene editing sickle cell disease"
- ✗ "CRISPR"

## Examples

### Example 1: Treatment Research

**Input:**
```
Summarize research on immunotherapy for breast cancer
```

**What Happens:**
1. Searches PubMed for "immunotherapy breast cancer"
2. Finds 14,190 papers, retrieves 10 most recent
3. Identifies themes: PD-L1 paradox, resistance mechanisms, novel approaches
4. Creates 3,000+ word plain-language summary
5. Saves as `Research_Summary_Immunotherapy_Breast_Cancer_2025-12-13.md`

### Example 2: Disease Mechanism

**Input:**
```
What does research say about Alzheimer's disease causes?
```

**What Happens:**
1. Skill activates automatically
2. Searches for "Alzheimer's disease pathogenesis"
3. Explains amyloid hypothesis, tau protein, neuroinflammation in accessible terms
4. Discusses competing theories and current debates
5. Saves comprehensive summary

### Example 3: Emerging Technology

**Input:**
```
Tell me about mRNA vaccine technology
```

**What Happens:**
1. Searches "mRNA vaccine mechanism clinical trials"
2. Explains how mRNA vaccines work (using simple analogies)
3. Covers COVID-19 applications and future potential
4. Discusses safety, efficacy, and ongoing research
5. Saves detailed summary

## Tips for Best Results

### Getting Comprehensive Summaries

- Be specific about what aspect interests you
- Mention if you want focus on mechanisms, treatments, or clinical trials
- Specify populations if relevant (pediatric, elderly, specific conditions)

### Understanding Technical Topics

- The skill will define key terms in a "Key Terminology" section
- Explanations use analogies and plain language
- Complex mechanisms are broken down step-by-step

### Finding Specific Papers

- Use the "Selected Papers" section for highlighted research
- Each paper includes PMID (PubMed ID) for direct lookup
- Links provided for one-click access to PubMed

### Follow-Up Questions

After receiving a summary, you can ask:
- "Can you explain the [specific mechanism] in more detail?"
- "Which of these approaches is most promising?"
- "Are there clinical trials I can look into?"

## Limitations

**What This Skill Does:**
- Summarizes published peer-reviewed research
- Explains scientific concepts in plain language
- Identifies trends and patterns in literature
- Provides educational information

**What This Skill Doesn't Do:**
- Provide medical advice or treatment recommendations
- Replace consultation with healthcare providers
- Guarantee accuracy of cited research
- Cover unpublished or non-PubMed indexed research

**Currency Note:**
- Focuses on most recent papers (typically last 1-2 years)
- Very new research (last few weeks) may not yet be indexed
- Some emerging topics may have limited papers available

## Troubleshooting

### "No papers found"

Try:
- Broadening search terms (use general terms)
- Checking spelling of medical terms
- Using alternative terminology (e.g., "myocardial infarction" vs "heart attack")
- Verifying the topic has biomedical research (PubMed covers life sciences)

### "Papers are too technical"

The skill should automatically translate complex findings. If unclear:
- Ask for clarification on specific terms
- Request the skill focus on clinical implications
- Check the "Key Terminology" section for definitions

### "Results seem narrow"

- Modify the `.claude/skills/medical-research/pubmed_search.py` script to retrieve more papers
- Use broader search terms
- Ask for a follow-up search on related topics

## Technical Details

### How It Works

1. **Query Processing**: Converts your natural language question into a PubMed search query
2. **Paper Retrieval**: Uses Biopython's Entrez module to query PubMed API
3. **Analysis**: Reads titles, abstracts, authors, and metadata from retrieved papers
4. **Synthesis**: Identifies themes, patterns, and key findings across papers
5. **Translation**: Converts technical language to plain English with analogies and context
6. **Structuring**: Organizes information into clear sections with hierarchy
7. **Documentation**: Saves as markdown file with proper citations

### Data Sources

- **Primary**: PubMed/MEDLINE (https://pubmed.ncbi.nlm.nih.gov/)
- **Coverage**: 35+ million biomedical literature citations
- **Update Frequency**: Daily; new papers added continuously
- **Access**: Free, public database maintained by US National Library of Medicine

### Quality Assurance

Summaries are designed to:
- Write at 10th-grade reading level (accessible to general audience)
- Define all technical terms and abbreviations
- Cite specific papers with PMIDs for verification
- Note limitations and areas of uncertainty
- Include educational disclaimers
- Present balanced view including challenges

## Contributing

To improve this skill:

1. **Enhance the script**: Modify `.claude/skills/medical-research/pubmed_search.py` to retrieve more metadata
2. **Improve templates**: Update `SKILL.md` with better structure suggestions
3. **Add examples**: Contribute sample summaries to `EXAMPLES.md`
4. **Report issues**: Note any topics that produce poor summaries

## Related Resources

- **PubMed**: https://pubmed.ncbi.nlm.nih.gov/
- **Biopython Tutorial**: https://biopython.org/wiki/Documentation
- **MeSH Browser**: https://meshb.nlm.nih.gov/ (for finding medical search terms)
- **Plain Language Guidelines**: https://www.plainlanguage.gov/

## Version History

- **v1.0** (December 2025): Initial release
  - PubMed integration via Biopython
  - Plain-language summarization
  - Automatic file saving
  - Comprehensive templates

## License

Part of the Vibe project. See main repository for license details.

---

**Questions or Issues?**

If you encounter problems or have suggestions for improvement, please open an issue in the Vibe repository.
