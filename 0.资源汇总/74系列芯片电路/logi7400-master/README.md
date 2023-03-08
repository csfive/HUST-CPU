# Logi7400

[Logisim](http://www.cburch.com/logisim/) 7400 series integrated circuits library.

## Variants

There are two variants of the library with different circuit appearances available:

* In the classic **Logi7400dip** library, the circuit appearance reflects the physical pin layout of the DIP packaged chips.
* The new **Logi7400ic** library provides a logical circuit appearance.

## Goal

This library aims to be a comprehensive 7400 series library for Logisim for designing logical circuits and for educational purposes.

The library should be compatible both with original [Logisim](http://www.cburch.com/logisim/) and [logisim-evolution](https://github.com/reds-heig/logisim-evolution).

## Lists by type

- [Gates](doc/gates.md)
- [Inverters](doc/inverters.md)
- [Flip-Flops and Latches](doc/flip_flops.md)
- [Encoders and Decoders](doc/encoders_decoders.md)
- [Arithmetic and Counters](doc/arithmetic.md)

## Supported Chips

You're welcome to request missing chips by opening an issue.

| Chip                    | Description                                   | Pins | IC  | DIP | Status Docs        |
| ----------------------- | --------------------------------------------- |:----:| --- | --- | ------------------ |
| [7400](doc/7400.md)     | quad 2-input NAND gate                        |  14  | OK  | OK  | OK                 |
| [7402](doc/7402.md)     | quad 2-input NOR gate                         |  14  | OK  | OK  | OK                 |
| [7403](doc/7403.md)     | quad 2-input NAND gate, open collector output |  14  | OK  | OK  | OK                 |
| [7404](doc/7404.md)     | hex inverter                                  |  14  | OK  | OK  | OK                 |
| [7405](doc/7405.md)     | hex inverter, open collector output           |  14  | OK  | OK  | OK                 |
| [7408](doc/7408.md)     | quad 2-input AND gate                         |  14  | OK  | OK  | OK                 |
| [7410](doc/7410.md)     | tripe 3-input NAND gate                       |  14  | OK  | OK  | OK                 |
| [7411](doc/7411.md)     | tripe 3-input AND gate                        |  14  | OK  | OK  | OK                 |
| [7414](doc/7414.md)     | hex Schmitt trigger inverter                  |  14  | OK  | OK  | OK                 |
| [7420](doc/7420.md)     | dual 4-input NAND gate                        |  14  | OK  | OK  | OK                 |
| [7421](doc/7421.md)     | dual 4-input AND gate                         |  14  | OK  | OK  | OK                 |
| [7427](doc/7427.md)     | tripe 3-input NOR gate                        |  14  | OK  | OK  | OK                 |
| [7430](doc/7430.md)     | 8-input NAND gate                             |  14  | OK  | OK  | OK                 |
| [7432](doc/7432.md)     | quad 2-input OR gate                          |  14  | OK  | OK  | OK                 |
| [7442](doc/7442.md)     | 4-bit BCD to 10-line decoder                  |  16  | OK  | OK  | OK                 |
| [7451](doc/7451.md)     | AND-OR-invert gates                           |  14  | OK  | OK  | OK                 |
| [7473](doc/7473.md)     | dual J-K flip-flop                            |  14  | OK  | OK  | OK                 |
| [7474](doc/7474.md)     | dual D-type flip-flop                         |  14  | OK  | OK  | OK                 |
| [7475](doc/7475.md)     | quad D-type latch                             |  16  | OK  | --  | old diagram        |
| [7476](doc/7476.md)     | dual J-K flip-flop                            |  16  | OK  | OK  | OK                 |
| [7485](doc/7485.md)     | 4-bit magnitude comparator                    |  16  | OK  | OK  | layout missing     |
| [7486](doc/7486.md)     | quad 2-input XOR gate                         |  14  | OK  | OK  | OK                 |
| [7493](doc/7493.md)     | 4-bit binary ripple counter                   |  14  | OK  | --  | layout missing     |
| [74107](doc/74107.md)   | dual J-K flip-flop                            |  14  | OK  | --  | OK                 |
| [74109](doc/74109.md)   | dual J-not-K flip-flop                        |  14  | OK  | OK  | OK                 |
| [74112](doc/74112.md)   | dual J-K flip-flop                            |  16  | OK  | --  | OK                 |
| [74132](doc/74132.md)   | quad 2-input NAND Schmitt trigger             |  14  | OK  | --  | OK                 |
| [74137](doc/74137.md)   | 3-bit to 8-line decoder, latched input        |  16  | --  | --  | layout missing     |
| [74138](doc/74138.md)   | 3-bit to 8-line decoder                       |  16  | OK  | OK  | OK                 |
| [74139](doc/74139.md)   | dual 2-bit to 4-line decoder                  |  16  | OK  | OK  | OK                 |
| [74147](doc/74147.md)   | 10-line to 4-bit BCD priority encoder         |  16  | OK  | OK  | OK                 |
| [74151](doc/74151.md)   | 8-line multiplexer                            |  16  | OK  | OK  | OK                 |
| [74153](doc/74153.md)   | dual 4-line multiplexer                       |  16  | OK  | OK  | old diagram        |
| [74157](doc/74157.md)   | quad 2-line multiplexer                       |  16  | OK  | OK  | old diagram        |
| [74161](doc/74161.md)   | 4-bit synchronous binary counter              |  16  | OK  | OK  | pin layout missing |
| [74163](doc/74163.md)   | 4-bit synchronous binary counter              |  16  | OK  | OK  | pin layout missing |
| [74165](doc/74165.md)   | 8-bit parallel in shift register              |  16  | --  | --  | missing            |
| [74173](doc/74173.md)   | quad D-type flip-flop                         |  16  | OK  | --  | OK                 |
| [74174](doc/74174.md)   | hex D-type flip-flop                          |  16  | --  | --  | missing            |
| [74175](doc/74175.md)   | quad D-type flip-flop                         |  16  | OK  | --  | missing            |
| [74181](doc/74181.md)   | 4-bit arithmetic logic unit                   |      | --  | OK  | missing            |
| [74237](doc/74237.md)   | 3-bit to 8-line decoder, latched input        |  16  | --  | --  | missing            |
| [74238](doc/74238.md)   | 3-bit to 8-line decoder                       |  16  | OK  | OK  | old diagram        |
| [74244](doc/74244.md)   | octal buffer                                  |  20  | OK  | OK  | old diagram        |
| [74247](doc/74247.md)   | BCD to 7-segment decoder                      |  16  | --  | OK  | pin layout missing |
| [74259](doc/74259.md)   | octal adressable D-type latch                 |      | --  | --  | missing            |
| [74273](doc/74273.md)   | octal D-type flip-flop                        |  20  | OK  | OK  | old diagram        |
| [74283](doc/74283.md)   | 4-bit binary full adder                       |  16  | OK  | OK  | pin layout missing |
| [74373](doc/74373.md)   | octal transparent D-type latch                |  20  | --  | OK  | pin layout missing |
| [74374](doc/74374.md)   | octal D-type flip-flop                        |  20  | OK  | OK  | pin layout missing |
| [74377](doc/74377.md)   | 8-bit register with clock enable              |  20  | OK  | OK  | missing            |
| [74390](doc/74390.md)   |                                               |      | --  | --  | missing            |
| [74393](doc/74393.md)   |                                               |      | --  | --  | missing            |
| [74534](doc/74534.md)   |                                               |      | --  | --  | missing            |
| [74573](doc/74573.md)   | 8-bit D-type latch                            |  20  | --  | OK  | pin layout missing |
| [74574](doc/74574.md)   | 8-bit D-type flip-flop                        |  20  | --  | OK  | pin layout missing |
| [74595](doc/74595.md)   | 8-bit shift register                          |  16  | --  | OK  | pin layout missing |
| [74670](doc/74670.md)   | 4 by 4 register file                          |      | --  | OK  | missing            |
| [404002](doc/744002.md) | dual 4-input NOR gate                         |  14  | --  | --  | OK                 |
| [744049](doc/744049.md) | hex inverter                                  |  16  | --  | OK  | pin layout missing |
| [744075](doc/744075.md) | triple 3-input OR gate                        |  14  | --  | OK  | OK                 |
| [744511](doc/744511.md) | BCD to 7-segment decoder                      |  16  | --  | OK  | pin layout missing |
| [747266](doc/747266.md) | dual 2-input XNOR gate                        |  14  | --  | --  | OK                 |

## Design Guidelines

To meet these goals, the following design [guidelines](guidelines.md) are met:

* Circuits are build from a minimal set of built-in components.
* The pin layout matches the DIP pinout of the corresponding ICs.
* Automated tests are provided.
* Labels must conform to [VHDL](https://en.wikipedia.org/wiki/VHDL), i.e. start with a letter and contain only letters, digits, or underscores.

## Credits

* [logisim_74v1](http://74x.weebly.com/blog/library-of-7400-logic-for-logisim), Public Domain
* [7400 series Logisim library from Ben Oztalay](http://www.cburch.com/logisim/download/7400-lib.zip): Provided on Logisim web site, Public Domain
