## CV Automation

Given that maintaining my gh-pages and Awesome-CV is a hassle, I want to store my data in one place. This repo is supposed to do just that and is ought to serve as an entry-point to build my gh-pages and my Awesome-CV in a CI/CD way.

- On push to this repo, a repository_dispatch to my gh-pages and Awesome-CV repos should happen.
- On receiving the repository_dispatch the other repos will checkout this repo and build the gh-pages (and publish) and CV respectively.
