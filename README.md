# shenyaojin.github.io

Source for my personal website, built with [Jekyll](https://jekyllrb.com/) and
the [al-folio](https://github.com/alshedivat/al-folio) theme (v1.x, gem-based —
the theme lives in the `al_folio_core` gem; this repo holds only content and
config).

Deployed by GitHub Actions ([.github/workflows/ci.yml](.github/workflows/ci.yml))
on every push to `main`.

## Everyday tasks

### Write a blog post

Create `_posts/YYYY-MM-DD-short-name.md`:

```yaml
---
layout: post
title: "Post title"
description: "One-sentence summary (shown in the blog list and link previews)."
date: YYYY-MM-DD
categories: [geophysics]   # becomes part of the URL: /geophysics/short-name/
tags: [DAS, inversion]
# for long posts, add a table of contents:
# toc:
#   beginning: true
# to pin the post as a card on the blog page:
# featured: true
---
```

A ready-made template lives in `_drafts/paper-reading-template.md`
(drafts are not published; preview them with `jekyll serve --drafts`).
Put images in `public/images/<post-name>/` and reference them as
`/public/images/<post-name>/figure.png`.

### Add a publication

Append a BibTeX entry to `_bibliography/papers.bib`. Useful extra fields:
`pdf` (link to the PDF), `selected={true}` (show on the home page),
`abbr` (venue badge). The publications page regenerates automatically.

### Edit the about page

`_pages/about.md`. The CV iframe points at `/public/files/resume.pdf` —
**do not move that file**: it is overwritten automatically by the
[CV repository](https://github.com/shenyaojin/CV) on every push there.

### Change the accent color

`_sass/_variables.scss` — `$purple-color` is the light-theme accent,
`$cyan-color` the dark-theme accent. Everything else in that file matches the
theme gem's defaults.

### Site-wide settings

`_config.yml` — name, description, favicon emoji (`icon:`), analytics,
feature toggles. Social links live in `_data/socials.yml`.

## Local preview

```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000
```

Requires Ruby 3.3+. Optional: `brew install imagemagick` and flip
`imagemagick.enabled` to `true` in `_config.yml` for responsive WebP images.

## License

GNU GPL v2 — see [LICENSE](LICENSE). Theme © the
[al-folio](https://github.com/alshedivat/al-folio) authors (MIT).
