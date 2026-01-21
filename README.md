Calgary Fastpitch — Coming Soon landing page

This is a tiny static landing page that shows a "Big changes coming soon" message and references the live site's favicon and (optionally) logo.

Files added
- `index.html` — The landing page.
- `styles.css` — Minimal styling.
- `README.md` — This file.

Notes and assumptions
- The favicon and logo are referenced from the live site at `https://calgaryfastpitch.com/favicon.ico` and `https://calgaryfastpitch.com/images/logo.png` respectively. If those assets change or are blocked, the page will still display the message (the logo will hide on error).
- I didn't download any assets; the page links to the site's favicon directly. If you prefer offline copies, download the favicon/logo into an `assets/` directory and update the `index.html` references.

Preview locally
You can open `index.html` directly in a browser (double-click) or serve it with a simple HTTP server. From PowerShell in this folder:

Calgary Fastpitch — Coming Soon landing page

This is a tiny static landing page that shows a "Big changes coming soon" message and uses local SVG fallbacks for the favicon and logo.

Files added
- `index.html` — The landing page.
- `styles.css` — Minimal styling.
- `README.md` — This file.

Additional files added by this update
- `assets/` — contains generated `favicon.svg` and `logo.svg` used as local fallbacks.
 - `assets/` — contains generated `favicon.svg` and `logo.svg` used as local fallbacks. You also downloaded `assets/favicon.png`, which the site will now prefer for the favicon.
- `.github/workflows/deploy.yml` — GitHub Actions workflow to publish the site to `gh-pages` on pushes to `main`.
- `tests/smoke.ps1` — small PowerShell smoke test to check critical files exist.
 - `assets/` — contains generated `favicon.svg` and `logo.svg` used as local fallbacks, and your uploaded `CFL-BK-BGWhite.svg` which is now used as the site logo and preferred SVG favicon.
 - `assets/favicon.svg` — small wrapper SVG that references `CFL-BK-BGWhite.svg` so browsers that accept SVG favicons can use it.

Notes and assumptions
- I attempted to download the remote favicon/logo automatically. The favicon returned a 0-byte result and the remote logo could not be fetched in this environment, so I generated small local SVG assets as reliable fallbacks. If you prefer the original assets, download them into `assets/` and replace `favicon.svg`/`logo.svg`.

Preview locally
You can open `index.html` directly in a browser (double-click) or serve it with a simple HTTP server. From PowerShell in this folder:

```powershell
# start a quick local server on port 8000
python -m http.server 8000
# then visit http://localhost:8000 in your browser
```

Deploy to GitHub Pages (from `public/` folder)
1. Push this repository to GitHub (branch `main`).
2. The workflow at `.github/workflows/deploy.yml` will run on push and publish the repository `public/` folder to GitHub Pages using GitHub's Pages actions.
	- The workflow runs a quick smoke test, uploads `./public` as a Pages artifact, and uses the `actions/deploy-pages` action to publish it.
3. Repository permissions: ensure Actions workflows have permission to write Pages artifacts:
	- Go to Settings → Actions → General → Workflow permissions and enable "Read and write permissions" for GitHub Actions. This lets the workflow publish the site using the built-in GITHUB_TOKEN.
	- If your organization blocks write permissions, create a Personal Access Token (repo scope) and add it to repo Secrets (name it `GH_PAGES_PAT`) and I can update the workflow to use it.
4. After the action completes, enable GitHub Pages for the repository (if not auto-enabled) and set the source to "GitHub Pages" (the Pages action will handle publishing to the Pages system).
5. If you prefer to publish a different folder, update the `path` in the `upload-pages-artifact` step in `.github/workflows/deploy.yml`.

Run the smoke test locally
From PowerShell in the project folder:

```powershell
# run the smoke test
pwsh .\tests\smoke.ps1
```

Next steps (optional)
- Replace `assets/favicon.svg` and `assets/logo.svg` with the original site assets if you want exact branding.
- Tweak colors/copy, add a contact subscribe form, or wire up a small CI test.

