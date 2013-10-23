""" haf package

"""
print "\nPackage at %s" % __path__[0]

from .base.consoling import getConsole

console = getConsole()

console.terse("\nPackage at {0}\n".format(__path__[0]))

_version = "0.6.4"
console.terse("Version {0}\n".format(_version))

__all__ = ['base', 'trim']

for m in __all__:
    exec "from . import %s" % m  #relative import
    #print "Imported %s" % globals().get(m,'')

#used by CreateAllInstances                 
_InstanceModules = [base, trim]


def CreateAllInstances(store, modules=_InstanceModules):
    """Creates all the instances for this package. Should have blank registry
    """
    console.concise("     Creating instances in package {0} for modules {1}.\n".format(
        __name__, [module.__name__ for module in modules]))

    def CreateModuleInstances(store, modules):
        for module in modules:
            if hasattr(module, '_InstanceModules'): # recurse
                console.concise("     Creating instances in package {0} for modules {1}.\n".format(
                    module.__name__, [amod.__name__ for amod in module._InstanceModules]))
                CreateModuleInstances(store, module._InstanceModules)

            if hasattr(module, 'CreateInstances'):
                console.concise("     Creating instances in module {0}.\n".format(module.__name__))
                module.CreateInstances(store = store)

    CreateModuleInstances(store, modules)