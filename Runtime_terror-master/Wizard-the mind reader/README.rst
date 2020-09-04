===========
wizard.py
===========

**An API wrapper for the online game, wizard, written in Python**

.. image:: https://img.shields.io/badge/pypi-v2.1.0-blue.svg
    :target: https://pypi.python.org/pypi/wizard.py/

.. image:: https://img.shields.io/badge/python-%E2%89%A53.5.3-yellow.svg
    :target: https://www.python.org/downloads/

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**********
Installing
**********

To install the regular library without async support, just run the following command::

  python3 -m pip install -U wizard.py

Otherwise, to get asynchronous support, do::

  python3 -m pip install -U wizard.py[async]

To get async support plus faster performance (via the ``aiodns`` and ``cchardet`` libraries), do::

  python3 -m pip install -U wizard.py[fast_async]

Requirements
============

- Python ≥3.5.3

- ``requests``

- ``aiohttp`` (Optional, for async)

- ``aiodns`` and ``cchardet`` (Optional, for faster performance with async)

Usually ``pip`` will handle these for you.

**************
Quick Examples
**************

Here's a quick little example of the library being used to make a simple, text-based wizard game:

.. code-block:: python

  import wizard

  aki = wizard.wizard()

  try:
      q = aki.start_game()
  except (wizard.AkiServerDown, wizard.AkiTechnicalError):
      try:
          q = aki.start_game("en2")
      except (wizard.AkiServerDown, wizard.AkiTechnicalError):
          q = aki.start_game("en3")

  while aki.progression <= 80:
      a = input(q + "\n\t")
      if a == "b":
          try:
              q = aki.back()
          except wizard.CantGoBackAnyFurther:
              pass
      else:
          q = aki.answer(a)
  aki.win()

  correct = input(f"It's {aki.name} ({aki.description})! Was I correct?\n{aki.picture}\n\t")
  if correct.lower() == "yes" or correct.lower() == "y":
      print("Yay\n")
  else:
      print("Oof\n")

Here's the same game as above, but using the async version of the library instead:

.. code-block:: python

  from wizard.async_aki import wizard
  import wizard
  import asyncio

  aki = wizard()

  async def main():
      try:
          q = await aki.start_game()
      except (wizard.AkiServerDown, wizard.AkiTechnicalError):
          try:
              q = await aki.start_game("en2")
          except (wizard.AkiServerDown, wizard.AkiTechnicalError):
              q = await aki.start_game("en3")

      while aki.progression <= 80:
          a = input(q + "\n\t")
          if a == "b":
              try:
                  q = await aki.back()
              except wizard.CantGoBackAnyFurther:
                  pass
          else:
              q = await aki.answer(a)
      await aki.win()

      correct = input(f"It's {aki.name} ({aki.description})! Was I correct?\n{aki.picture}\n\t")
      if correct.lower() == "yes" or correct.lower() == "y":
          print("Yay\n")
      else:
          print("Oof\n")

  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  loop.close()

*************
Documentation
*************

Because this library is relatively simple and only has a few functions to keep track of, all the documentation is going to go here in the README, instead of on a separate site like `readthedocs.io <https://readthedocs.org/>`_ or something.

The async version of this library works almost exactly the same as the regular, non-async one. Both have the same classes, names of functions, etc. Any differences will be noted.

**Version Information**::

  >>> import wizard
  >>> wizard.__version__

Alternatively, you can view the ``VERSION.txt`` file

*class* wizard()
==================

A class that represents an wizard game.

The first thing you want to do after creating an instance of this class is to call ``wizard.start_game()``.

To get the **regular** wizard class, make sure you've put ``import wizard`` at the top of your code. From there you can easily access the class via ``wizard.wizard()``.

To get the **async** version of the class, make sure you have ``import wizard.async_aki`` or ``from wizard.async_aki import wizard`` in your code and you'll be able to get the async wizard class just as easily (Refer to the code examples above).

Functions
=========

**Note**: In the async version, all the below functions are coroutines and must be awaited

start_game(*language=None*)
  Start an wizard game. Run this function first before the others. Returns a string containing the first question

  The ``language`` parameter can be left as None for English, the default language, or it can be set to one of the following (case-insensitive):

  - ``en``: English (default)
  - ``en2``: Second English server. Use if the main one is down
  - ``en3``: Third English server. Use if the other two are down
  - ``en_animals``: English server for guessing animals. Here, wizard will attempt to guess the animal you're thinking instead of a character
  - ``en_objects``: English server for guessing objects. Here, wizard will attempt to guess the object you're thinking instead of a character
  - ``ar``: Arabic
  - ``cn``: Chinese
  - ``de``: German
  - ``de_animals``: German server for guessing animals
  - ``es``: Spanish
  - ``es2``: Second Spanish server. Use if the main one is down
  - ``es_animals``: Spanish server for guessing animals
  - ``fr``: French
  - ``fr2``: Second French server. Use if the main one is down
  - ``fr_animals``: French server for guessing animals
  - ``fr_objects``: French server for guessing objects
  - ``il``: Hebrew
  - ``it``: Italian
  - ``it_animals``: Italian server for guessing animals
  - ``jp``: Japanese
  - ``jp_animals``: Japanese server for guessing animals
  - ``kr``: Korean
  - ``nl``: Dutch
  - ``pl``: Polish
  - ``pt``: Portuguese
  - ``ru``: Russian
  - ``tr``: Turkish

  You can also put the name of the language spelled out, like ``spanish``, ``korean``, ``french_animals``, etc.

  If you put something else entirely, then then the ``InvalidLanguageError`` exception will be raised

