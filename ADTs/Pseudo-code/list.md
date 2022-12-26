```
List<Item>:

    /*
    A list is a generalised stack/queue (using dynamic arrays or linked lists)

    We don't restrict to only remove the front/end element.
    */

    // Inserts Item X at position i in the list
    void add(Item x, int i)

    // Removes and returns the item at position i
    Item remove(int i)

    // Returns the element on position i
    Item get(int i)

    // Sets/replaces element i with x
    void set(int i, Item x)

    // Returns True if the list is currently empty, otherwise False
    boolean is_empty()

    // Returns the current size (# of elements) in the list
    int size()
```
