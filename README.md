# Shenyao's GitHub Page

Welcome to the source code repository for my personal website. This site is built using [Jekyll](https://jekyllrb.com/) and the [Lanyon](https://github.com/poole/lanyon) theme by [Poole](https://github.com/poole).

## 📖 Overview

This repository contains:

- **Theme:** Lanyon (a minimal Jekyll theme)
- **Content:** Personal blog, research notes, and static pages
- **License:** GNU General Public License v2.0

## 🚀 Getting Started

### Prerequisites

To build and run the site locally, ensure you have the following installed:

- **Ruby 3.x** (recommended via Homebrew or rbenv)
- **Bundler** (`gem install bundler`)
- **Jekyll** (installed via the `github-pages` gem)

### Local Development

Follow these steps to build and serve the site locally:

1. Install dependencies:
    ```bash
    bundle install
    ```

2. Serve the site:
    ```bash
    bundle exec jekyll serve
    ```

3. Open your browser and visit:
    ```
    http://localhost:4000
    ```

For subsequent builds, you can use the shortcut `cmd + shift + B` to start the server.

## 📁 Project Structure

The repository is organized as follows:

```
├── _posts/        # Blog posts (Markdown files)
├── _layouts/      # Page templates
├── _includes/     # Shared partials (e.g., sidebar)
├── public/        # Custom CSS/JS files
├── blog/          # Blog landing page
├── index.html     # Homepage
├── about.md       # About page
```

## 🌐 Deployment

This site is deployed via GitHub Pages from the `main` branch. Once changes are pushed to the branch, they are automatically reflected on the live site.

## 🧪 Features

- **Custom Markdown Support:** Includes MathJax for rendering equations.
- **Responsive Design:** Clean, sidebar-based navigation that works on all devices.
- **Syntax Highlighting:** Built-in support for code snippets.
- **Easy Customization:** Modify content and styles to suit your needs.

## 🛠️ Build Your Own Site

If you'd like to create your own site using this repository as a starting point, follow these steps:

1. **Fork the Repository**  
    Click the "Fork" button in the top-right corner of this repository to create your own copy. Remember to rename the repository to `<your-username>.github.io` for GitHub Pages to work correctly!

2. **Clone Your Fork**  
    Clone the forked repository to your local machine:
    ```bash
    git clone https://github.com/<your-username>/<your-username>.github.io.git
    cd <your-username>.github.io
    ```

3. **Install Dependencies**  
    Ensure Ruby and Bundler are installed, then run:
    ```bash
    bundle install
    ```

4. **Customize the Content**  
    - Update `_config.yml` with your site details (e.g., title, description, URL).
    - Replace the content in `_posts/` with your own blog posts.
    - Edit `about.md` and other pages to reflect your personal information.

5. **Test Locally**  
    Preview your changes by serving the site locally:
    ```bash
    bundle exec jekyll serve
    ```
    Visit `http://localhost:4000` in your browser.

6. **Push Changes**  
    Commit and push your changes to your forked repository:
    ```bash
    git add .
    git commit -m "Customize site"
    git push origin main
    ```

7. **Enable GitHub Pages**  
    - Navigate to your repository's settings on GitHub.
    - Under "Pages," select the `main` branch as the source and save.

Your site will be live at `https://<your-username>.github.io` shortly!

## 📝 License

This project is licensed under the GNU GPL v2. See the `LICENSE` file for more details.