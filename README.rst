Qt5Reactor

Using the QtReactor
-------------------

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
