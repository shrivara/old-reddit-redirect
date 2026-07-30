# Old Reddit Redirect

A small Manifest V3 extension for Chromium-based browsers. It redirects Reddit page navigations to `https://old.reddit.com` while preserving the path, query string, and fragment.

## Install in Chrome or Chromium

1. Open `chrome://extensions`.
2. Enable **Developer mode**.
3. Click **Load unpacked**.
4. Select this project directory.

Examples:

- `https://www.reddit.com/r/programming/` → `https://old.reddit.com/r/programming/`
- `https://soccer.reddit.com/` → `https://old.reddit.com/r/soccer/`

Legacy subreddit subdomains are converted to `/r/<subreddit>` paths.

## How it works

The extension uses a static `declarativeNetRequest` rule. It only changes top-level page navigations, and excludes `old.reddit.com` to prevent redirect loops.

## Files

- `manifest.json` — extension metadata and permissions
- `rules.json` — redirect rules
- `icons/` — extension icons
- `scripts/generate-icons.py` — reproducible icon generator (requires Pillow)
