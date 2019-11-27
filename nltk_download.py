"""
Downloads the averaged_perceptron_tagger package.
This script is a workaround to prevent SSL errors.

Source: https://github.com/gunthercox/ChatterBot/issues/930#issuecomment-322111087
"""

package = 'averaged_perceptron_tagger'

import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download(package)
