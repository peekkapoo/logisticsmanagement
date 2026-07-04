# Reference: Data Cleaning Rules

1. **Dates:** Always coerce dates into ISO 8601 (`YYYY-MM-DD`) format. Avoid ambiguous locales (e.g., `12/11/20` could be Nov 12 or Dec 11). If ambiguous, log a warning and use Pandas `dayfirst=True` or `False` consistently.
2. **Numbers & Currencies:** Strip symbols (`$`, `€`, `£`, `%`) and commas before casting to numeric. Never keep numbers as strings if you intend to aggregate them later.
3. **Column Names:** Rename columns to `snake_case`. Strip trailing spaces. 
4. **Missing Values:**
   - If a column is critical (e.g., an `ID` or a `price` you need to sum), use `--drop-na-cols`.
   - If a categorical column is missing, use `--fill-na` to set it to `"Unknown"` or `"N/A"`.
   - Never fill numeric columns with `0` or the `mean` unless explicitly requested, as this alters the dataset's statistical reality.
