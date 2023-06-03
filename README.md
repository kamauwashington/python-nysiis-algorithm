# NYSIIS Algorithm in Python 3+

> This repository is purely for reference and is illustrative in it is purpose. This is one of the many ways of implementing this algorithm. 


This project illustrates an implementation of the [NYSIIS Algorithm](https://en.wikipedia.org/wiki/New_York_State_Identification_and_Intelligence_System) in Python. The NYSIIS Algorithm is a phonetic algorithm that can match words or names in a reductive form. The New York State Identification and Intelligence System (NYSIIS) was devised in 1970 and is 2.7% more accurate than the standard Soundex algorithm.

Examples would be **Bishop** to **BASAP**, or **Willis** to **WALA**, as they are reduced to a form that can be easily matched by similar words or names.

## Examples

| Word     | Translation |
|----------|-------------|
| Harper   | HARBAR      |
| Chapman  | CAPNAN      |
| O'Daniel | ODANAL      |
| Willis   | WALA        |
| LouisXVI | LASXV       |
| Jacobs   | JACAB       |


> **IMPORTANT**
>
> This algorithm was authored to be *readable* as to the steps to achieve consistant and expected NYSIIS codes given the specification provided. 
 **This code can be refactored to be more compact and performant if needed.**


## Prerequisites

Before you continue, ensure you have met the following requirements:

* Python 3 installed
* PyTest installed (to run the unit tests if need be)

## Running / Testing

* Run **pytest** from the command line 


## Notes

* This implementaton uses standard Python string maninulation vs **REGEX** as to apply the basics needed to create codes. While REGEX would be easier to
write, a vanilla string manipulation implementation illustrates some of the intracacies of the algorithm, and *may* perform better
* This repository is heavily commented to provide context as to what and why, if in VS Code feel free to collapse all comments if they are obtrusive
    * On Mac -> Press <kbd>&#8984;</kbd> + <kbd>K</kbd> then <kbd>&#8984;</kbd> + <kbd>/</kbd> 
    * On Windows & Linux -> Press <kbd>Ctrl</kbd> + <kbd>K</kbd> then <kbd>Ctrl</kbd> + <kbd>/</kbd> 
* The NYSIIS validation words are from various sites across the web, there will be more added and augmentation of the algorithm when edge cases are found.

## Try / Ask

* authoring this implementation or parts of it using REGEX, observe the performance at scale (try 10,000 iterations or more)
* Why do all examples have *Matthews* return as *MATA* when the last step states that a trailing *A* should be removed? 