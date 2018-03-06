# Giles

## About


This is a modified version of
[astropy-bot](https://github.com/astropy/astropy-bot) which handles receiving
webhooks from circle ci and adding a commit status with a link to the built
(sphinx) documentation as a commit status.


## Usage

To use this bot, you need to have a circle ci build which uploads build
artefacts. At the moment, this bot is hard-coded to look for the artefact that
matches the path `html/index.html`.

To activate the bot, you need to add the following to the end of your circle ci config file:

```
notify:
  webhooks:
    - url: https://giles.cadair.com/circleci
```

Also you need to enable the bot on your github repository by visiting
https://github.com/apps/giles the app only requests read and write access to
commit statuses.


## Attribution

All the hard work was done in Astropy bot, this is just a deployment of the bot
that does the circle ci documentation link.

<div>Icons made by <a href="https://www.flaticon.com/authors/popcorns-arts"
title="Icon Pond">Icon Pond</a> from <a href="https://www.flaticon.com/"
title="Flaticon">www.flaticon.com</a> is licensed by <a
href="http://creativecommons.org/licenses/by/3.0/" title="Creative Commons BY
3.0" target="_blank">CC 3.0 BY</a></div>

