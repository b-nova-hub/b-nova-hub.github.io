
B.NOVA Automatic Project Library

The website reads project entries from projects.json.

To add a project:
1. Create a folder inside projects/ using your project name.
2. Add a project.json file inside that folder.
3. Include name, category, description, image, features, openUrl and downloadUrl.
4. Add the project files and thumbnail image.
5. Commit your changes to the main branch.

GitHub Actions runs the project library builder when files in projects/ change.
Netlify deploys the website when committed changes are detected.

Supported categories: game, tool, app, software.
