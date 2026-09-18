"""
Course environment compatibility setup.

Importing this module applies runtime patches needed to make the course
notebooks work with the current Python environment.

Currently patches:
  - In pandas 3.0+, `pandas.util._decorators.deprecate_kwarg` no longer
    accepts the call patterns that statsmodels 0.14.6 uses to apply it
    as a decorator (e.g. `@deprecate_kwarg("unbiased", "adjusted")`).
    This causes statsmodels' submodules (tsa.arima, tsa.stattools, etc.)
    to fail at import time.

    This module replaces `deprecate_kwarg` with a no-op decorator factory
    that simply returns the decorated function unchanged. This is safe
    because `deprecate_kwarg`'s only runtime role is to redirect deprecated
    keyword argument names to their new names; course notebooks never use
    the deprecated names, so skipping the redirection has no observable
    effect on results.

When the course environment pins pandas to a compatible version
(`pandas<3.0`) or when statsmodels publishes a fixed release, this module
becomes unnecessary. To disable the patch without removing the file,
replace the body of `_patch_deprecate_kwarg()` with `pass`.

Students do not need to read or modify this file.
"""

import sys


def _patch_deprecate_kwarg():
    """
    Replace `pandas.util._decorators.deprecate_kwarg` with a no-op
    decorator factory.

    The real `deprecate_kwarg` in pandas 3.0 rejects the call patterns
    used by statsmodels 0.14.6, so we cannot delegate to the real
    implementation in any code path. Instead, every call to the
    patched `deprecate_kwarg` returns a decorator that leaves the
    target function exactly as it is.
    """
    try:
        import pandas.util._decorators as _dec
    except ImportError:
        # pandas is not installed; nothing to patch
        return

    if not hasattr(_dec, "deprecate_kwarg"):
        # API has changed beyond what we know how to patch; bail out
        return

    def _noop_deprecate_kwarg(*args, **kwargs):
        """
        Stand-in for `pandas.util._decorators.deprecate_kwarg`.

        Accepts any positional and keyword arguments (so it works with
        every call signature statsmodels might use) and returns a
        decorator that does nothing to the function it wraps.
        """
        def _identity_decorator(func):
            return func
        return _identity_decorator

    _dec.deprecate_kwarg = _noop_deprecate_kwarg


def _clear_statsmodels_module_cache():
    """
    Remove any partially-loaded statsmodels modules from `sys.modules`.

    If a notebook tried to import statsmodels before this setup ran and
    the import failed, Python may have cached a broken half-loaded module.
    The next attempt would find the cached entry and skip re-importing,
    even though the patch is now in place. Clearing the cache forces a
    clean re-import.
    """
    for module_name in list(sys.modules.keys()):
        if module_name.startswith("statsmodels"):
            del sys.modules[module_name]


# Apply patches on import.
_patch_deprecate_kwarg()
_clear_statsmodels_module_cache()
