# Sources

Each source, what it exposes, and its contact level. All `none` unless noted:
the whole point is that someone else already did the scanning.

## Infrastructure and DNS

- **amass** (passive) — subdomain enumeration from hundreds of passive sources:
  DNS archives, certificates, web scraping. Active/brute mode is `target`.
- **crt.sh** — Certificate Transparency log search. Every TLS cert ever issued
  for a domain, which routinely exposes dev, staging and internal subdomains.
- **Shodan / Censys** — search engines for internet-connected devices. Query the
  target's ranges or domains for open ports, software versions and known issues
  found during the provider's own global sweeps.
- **dig** TXT/MX against a public resolver — mail provider and mail-security
  vendor. Against the target's authoritative nameserver it is `target`.

## Defensive stack

- **BuiltWith / Wappalyzer** — frameworks, CMS, analytics, trackers. The catalog
  lookup is `none`; a programmatic Wappalyzer run that fetches the live pages is
  `target`.
- **SPF / DMARC / DKIM records** — name the mail-security vendor (Proofpoint,
  Mimecast, Google Workspace), i.e. the phishing defense you will face.

## Credentials and exposure

- **DeHashed** — historical plaintext credential corpus. Search by domain for
  passwords employees may still be reusing.
- **TruffleHog** — scans a target's public source repos' commit history for
  leaked API keys, passwords and private keys. Reads published data; `none`.
- **Google dorking** — advanced operators against the search index, e.g.
  `site:target.com filetype:xls "password"`. The index, not the target.

## People

- **theHarvester** (passive) — emails, names and subdomains from public search
  engines and aggregators. Active DNS resolution is `target`.
- **Hunter.io** — corporate email-format discovery, to convert a name found on
  social media into a precise address.
