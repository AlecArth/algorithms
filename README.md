# Algorithms

This repsitory contains the following algorithms along with tests using `SOME_TEST_LIBRARY`:

 - A Linked List
 - A Binary Tree
 - A Graph using an Adjacency List
 - Depth First Search using recursion
 - Breadth First Search using a while loop

## Setup

    conda create -p ./.conda python=3.10 -y
    conda activate ./.conda
    pip install -r requirements.txt

## DFS and BFS

When inserting the following keys into the graph in this order it will create the following graph structure in a binary tree.

Keys: [20, 15, 18, 10, 25, 24, 27, 19, 17, 28]

```mermaid
graph TD
    A((20)) --> B((15))
    A((20)) --> C((25))
    B((15)) --> D((10))
    B((15)) --> E((18))
    E((18)) --> F((17))
    E((18)) --> G((19))
    C((25)) --> H((24))
    C((25)) --> I((27))
    I((27)) --> J((28))
```

### Print keys using DFS
Keys: [20, 15, 10, 18, 17, 19, 25, 24, 27, 28]

```mermaid
graph TD
    A((A 20)) --> B((B 15))
    A((A 20)) --> C((G 25))
    B((B 15)) --> D((C 10))
    B((B 15)) --> E((D 18))
    E((D 18)) --> F((E 17))
    E((D 18)) --> G((F 19))
    C((G 25)) --> H((H 24))
    C((G 25)) --> I((I 27))
    I((I 27)) --> J((J 28))
```

### Print keys using BFS
Keys: [20, 15, 25, 10, 18, 24, 27, 17, 19, 28]

```mermaid
graph TD
    A((A 20)) --> B((B 15))
    A((A 20)) --> C((C 25))
    B((B 15)) --> D((D 10))
    B((B 15)) --> E((E 18))
    E((E 18)) --> F((H 17))
    E((E 18)) --> G((I 19))
    C((C 25)) --> H((F 24))
    C((C 25)) --> I((G 27))
    I((G 27)) --> J((J 28))
```

## Adjacency List

![Adjacency List Graph](adjacency_list.png)
