# 11. IO is aware of the Plateau grid

## Status

| Status   | Time                         |
| -------- | ---------------------------- |
| Accepted | 2024-09-23T15:46:22.5540002Z |

## Context

The user should be able to see the current state of the Plateau prior to
executing commands.

## Decision

The IO class will have to be able to access the current Plateau state to print
the Plateau grid to the user.

## Consequences

The IO class will have access to a minimal set of attributes of the Plateau
class in order to fulfill this decision.
