# Secret Santa Generator

## Description

This script takes a list of names and pairs them up for Secret Santa. It generates a list of `.txt` files for distributing to the participants, preventing the organizer (you!) from having to see who got who.

## Steps

 1. Download the script and update the names listed under `names` to reflect the participants, including the yourself.
 2. Run the script (ie: `$ python3 SecretSanta.py`). A `.txt` file per name should be generated, along with a `Matches.txt` file containing all of the pairings.
 3. Without opening any of the `.txt` files, send them to the associated person. Only open your own file.

`Matches.txt` is meant to be a source for a 3rd party to verify the pairings if needed. It should **not** be opened by any of the Secret Santa participants.

Obviously, a 3rd party could've just arranged these pairings, but this is more fun.
