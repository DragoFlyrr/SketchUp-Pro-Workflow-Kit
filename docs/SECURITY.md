# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 2.1.x   | :white_check_mark: |
| 2.0.x   | :white_check_mark: |
| < 2.0   | :x:                |

## Reporting a Vulnerability

Please report security vulnerabilities by emailing security@example.com or opening a private issue on GitHub.

## Security Practices

- Never commit `.env` files with real credentials
- Validate all file paths before processing
- Sanitize filenames to prevent path traversal
- Use temporary directories for intermediate files
