# Super Skills

Keep the five skills portable and self-contained. Preserve upstream attribution.
Do not add personal data, credentials, private endpoints or machine-specific paths.
Use synthetic examples. Do not import chat logs, runtime settings or Git history.
Run the package validator and installer tests before proposing changes.

## Ship gate

```bash
python3 scripts/validate.py && python3 -m unittest discover -s tests
```
