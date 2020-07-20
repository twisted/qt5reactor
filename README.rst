Qt5Reactor
==========

|PyPI| |Pythons| |GitHub| |GitHub Actions|


.. |PyPI| image:: https://img.shields.io/pypi/v/qt5reactor.svg
   :alt: PyPI version
   :target: https://pypi.org/project/qt5reactor/

.. |Pythons| image:: https://img.shields.io/pypi/pyversions/qt5reactor.svg
   :alt: supported Python versions
   :target: https://pypi.org/project/qt5reactor/

.. |GitHub| image:: https://img.shields.io/github/last-commit/twisted/qt5reactor/master.svg
   :alt: source on GitHub
   :target: https://github.com/twisted/qt5reactor

.. |GitHub Actions| image:: https://github.com/twisted/qt5reactor/workflows/CI/badge.svg
   :alt: GitHub Actions build status
   :target: https://github.com/twisted/qt5reactor/actions


Using the Qt5Reactor
--------------------

Qt5Reactor is compatible with both PyQt5 and PySide2.

Install using pip

::

    pip install qt5reactor

Before running / importing any other Twisted code, invoke:

::

    app = QApplication(sys.argv) # your code to init QtCore
    from twisted.application import reactors
    reactors.installReactor('qt5')

or

::

    app = QApplication(sys.argv) # your code to init QtCore
    import qt5reactor
    qt5reactor.install()

Testing
~~~~~~~

::

   trial --reactor=qt5 [twisted] [twisted.test] [twisted.test.test_internet]

Make sure the plugin directory is in path or in the current directory for
reactor discovery to work.

There is also `pytest-twisted`_ for use with pytest_.
You can specify to use the qt5reactor by adding ``--reactor=qt5reactor``.

.. _pytest-twisted: https://github.com/pytest-dev/pytest-twisted
.. _pytest: https://github.com/pytest-dev/pytest
