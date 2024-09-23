# 2. Plateau must be rectangular

## Status

| Status   | Time                         |
| -------- | ---------------------------- |
| Accepted | 2024-09-23T15:40:26.2862605Z |

## Context

The Mar's plateau where the rover's land is stated to be rectangular. It doesn't
state that it is a three dimensional plateau.

## Decision

The Plateau object will leverage a 2-dimensional array to represent the Mar's
plateau. Empty spaces will be denoted by 0, and non-empty spaces will be the
rover ID.

## Consequences

Rovers need a rover ID. The Plateau object will take in a width and length
argument to specify the size of the Plateau.
