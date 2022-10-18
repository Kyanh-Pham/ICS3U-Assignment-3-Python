#!/usr/bin/env python3

# Created by: Kyanh Pham
# Created on: Oct 2022
# This program sees if you can vote

import constants


def main():
    # This function sees if your age is >=18

    # Input
    age = int(input("Enter your age: "))
    print("")

    # Process and Output
    if age >= constants.VOTING_AGE:
        print("You are eligible to vote!")
    else:
        print("You are not eligible to vote.")

    print("\nDone.")


if __name__ == "__main__":
    main()
