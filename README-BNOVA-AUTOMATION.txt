
B.NOVA WEBSITE — FINAL PACKAGE

FILES
- index.html: the single website entry file.
- assets/bnova-banner.png: wide B.NOVA banner for the home hero.
- projects.json: generated project list; do not hand-edit it.
- .github/workflows/build-project-library.yml: GitHub Actions workflow.
- scripts/build_projects.py: scans projects/*/project.json and generates projects.json.
- templates/project-template/: starter metadata and instructions.

HOW TO ADD A PROJECT
1. In the repository root, create projects/your-project-name/
2. Put project.json in that folder. Add your thumbnail image (e.g. thumbnail.png).
3. In project.json set name, category (game/tool/app/software), description, image, optional features, openUrl and downloadUrl. Use a relative image filename such as thumbnail.png. Leave unavailable links empty.
4. Commit and push. GitHub Actions regenerates projects.json; Netlify redeploys from the new commit.

IMPORTANT
The automation reads project metadata; it cannot reliably infer a project's correct name, description or category from arbitrary app files alone. Include project.json and a thumbnail for every project. For Netlify auto-deploy, the repository must be connected to the Netlify site and production deploys must be enabled. GitHub Actions needs repository Actions enabled and permission to write contents.

SOCIAL LINKS
In index.html, search for BNOVA_LINKS and fill the URL values when each official account is ready. Empty URLs stay hidden, so only real links appear in the single Other Links section.

CONTACT
The only main contact CTA says CONTACT B.NOVA on one line and opens a WhatsApp chat with a prefilled editable message.
