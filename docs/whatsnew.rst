What is new?
============

v0.1.8
------
* Fixed typo
* Cleaned up code
* Changed input types from dict to numpy arrays

v0.1.8
------

* Aded new logger
* Added typechecker
* Removed lightning code for now
* Removed example data loader, this is something each user can implement on their own.

v0.1.7
------

* Exception catching version check


v0.1.6
------

* Added version check when running CentralProcessing


v0.1.5
------

* Minor bug fixes.


v0.1.4
------

* Revamped ``CentralProcessing``, it now has proper testing for all the production methods, with types of input and output.

* Added a new section :doc:`conduct_and_info` to the documentation about "How to go about" with Gingerbread.

* Restructured code structure with `modules`.

v0.1.3
------

* An issue where ``ǸotImplementedError`` always ran despite the the methods existing. This has been fixed with a new method in the init function: ``check_obligatory_methods``.

* Some documentation changes.