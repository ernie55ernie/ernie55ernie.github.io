# ernie55ernie.github.io
Home page for some code project [http://ernie55ernie.github.io](https://ernie55ernie.github.io)

## 
```bash
bundle init
bundle add jekyll
bundle add jekyll-seo-tag
bundle install
```
Add "#" to the beginning of the line that starts with gem "jekyll" to comment out this line.

Add the github-pages gem by editing the line starting with # gem "github-pages". Change this line to:

```
gem "github-pages", "~> GITHUB-PAGES-VERSION", group: :jekyll_plugins
```

Replace GITHUB-PAGES-VERSION with the latest supported version of the github-pages gem. You can find this version here: ["Dependency versions."](https://pages.github.com/versions/)

The correct version Jekyll will be installed as a dependency of the github-pages gem.

```
gem "webrick"
```

### Reference

- [Creating a GitHub Pages site with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll)
- [Jekyll serve fails on Ruby 3.0](https://github.com/jekyll/jekyll/issues/8523)

## Solved Environment Problems
- [Could not find commonmarker-0.17 1.3 in any of the sources](https://github.com/jekyll/jekyll/issues/7274)
- [Verifying Brave Rewards on GitHub Pages using Jekyll](https://www.derekcroote.com/2019/07/18/github-pages-brave.html)