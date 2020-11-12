# regex-tester

The repository contains a simple regex auto marker for B36, specifically targeting the B36 fall 2020 tt3 Q11.

## Requirements

`
python3
`

There are no other requirements since the simple GUI implemented here is by tkinter which is the standard python library.

## How the generate test suite

The tests are built specifically for B36 fall 2020 tt3 Q11. Generating the tests by running

`
$ python3 generator.py LEN
`

where LEN is the maximum length for the test string

#### Running without GUI

`
$ python3 tester.py
`

### Running with simple GUI

`
$ python3 tester-gui.py
`