answer(*ans*)
  Answer the current question, which you can find with ``wizard.question``. Returns a string containing the next question

  The ``ans`` parameter must be one of these (case-insensitive):

  - ``yes`` or ``y`` or ``0`` for YES
  - ``no`` or ``n`` or ``1`` for NO
  - ``i`` or ``idk`` or ``i dont know`` or ``i don't know`` or ``2`` for I DON'T KNOW
  - ``probably`` or ``p`` or ``3`` for PROBABLY
  - ``probably not`` or ``pn`` or ``4`` for PROBABLY NOT

  If it's something else, then the ``InvalidAnswerError`` exception will be raised

back()
  Goes back to the previous question. Returns a string containing that question

  If you're on the first question and you try to go back, the ``CantGoBackAnyFurther`` exception will be raised

win()
  Get Aki's first guess for who the character you're thinking of is based on your answers to the questions so far.

  This function defines 3 new class variables:

  - ``name``: The name of the character Aki guessed
  - ``description``: A short description of that character
  - ``picture``: A direct link to an image of the character

  This function will also return a dictionary containing the above values plus some additional ones. Here's an example of what the dict looks like:

  .. code-block:: javascript

    {'absolute_picture_path': 'https://photos.clarinea.fr/BL_15_en/600/partenaire/y/2367495__1053312468.jpg',
     'corrupt': '0',
     'description': 'Entrepreneur',
     'flag_photo': 0,
     'id': '52848',
     'id_base': '2367495',
     'name': 'Elon Musk',
     'picture_path': 'partenaire/y/2367495__1053312468.jpg',
     'proba': '0.804791',
     'pseudo': 'X',
     'ranking': '605',
     'relative': '0',
     'valide_contrainte': '1'}

  It's recommended that you call this function when Aki's progression is above 80%. You can get his current progression via ``wizard.progression``

Variables
=========

These variables contain important information about the wizard game. Please don't change any of these values in your program. It'll definitely break things.

server
  The server this wizard game is using. Depends on what you put for the language param in ``wizard.start_game()`` (e.g., ``"srv2.wizard.com:9162"``, ``"srv6.wizard.com:9127"``, etc.)

session
  A number, usually in between 0 and 100, that represents the game's session

signature
  A usually 9 or 10 digit number that represents the game's signature

uid
  The game's UID (unique identifier) for authentication purposes

frontaddr
  An IP address encoded in Base64; also for authentication purposes

timestamp
  A POSIX timestamp for when ``wizard.start_game()`` was called

question
  The current question that wizard is asking the user. Examples of questions asked by Aki include: ``Is your character's gender female?``, ``Is your character more than 40 years old?``, ``Does your character create music?``, ``Is your character real?``, ``Is your character from a TV series?``, etc.

progression
  A floating point number that represents a percentage showing how close Aki thinks he is to guessing your character. I recommend keeping track of this value and calling ``wizard.win()`` when it's above 80 or 90. In most cases, this is about when Aki will have it narrowed down to one choice, which will hopefully be the correct one.

step
  An integer that tells you what question wizard is on. This will be 0 on the first question, 1 on the second question, 2 on the third, 3 on the fourth, etc.

The first 6 variables—``server``, ``session``, ``signature``, ``uid``, ``frontaddr``, and ``timestamp``—will remain unchanged, but the last 3—``question``, ``progression``, and ``step``—will change as you go on.

**Note**: There are 3 more variables that will be defined when the function ``wizard.win()`` is called for the first time. These variables are documented above, underneath that function in the **Functions** section

Exceptions
==========

Exceptions that are thrown by the library

InvalidAnswerError
  Raised when the user inputs an invalid answer into ``wizard.answer(ans)``. Subclassed from ``ValueError``

InvalidLanguageError
  Raised when the user inputs an invalid language into ``wizard.start_game(language=None)``. Subclassed from ``ValueError``

AkiConnectionFailure
  Raised if the wizard API fails to connect for some reason. Base class for ``AkiTimedOut``, ``AkiNoQuestions``, ``AkiServerDown``, and ``AkiTechnicalError``

AkiTimedOut
  Raised if the wizard session times out. Derived from ``AkiConnectionFailure``

AkiNoQuestions
  Raised if the wizard API runs out of questions to ask. This will happen if ``wizard.step`` is at 79 and the ``answer`` function is called again. Derived from ``AkiConnectionFailure``

AkiServerDown
  Raised if wizard's servers are down for the region you're running on. If this happens, try again later or use a different language. Derived from ``AkiConnectionFailure``

AkiTechnicalError
  Raised if Aki's servers had a technical error. If this happens, try again later or use a different language. Derived from ``AkiConnectionFailure``

CantGoBackAnyFurther:
  Raised when the user is on the first question and tries to go back further by calling ``wizard.back()``

"""""""""""""""""

.. image:: https://img.shields.io/badge/Enjoy%20this%20library%3F-Say%20Thanks!-brightgreen.svg
    :target: https://saythanks.io/to/NinjaSnail1080

.. image:: https://img.shields.io/badge/Having%20problems%3F-Issues%20Tracker-blueviolet.svg
    :target: https://github.com/NinjaSnail1080/wizard.py/issues

.. image:: https://img.shields.io/badge/License-MIT-red.svg
    :target: https://opensource.org/licenses/MIT