# Reference: Error Taxonomy

When flagging bad data inside a cell (instead of dropping it), use these standard terms in a dedicated `data_quality_flag` column, or as the value itself if strictly necessary:

- `[ERR_MISSING]`: The source simply did not have the data.
- `[ERR_PARSE]`: The data existed but could not be parsed (e.g., a date written as "sometime next week").
- `[ERR_CONTRADICTION]`: Two merged sources gave different values for this exact cell.
- `[ERR_OUTLIER]`: The value passed parsing but failed sanity checks during `validate.py`.
