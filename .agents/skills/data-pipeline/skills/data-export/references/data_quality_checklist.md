# Reference: Data Quality Checklist

Before running `export_data.py` and presenting the final file to the user, ensure:
- [ ] No internal working columns (like `_merge`) are exposed unless requested.
- [ ] All dates are ISO 8601 strings.
- [ ] Row counts from `clean_data.py` match the `cleaned_data` CSV.
- [ ] The `validate.py` script returns a clean pass on the final CSV.
