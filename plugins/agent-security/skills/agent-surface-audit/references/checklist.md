# Implementation review checklist

Use after `scripts/inspect_tools.py`. One pass per tool, in the order the
script ranked them. Record a yes/no and a file:line for each item; "didn't
check" is a finding against the review, not the server.

## Parameter handling

- Is any parameter concatenated or templated into a shell command, SQL
  string, URL, file path, or `eval`? (Look for `subprocess`, `os.system`,
  `exec`, f-strings into `cursor.execute`, `open(param)`, `requests.get(param)`.)
- Are path parameters resolved against a fixed root and checked for `..`
  and symlink escape after resolution, not before?
- Are enums enforced server-side, or only declared in the schema?
- Is there any parameter the schema does not declare that the handler reads
  anyway (`kwargs`, `request.params.get(...)`)?

## Scope and side effects

- Does the tool do exactly what its description says? List any extra effect
  (logging to a remote endpoint, caching to disk, modifying state on read).
- For "read-only" tools: can a parameter make it read somewhere the user
  would not expect (another user's data, env vars, dotfiles)?
- For destructive tools: is there a server-side guard independent of the
  model (dry run, confirmation token, allowlist)? A model-supplied
  `confirm: true` is not a guard.

## Credentials and network

- Which credentials does the process hold, and from where (env, file,
  keychain)? Are they readable by any tool, or scoped to the one that needs
  them?
- Which hosts does the server contact? Is any of them not the service the
  server is named for (telemetry, update checks, "analytics")?
- Does any response from a remote host flow back into a tool result
  unescaped? That is a second injection surface: content the model reads.

## Transport and auth

- stdio: who can spawn it and with what environment?
- HTTP/SSE: is there authentication at all? Is the bind address loopback?
  Is there CSRF protection if a browser can reach it?
- Does the server accept `roots` or `sampling` requests, and does it honor
  the boundaries they imply?

## Description-level

- Has the description changed between versions? A description that grew an
  "IMPORTANT" paragraph is a rug pull, the pattern where a benign server
  later ships poisoned text.
- Does any description reference tools from *other* servers by name?
