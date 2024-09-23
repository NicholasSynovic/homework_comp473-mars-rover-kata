# 5. Rovers must be aware of orientation

## Status

| Status   | Time                         |
| -------- | ---------------------------- |
| Accepted | 2024-09-23T15:41:31.2533184Z |

## Context

Rovers need to know their orientation with respect to the cardinal directions.

## Decision

Each Rover will keep track of its own cardinal directions. Every time that the
Rover moves, it will move 1 step forward in its respective cardinal direction.

## Consequences

Rovers will have to be able rotate both clockwise and counter clockwise. Every
rotational update will have to update the orientation of the Rover.
