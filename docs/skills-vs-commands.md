# Claude Skills vs Slash Commands

**Skills** are model-invoked capabilities that Claude automatically uses when relevant. **Slash commands** are user-invoked prompts that you trigger explicitly by typing `/command`.

## Quick Comparison

| Feature | Slash Commands | Skills |
|---------|---------------|--------|
| Invocation | You type `/cmd` | Claude decides automatically |
| Structure | Single `.md` file | Directory with multiple resources |
| Complexity | Simple prompts | Complex workflows |
| Discovery | Manual | Automatic |
| Parameters | ✅ Supported | ❌ Not supported |

## Notes

### Parameters
Slash commands support parameters using `$1`, `$2`, `$ARGUMENTS`, etc., allowing you to pass values when invoking them (e.g., `/review-pr 123 high`). Skills do not support parameters since they are automatically invoked by Claude based on context.

### Nested Calls
You can combine both features by creating a slash command that accepts parameters and then invokes a Skill through natural language prompts. For example, a slash command `/analyze $1 $2` could contain a prompt like "Analyze @$1 for $2 issues" which would trigger Claude to use relevant Skills automatically.
