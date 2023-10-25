# Expose only this class
# The _another module is 'hidden' so while it while become an attribute of this module
# when we import it, it won't show up when we tab-complete

from ._another import AnotherClass
