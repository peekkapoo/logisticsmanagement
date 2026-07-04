# Rule: Data Ethics and Reproducibility

These constraints apply to EVERY data operation (collection, cleaning, aggregation).

1. **Never bypass access controls:** Do not bypass login walls, paywalls, CAPTCHA, or anti-bot systems. This constitutes unauthorized access and destroys pipeline reproducibility.
   - *Reason:* If a pipeline depends on an active session token or a solved CAPTCHA, it cannot be run automatically in the future.
   - *Action:* On hitting a wall, stop and ask the user for a permitted source or a provided data export.

2. **Respect polite collection practices:** Always respect `robots.txt`. Identify yourself with a real user-agent. Use polite delays and bounded retries with exponential backoff.
   - *Reason:* Aggressive crawling leads to IP bans and harms target infrastructure.
   - *Action:* No proxy rotation, stealth fingerprinting, or aggressive parallel crawling. Prefer official APIs > structured files (CSV/JSON) > HTML tables > CSS selectors > Playwright.

3. **Never fabricate missing data:** Do not invent values to fill gaps.
   - *Reason:* A blank or flagged cell is a known unknown. An invented value is a silent lie that corrupts downstream analysis permanently.
   - *Action:* Document missing data, drop it, or use explicit statistical imputation only if explicitly requested by the user.
