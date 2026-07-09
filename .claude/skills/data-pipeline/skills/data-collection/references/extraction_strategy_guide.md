# Reference: Extraction Strategy

## Handling Pagination
- **API Pagination:** Look for `next_page`, `cursor`, or `offset` parameters. You will need to write a wrapper loop around `collect_api.py` if fetching multiple pages.
- **URL Parameter Pagination:** Look for `?page=1` or `?start=20`. Generate the list of URLs and loop over them with `collect_static.py`.

## CSS Selectors Best Practices
- Target unique IDs (`#content-box`) or semantic classes (`.product-price`).
- Avoid brittle structural selectors (`div > div > span:nth-child(3)`).
- If the layout changes often, consider grabbing the parent container and parsing the JSON output later in the `data-cleaning` phase.

## Bypassing Issues
- If you receive `403 Forbidden`, ensure you are setting a User-Agent. If blocked by Cloudflare or CAPTCHA, **stop and ask the user**. Do not attempt to bypass security.
