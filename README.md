# Giles

Giles is a GitHub bot which deploys
[Baldrick](https://github.com/OpenAstronomy/baldbrick), it has the following
features:

* Post Statuses for CircleCI artifacts.
* Check that all PRs have milestones.
* Validate a [towncrier](https://github.com/hawkowl/towncrier) changelog entry
  is present.


[Baldrick](https://github.com/OpenAstronomy/baldbrick) is designed to be
extensible, if you want extra features it's easy to host your own custom bot.

## Getting started

To use Giles, go to https://github.com/apps/giles and add the app to your
repositories.

Then follow the instructions below on how to configure Giles.


## Configuration

Configuration of Giles is done via the `pyproject.toml` file, in the root of
the repository.


### Sphinx HTML Build Status

The CircleCI artifact plugin is enabled by default to post a status for
a sphinx html build. If you add Giles to a repository and add the webhook to
the `.circleci/config.yml` file as such:

    notify:
      webhooks:
        - url: https://giles.cadair.dev/circleci

A status will be posted with a link to your `html/index.html` file.

### Custom CircleCI artifacts

To add a custom artifact link add the following to your `pyproject.toml` file:

    [ tool.gilesbot ]
      [ tool.gilesbot.circleci_artifacts.checkname ]
        url = "my/artifact/path"
        message = "GitHub Status Message."

You can add as many of these as you wish, change `checkname` for each one. You
need the circleci webhook configuration as above.

### Milestone checks

To enable checking of milestones add the following to your `pyproject.toml`
file:

  [ tool.gilesbot ]
    [ tool.gilesbot.pull_requests ]
      enabled = true
    
    [ tool.gilesbot.milestones ]
      enabled = true

You can customise the behaviour of the checks by following the [Baldrick
documentation](https://baldrick.readthedocs.io/en/latest/plugins.html#github-milestone-checker).


### Towncrier Changelog Checking

To enable Towncrier GitHub checks on your Pull Requests add the following to
your `pyproject.toml` file:

  [ tool.gilesbot ]
    [ tool.gilesbot.pull_requests ]
      enabled = true
    
    [ tool.gilesbot.towncrier_changelog ]
      enabled = true

To customise the behaviour follow the [Baldrick
documentation](https://baldrick.readthedocs.io/en/latest/plugins.html#towncrier-changelog-checker).


## Questions or Suggestions

Feel free to open an issue on this repository or on the 
[Baldrick repository](https://github.com/OpenAstronomy/baldrick/issues/new) with feature
requests or bug reports.


## Attribution
<div>Icons made by <a href="https://www.flaticon.com/authors/popcorns-arts"
title="Icon Pond">Icon Pond</a> from <a href="https://www.flaticon.com/"
title="Flaticon">www.flaticon.com</a> is licensed by <a
href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY
3.0" target="_blank">CC 3.0 BY</a></div>
