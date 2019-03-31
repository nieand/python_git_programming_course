Organizing code and data: Advanced Git, Github and more
=======================================================

Meta
----
- Links
    - Make graphs: https://github.com/deuill/grawkit
    - Slides: https://www.slideshare.net/ThomasRausch4/git-introduction-tutorial
    - How to teach GIT:
        - https://recompilermag.com/issues/issue-0/bad-metaphors/
        - https://recompilermag.com/issues/issue-1/how-to-teach-git/
        - https://software-carpentry.org/blog/2012/12/some-of-the-things-weve-learned-about-teaching-git.html
        - https://jordankasper.com/lessons-learned-teaching-git/

- Prepare Laptop
    - slides
    - Vocabulary + commands
    - github
        - https://github.com/shoyer
        - https://github.com/gvanrossum
    - Style
        - https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53
        - https://chris.beams.io/posts/git-commit/

    - Travis-CI
        - https://travis-ci.org/lumbric/lunchbot/branches
        - https://github.com/lumbric/lunchbot

- Print for overhead projector:
    - Vocabulary
    - Basic workflow graph
    - Commands
    - cheat sheet


Intro
-----

- Introduce presenters
    - quick intro of 4 sessions
    - interrupt for questions today & expect participation
    - quick survey: commands & terms

- Introduction
    - Screenshot of "final.doc"
        - Why is this a bad example?
            - somebody working that chaotic can make a GIT repository chaotic too
            - one person with a completely linear history is
            - docx does not work well with for diff
            - in an abstract.docx one might not need the old versions at all
            - maybe no need to maintain old versions
            - it is not clear how to split work into single consistent steps
            - not clear and maybe no need how to describe these steps

    - What is a version control system and why do I need it?
        - protects yourself and others from yourself and others (backup)
        - collaboration: work on the same project in a team without need of complicated architecture
        - don't afraid change: reverting is easy
        - mark which parts are working and which are broken (stable branch, commits under review etc)
        - review: split work into readable and consistent parts
        - apply a fix to multiple maintained branches
        - develop 5 features and deploy them in arbitrary order to the production system

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
        - difference 1 to copying folders: connections (history)
        - difference 2 to copying folders: operations
        - difference 3 to copying folders: smaller file size
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
        - is it dangerous to delete a branch?

    - commit, branch, checkout, rebase, cherry-pick, merge

    - https://geo-python.github.io/2018/_images/Git_illustration.png


- Something went wrong...
  - https://ohshitgit.com/
  - git reflog


- Some hints:
    - don't leave comments in the code!
    - for command line, use a good command completion!
    - you want to have a tree viewer (terminal or GUI)
    - many commands can be aborted, like git rebase --abort
    - git add again after changing a file


- Excercise: local repo
    - git init
    - git config --global user/mail
    - commit, branch, checkout, rebase, cherry-pick, merge
    - https://learngitbranching.js.org/

- Excercise: merge conflict
    - create a feature branch
    - create a commit

- Exercise:
    - clone some open source repository


10:15: Remotes
--------------

- Remotes
    - Decentralized version control system
    - What is a remote?
    - http, ssh, filesystem...
    - ssh publickeys

- Github
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

    - Warning: Many things are undeletable
        - Commits (only by changing Sha1)
        - Pull requests
        - Issues

- Live demo: pull request xarray: typo most -> must
    xarray/core/alignment.py

- Fix things, rewrite history:
    - commit --ammend
    - checkout
    - reset, reset --hard
    - git rebase -i HEAD~7
    - reflog
    - revert: not!
    - https://ohshitgit.com/

- rewriting history?
    - commit
    - rebase
    - cherry-pick
    - fetch
    - pull
    - push

- forced push: rewriting history on the remote
    - rewrite history: rebase, git commit --amend
    - Golden rule: don't rewrite history after it leaves your machine
        - Exception: you know what you are doing and won't regret if it turns out you actually didn't
        - Exception: feature branches (or branches you own exclusively)

- style (commit messages)
    - https://xkcd.com/1296/
    - https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53
    - https://chris.beams.io/posts/git-commit/

- Excercise: push to Github
    - Clone the workshop repo with --recursive!
    - git-game
    - run as many commands as possible!

- Exercise:
    - create a repository (on github)
    - work in it (commit)
    - somebody else breaks master (evil commit)
    - continue working and rebase your work afterwards!


11:00 Large files and workflow
------------------------------

- Complete Workflow:
    - Imagine there are 3-8 developers with an idea
    - start sitting together and roughly agree on some goals, (project) names, workflow, review

    - folder structure
        - no cyclic dependencies
        - README, LICENSE
        - packages: Make, setup.py
            - how does a repository look like?
            - https://github.com/numpy/numpy/

    - somebody creates one or more repositories and the initial file/folder structure
    - split work in tasks, go agile? :)
    - different ways:
        - every body pushes to master, maybe tags from time to time
        - feature branches & pull request, somebody approves and merges

- Build server: e.g. Travis CI
    - build packages & run tests (and other tasks?)
    - https://travis-ci.org/lumbric/lunchbot/branches
    - https://github.com/lumbric/lunchbot


- what could go wrong: nothing!
    - publish private data
    - Github: issues, wiki are not deletable
    - merge conflicts might be complicated and surprising
    - start something and end in a weird state (e.g. git rebase)
        --> ohshitgit

- GIT large files
    - git lfs
    - DVC
    - ...?

What you cannot do with GIT:
- large files (Github: 100MB, everything is stored forever)
- mixing public and private branches in one repository, cloning repos partially
- Jupyter notebooks: nbdime


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
        - git cat -p file COMMIT
        - git ls-tree COMMIT
        - commmit: da483
        - file: 8e8bd5
          --> cat 8bd5 | pigz -d
    - hashes
    - refs
        - HEAD
        - refs/heads

- Fun with GIT
    - cycles in history?
    - GIT coin

