# Finding template

```markdown
## <ID> — <Component>: <flaw in plain words>

**Severity:** <Critical | High | Medium | Low | Info>
**Justification:** <one sentence naming demonstrated impact and likelihood, e.g. "A tested standard account read two other tenants' invoices; exploitation required only an account.">

**Affected:** <component, version, commit, endpoint, or file:line>
**Status:** <Open | Fixed in <version> | Accepted risk | Lead (not reproduced)>

### Description
<What the flaw is. Two to five sentences. Name the mechanism, not the category.>

### Reproduction
1. <Step>
2. <Step>
3. <Observed result>

<Evidence: request/response, log excerpt, output. Pasted, trimmed, not paraphrased.>

### Impact
<What the tested actor obtained or did. State preconditions explicitly. Do not
generalize from sampled actors or objects to "any" or "all" without coverage
or authoritative implementation evidence.>

### Fix
<The specific change that removes the flaw.>

### Mitigation (if fix is not immediate)
<What reduces exposure in the meantime, and what it does not cover.>

### References
<Standards, CWE, prior art, vendor advisories. "N/A" is acceptable here only.>

### Notes
<Leads, unconfirmed escalations, related observations. Nothing here affects severity.>
```
