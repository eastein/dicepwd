# Purpose

To use dicerolls to generate secure passwords.

# Usage

The key arguments are -c for how many characters the password should be and -d for how many sides your die(s) have.

    ./dpwdgen -c 8 -d 6

You will be prompted for the number value of a die until enough entropy has been collected to generate the password according to your request. When the program completes, you will be presented a password to use.

# Future Work

A few additional features are planned.

* add a -b option to specify entropy bits rather than characters of password
* option to specify or configure a password composition policy for dpwdgen to comply with
