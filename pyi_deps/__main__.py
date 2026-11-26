"""Entry point for ``python -m pyi_deps``.

The package has no import side effects, so this module only exists to make the
module form work: ``console_scripts`` gives ``pyi-deps``, but ``-m`` needs a
``__main__`` submodule before Python will run anything.
"""

import sys

from . import main

if __name__ == "__main__":
    sys.exit(main())
