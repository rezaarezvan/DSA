```
Set<Item>:

    /*

    A collection of objects - the set cannot contain duplicates.

    */

    // Returns True if x is in the set, False otherwise
    boolean contains(Item x)

    // Adds x to the set, if it's not already in the set
    void add(Item x)

    // Removes x from the set, if it's present
    void remove(Item x)

    // Returns True if the set is currently empty, False otherwise
    boolean is_empty()

    // Returns the current size (# of elements) in the set
    int size()

    // Iterates over all elements in the set
    Iterator<Item> iterator()
```
