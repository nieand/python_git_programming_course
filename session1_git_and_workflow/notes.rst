Organizing code and data: Advanced Git, Github and more
=======================================================

- Links
    - Make graphs: https://github.com/deuill/grawkit
    - Slides: https://www.slideshare.net/ThomasRausch4/git-introduction-tutorial


    - Print for overhead projector:
        - Vocabulary
        - Basic workflow graph
        - Commands
        - cheat sheet


- Introduce presenters
    - quick intro of 4 sessions
    - interrupt for questions today

- Introduction
    - Screenshot of "final.doc"

    - Why?
        - GIT as solution for versioning files
            --> split work into steps (commits)
            --> forced to describe each step (commit message)
            --> branch, tags: version of software
        - GIT as solution for collaboration
        - GIT for distributing software/code
    - What?
        - versions connected via tree-like graph, each node is a commit
        - GIT: think of commit as changes ("patches")
        - Operations: branch, rebase, cherry-pick, sending commits (push/pull)
    - How?
        - command line
        - GUIs, IDE integration
        - API (eg. Python etc.)

- Nice features:
    - merging
    - git blame
    - biscet

- Git is terrible:
    - Man page generator https://git-man-page-generator.lokaltog.net/

    - real man page: source:
        - git-push – Update remote refs along with associated objects
            git-push – Upload changes from your local repository into a remote repository
        - git-rebase – Forward-port local commits to the updated upstream head
            Translation: git-rebase: re-apply a set of sequential commits on a different branch

        https://git.github.io/htmldocs/git-push.html
        https://git.github.io/htmldocs/git-rebase.html
        https://stevebennett.me/2012/02/24/10-things-i-hate-about-git/

    - https://xkcd.com/1597/

    - More reasons why GIT is bad: https://svnvsgit.com/

    - Still a must-have: Quasi-standard & Github, (speed compared to mercurial)


- Working alone one needs only:
    - init / clone
    - commit
    - push/pull

    --> but the benefit is not very high
    --> explain how working with GIT works in larger teams

- Quick-intro
    - tree
    - hash
    - working tree
    - staging area in between

    - branches: imagine different versions of software

    - commit, branch, checkout, rebase, cherry-pick, merge

    - https://geo-python.github.io/2018/_images/Git_illustration.png


- Something went wrong...
  - https://ohshitgit.com/
  - revert a file in the working tree to the last committed one
  - edit the last commit (before pushing to remote)
  - git reflog


- Excercise: local repo
    - git init
    - git config --global user/mail
    - commit, branch, checkout, rebase, cherry-pick, merge
    - https://learngitbranching.js.org/

- Excercise: merge conflict
    - create a feature branch
    - create a commit


10:15: Remotes
--------------

- Github
    - Decentralized version control system
    - What is a remote?
    - git != Github
    - Alternatives: Gitlab, Bitbucket, your own server, local folder and many more
    - Github is your business card!
        - https://github.com/shoyer
        - https://github.com/gvanrossum

    - Github stars

    - Github features:
        - README
        - Wiki
        - Issue tracker

    - Many things are undeletable
        - Commits (only by changing Sha1)
        - Pull requests
        - Issues

- forced push: rewriting history on the remote

    - Golden rule: don't rewrite history after it leaves your machine
        - Exception: you know what you are doing and won't regret if it turns out you actually didn't
        - Exception: feature branches (or branches you own exclusively)

- style (commit messages)
    - https://xkcd.com/1296/
    - https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53
    - https://chris.beams.io/posts/git-commit/

- Live demo: pull request xarray: typo most -> must
    xarray/core/alignment.py

- Excercise: push to Github
    - Clone the workshop repo with --recursive!
    - git-game



11:00 Large files and workflow
------------------------------

- folder structure
    - no cyclic dependencies
    - README, LICENSE
    - packages: Make, setup.py

- Complete Workflow:
    - Imagine there are 3-8 developers with an idea
    - start sitting together and roughly agree on some goals, (project) names,
      workflow, review
        - how does a repository look like?
    - somebody creates one or more repositories and the initial file/folder
      structure
    - Build server: tests & packages

- what could go wrong: nothing! (reflog)
    - merge conflict
    - publish private data
    - Github: issues, wiki are not deletable

- GIT large files


11:45 How git works
-------------------

- Hashes & Refs
    - What is Sha1?
    - Probability of hash collisions
    - Hashes can be shorted
    - For many Hashes there are symbolic names, like tags
        --> HEAD

- GIT internals (what is a hash?)
    - .git
    - config
    - objects: files, commits
    - hashes
    - refs
        - HEAD
        - refs/heads

What you cannot do with GIT:
- large files (Github: 100MB, everything is stored forever)
- mixing public and private branches in one repository, cloning repos partially
- Jupyter notebooks

- Branching models
    - feature branches

- Fun with GIT
    - cycles in history?
    - GIT coin

