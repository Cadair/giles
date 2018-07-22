import os

from baldrick import create_app


"""
Configure the App
"""

app = create_app('giles-dev')


"""
Configure Plugins
"""

import baldrick.plugins.circleci_artifacts  # noqa
import baldrick.plugins.github_milestones  # noqa
import baldrick.plugins.github_towncrier_changelog  # noqa


# Bind to PORT if defined, otherwise default to 5000.
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port, debug=False)
