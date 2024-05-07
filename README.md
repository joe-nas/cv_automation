## CV Automation

Given that maintaining my gh-pages and Awesome-CV is a hassle, I want to store my data in one place. This repo is supposed to do just that and is ought to serve as an entry-point to build my gh-pages and my Awesome-CV in a CI/CD way.

- On push to this repo, a repository_dispatch to my gh-pages and Awesome-CV repos should happen.
- On receiving the repository_dispatch the other repos will checkout this repo and build the gh-pages (and publish) and CV respectively.
- use https://github.com/nektos/act test workflows locally

### to-do

- to separate concerns, move the python script and jinja2 templates to the Awesome-Cv repo where the latex files are actually used.

dies ist der testbranch