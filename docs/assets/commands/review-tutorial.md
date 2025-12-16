# Review and Polish Tutorial

Review and polish the tutorial file: $ARGUMENTS

## Phase 1: Read and Analyze

1. **Read the tutorial file** specified in the arguments
2. **Review against these quality criteria:**

### Content Quality
- [ ] Clear, descriptive title
- [ ] Engaging hook (2-4 sentences combining problem + analogy + why it matters)
- [ ] Key Concepts section (3-4 terms max, bullet format)
- [ ] What You'll Need section with prerequisites and time estimate
- [ ] Logical step flow that builds progressively
- [ ] Next Steps section (2-3 suggestions)
- [ ] Troubleshooting section (2-3 common issues)

### Formatting Standards
- [ ] `[Home](./)` link at the very top
- [ ] Steps formatted as `## Step N: Action Verb + What`
- [ ] Sub-steps use bullets (-) not numbers
- [ ] Bold for UI elements: **Button Name**
- [ ] Backticks for commands: `command`
- [ ] Code blocks for multi-line commands
- [ ] Short paragraphs (2-3 sentences max)
- [ ] Creation date at end with author link

### Beginner-Friendliness
- [ ] Menu-based instructions preferred over keyboard shortcuts
- [ ] Platform-specific differences noted (Windows/Mac)
- [ ] Exact click targets described (e.g., "Click the **gear icon** in lower left")
- [ ] No assumed prior knowledge
- [ ] Jargon explained or avoided
- [ ] Links to tools on first mention
- [ ] Prerequisite tutorials are all listed

### Technical Accuracy
- [ ] Commands are correct and complete
- [ ] UI instructions match current versions
- [ ] Prerequisites are accurate and sufficient
- [ ] Time estimates are realistic

### Writing Quality
- [ ] No typos or grammar errors
- [ ] Consistent terminology throughout
- [ ] No unnecessary introductory/ending sentences in steps
- [ ] Concise language (remove filler words)

## Phase 2: Report Findings

Present a summary to the user:

1. **Overall Assessment** - Brief evaluation of the tutorial quality
2. **Issues Found** - Categorized list:
   - Typos/Grammar
   - Flow Issues
   - Accuracy Concerns
   - Formatting Problems
   - Beginner-Friendliness Gaps
3. **Recommended Changes** - Specific fixes with line references

Ask the user: "Would you like me to apply these fixes?"

## Phase 3: Apply Fixes

After user approval:

1. Make all corrections using the Edit tool
2. Preserve the author's voice and style
3. Keep changes minimal - fix issues without rewriting
4. Update the todo list as you work through fixes
5. Report completed changes

## Guidelines Reference

These tutorials follow the style guide in `.claude/commands/tutorial.md`. Key principles:

- **Target audience**: Complete beginners with no coding experience
- **Length**: Aim for ~400 lines or less
- **Tone**: Friendly but concise, no unnecessary praise or filler
- **Focus**: Hands-on, minimal theory, learn by doing
