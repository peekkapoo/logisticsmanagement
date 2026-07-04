# Reference: Data Dictionary Template

A `data_dictionary.csv` (which becomes a sheet in the final Excel) must contain these columns:

- `column_name`: The exact snake_case name used in the `cleaned_data` sheet.
- `data_type`: String, Integer, Float, Date, Boolean.
- `description`: Plain english explanation of what the field represents.
- `calculation_method`: If an aggregated metric, the formula used (e.g., `sum(revenue)`). Leave blank for raw fields.
- `source`: Where the field originated (e.g., "API response", "HTML Table 2").
