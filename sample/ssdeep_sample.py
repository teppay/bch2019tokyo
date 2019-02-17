#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ssdeep

def same_str():
    str1 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
              sed do eiusmod tempor incididunt ut labore et dolore magna 
              aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
              ullamco laboris nisi ut aliquip ex ea commodo consequat. 
              Duis aute irure dolor in reprehenderit in voluptate velit 
              esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
              occaecat cupidatat non proident, sunt in culpa qui officia 
              deserunt mollit anim id est laborum."""
    str2 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
              sed do eiusmod tempor incididunt ut labore et dolore magna 
              aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
              ullamco laboris nisi ut aliquip ex ea commodo consequat. 
              Duis aute irure dolor in reprehenderit in voluptate velit 
              esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
              occaecat cupidatat non proident, sunt in culpa qui officia 
              deserunt mollit anim id est laborum."""
    hash1 = ssdeep.hash(str1)
    hash2 = ssdeep.hash(str2)

    result = ssdeep.compare(hash1, hash2)
    print(result)

def difference_of_a_word():
    str1 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
              sed do eiusmod tempor incididunt ut labore et dolore magna 
              aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
              ullamco laboris nisi ut aliquip ex ea commodo consequat. 
              Duis aute irure dolor in reprehenderit in voluptate velit 
              esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
              occaecat cupidatat non proident, sunt in culpa qui officia 
              deserunt mollit anim id est laborum."""
    # First word: Lorem -> Hello
    str2 = """Hello ipsum dolor sit amet, consectetur adipiscing elit, 
              sed do eiusmod tempor incididunt ut labore et dolore magna 
              aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
              ullamco laboris nisi ut aliquip ex ea commodo consequat. 
              Duis aute irure dolor in reprehenderit in voluptate velit 
              esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
              occaecat cupidatat non proident, sunt in culpa qui officia 
              deserunt mollit anim id est laborum."""
    hash1 = ssdeep.hash(str1)
    hash2 = ssdeep.hash(str2)

    result = ssdeep.compare(hash1, hash2)
    print(result)

def difference_of_a_sentence():
    str1 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
              sed do eiusmod tempor incididunt ut labore et dolore magna 
              aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
              ullamco laboris nisi ut aliquip ex ea commodo consequat. 
              Duis aute irure dolor in reprehenderit in voluptate velit 
              esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
              occaecat cupidatat non proident, sunt in culpa qui officia 
              deserunt mollit anim id est laborum."""

    str2 = """We are really enjoying this hackathon, but I want to go to bed 
              as soon as possible.Ut enim ad minim veniam, quis nostrud exercitation 
              ullamco laboris nisi ut aliquip ex ea commodo consequat. 
              Duis aute irure dolor in reprehenderit in voluptate velit 
              esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
              occaecat cupidatat non proident, sunt in culpa qui officia 
              deserunt mollit anim id est laborum."""
    hash1 = ssdeep.hash(str1)
    hash2 = ssdeep.hash(str2)

    result = ssdeep.compare(hash1, hash2)
    print(result)

def difference_of_half_of_str():
    str1 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
              sed do eiusmod tempor incididunt ut labore et dolore magna 
              aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
              ullamco laboris nisi ut aliquip ex ea commodo consequat. 
              Duis aute irure dolor in reprehenderit in voluptate velit 
              esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
              occaecat cupidatat non proident, sunt in culpa qui officia 
              deserunt mollit anim id est laborum."""
    str2 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
              sed do eiusmod tempor incididunt ut labore et dolore magna 
              aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
              ullamco laboris nisi ut aliquip ex ea commodo consequat. 
              In sagittis mi sit amet risus ultrices pellentesque. Aliquam
               a arcu et felis dignissim iaculis. Mauris ut erat neque. 
               Pellentesque sapien quam, efficitur vitae ex in, cursus 
               volutpat dolor. Quisque et lectus nunc. Quisque vulputate 
               est odio, quis molestie tortor interdum sit amet."""
    hash1 = ssdeep.hash(str1)
    hash2 = ssdeep.hash(str2)

    result = ssdeep.compare(hash1, hash2)
    print(result)

def different_str():
    str1 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
              sed do eiusmod tempor incididunt ut labore et dolore magna 
              aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
              ullamco laboris nisi ut aliquip ex ea commodo consequat. 
              Duis aute irure dolor in reprehenderit in voluptate velit 
              esse cillum dolore eu fugiat nulla pariatur. Excepteur sint 
              occaecat cupidatat non proident, sunt in culpa qui officia 
              deserunt mollit anim id est laborum."""
    str2 = """In sagittis mi sit amet risus ultrices pellentesque. Aliquam 
              a arcu et felis dignissim iaculis. Mauris ut erat neque. 
              Pellentesque sapien quam, efficitur vitae ex in, cursus v
              olutpat dolor. Quisque et lectus nunc. Quisque vulputate 
              est odio, quis molestie tortor interdum sit amet. Nam iaculis 
              feugiat vulputate. Sed ac massa nisi. Vestibulum pellentesque 
              viverra augue eget imperdiet. Donec dictum vulputate diam, sed 
              fringilla erat scelerisque id. Vivamus augue arcu, porta id 
              blandit ac, convallis at sapien. Nullam facilisis consequat 
              turpis, in ultricies augue sagittis sit amet. Orci varius natoque 
              penatibus et magnis dis parturient montes, nascetur ridiculus mus. 
              Nullam egestas feugiat porttitor."""
    hash1 = ssdeep.hash(str1)
    hash2 = ssdeep.hash(str2)

    result = ssdeep.compare(hash1, hash2)
    print(result)

if __name__ == '__main__':
    same_str()
    difference_of_a_word()
    difference_of_a_sentence()
    difference_of_half_of_str()
    different_str()